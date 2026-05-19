import json
import requests
from jsonschema import validate, ValidationError

OLLAMA_URL = "http://localhost:11434/api/generate"

SCHEMA_PATH = "schemas/sdv_service_schema.json"


def load_schema():
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def build_prompt(feature_text: str) -> str:
    return f"""
You are an expert Software Defined Vehicle systems engineer.

Convert the following SDV feature requirement into structured JSON.

Rules:
- Output ONLY valid JSON
- No markdown
- No explanations

Feature:
{feature_text}

JSON format:
{{
  "feature_name": "...",
  "services": [
    {{
      "service_name": "...",
      "description": "...",
      "inputs": [],
      "outputs": [],
      "constraints": [],
      "dependencies": []
    }}
  ],
  "non_functional": {{
    "latency_ms": 0,
    "safety_standard": "...",
    "update_method": "..."
  }}
}}
"""


def call_ollama(prompt: str) -> str:

    payload = {
        "model": "llama3.1",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=payload
    )

    response.raise_for_status()

    return response.json()["response"]


def extract_json(text: str):

    text = text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "")
        text = text.replace("```", "")
        text = text.strip()

    return json.loads(text)


def extract_requirements(feature_text: str, retries: int = 2):

    schema = load_schema()

    prompt = build_prompt(feature_text)

    last_error = None

    for attempt in range(retries + 1):

        raw_output = call_ollama(prompt)

        try:

            parsed = extract_json(raw_output)

            validate(
                instance=parsed,
                schema=schema
            )

            return parsed

        except (json.JSONDecodeError, ValidationError) as e:

            last_error = str(e)

            prompt += f"""

The previous output was invalid.

Fix the JSON.

Error:
{last_error}
"""

    raise RuntimeError(
        f"Failed after retries. Last error: {last_error}"
    )


if __name__ == "__main__":

    sample_input = """
    Vehicle Health and Diagnostics:
    Monitor ECU health,
    detect faults,
    and report anomalies via OTA.
    """

    result = extract_requirements(sample_input)

    print(json.dumps(result, indent=2))