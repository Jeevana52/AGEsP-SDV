import os
from typing import Dict


def generate_fastapi_service(service_spec: Dict, output_dir: str = "generated") -> str:
    """
    Code Generation Agent v1
    Generates a minimal FastAPI microservice skeleton from a microservice spec.
    """

    service_name = service_spec["name"]
    service_folder = os.path.join(output_dir, service_name)

    os.makedirs(service_folder, exist_ok=True)

    main_py = f"""from fastapi import FastAPI

app = FastAPI(title="{service_name}")

@app.get("/health")
def health():
    return {{"status": "ok"}}

@app.get("/faults")
def faults():
    return {{"faults": []}}
"""

    requirements_txt = "fastapi\nuvicorn\n"

    dockerfile = """FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY main.py .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

    with open(os.path.join(service_folder, "main.py"), "w", encoding="utf-8") as f:
        f.write(main_py)

    with open(os.path.join(service_folder, "requirements.txt"), "w", encoding="utf-8") as f:
        f.write(requirements_txt)

    with open(os.path.join(service_folder, "Dockerfile"), "w", encoding="utf-8") as f:
        f.write(dockerfile)

    return service_folder


if __name__ == "__main__":
    print("Running Code Generation Agent v1...")

    sample = {
        "name": "ecuhealthmonitor-service",
        "description": "Handles ECU health monitoring and diagnostics",
        "apis": [
            {"endpoint": "/health", "method": "GET"},
            {"endpoint": "/faults", "method": "GET"}
        ]
    }

    folder = generate_fastapi_service(sample)
    print(f"Generated service in: {folder}")
