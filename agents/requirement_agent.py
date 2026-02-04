# Output of this agent feeds into Service Design Agent
import json
from typing import Dict

def extract_requirements(feature_text: str) -> Dict:
    """
    Requirement Agent v1
    Converts SDV feature text into structured service requirements.
    """

    # For now, rule-based (LLM will come next session)
    return {
        "feature_name": feature_text,
        "services": [
            {
                "service_name": "ECUHealthMonitor",
                "description": "Monitors ECU health and detects fault conditions",
                "inputs": ["ECU_ID", "Sensor_Data"],
                "outputs": ["Health_Status", "Fault_Code"],
                "constraints": ["Real-time", "ASIL-B"],
                "dependencies": ["CAN Bus", "OTA Service"]
            }
        ],
        "non_functional": {
            "latency_ms": 50,
            "safety_standard": "ISO 26262",
            "update_method": "OTA"
        }
    }

if __name__ == "__main__":
    sample = "Vehicle Health and Diagnostics"
    print(json.dumps(extract_requirements(sample), indent=2))
