from typing import Dict, List

def design_services(requirement_spec: Dict) -> Dict:
    """
    Service Design Agent v1
    Converts SDV requirement specs into microservice designs.
    """

    services = []

    for svc in requirement_spec.get("services", []):
        services.append({
            "name": f"{svc['service_name'].lower()}-service",
            "description": svc.get("description", ""),
            "apis": [
                {"endpoint": "/health", "method": "GET"},
                {"endpoint": "/faults", "method": "GET"}
            ],
            "data_contract": svc.get("outputs", []),
            "runtime": "AUTOSAR Adaptive",
            "communication": "SOME/IP"
        })

    return {"microservices": services}


if __name__ == "__main__":
    sample_requirements = {
        "services": [
            {
                "service_name": "ECUHealthMonitor",
                "description": "Monitors ECU health and detects faults",
                "outputs": ["Health_Status", "Fault_Code"]
            }
        ]
    }

    print(design_services(sample_requirements))
