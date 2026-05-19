import json


def review_services(service_design):

    issues = []

    for service in service_design.get("microservices", []):

        apis = service.get("apis", [])

        api_endpoints = [
            api.get("endpoint")
            for api in apis
        ]

        if "/health" not in api_endpoints:
            issues.append(
                f"{service['name']} missing /health endpoint"
            )

        if "/faults" not in api_endpoints:
            issues.append(
                f"{service['name']} missing /faults endpoint"
            )

    result = {
        "status": "success" if not issues else "warning",
        "issues": issues
    }

    return result


if __name__ == "__main__":

    sample_design = {
        "microservices": [
            {
                "name": "ecu-service",
                "apis": [
                    {"endpoint": "/health"}
                ]
            }
        ]
    }

    print(
        json.dumps(
            review_services(sample_design),
            indent=2
        )
    )