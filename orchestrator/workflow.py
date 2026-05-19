import json

from agents.requirement_agent import extract_requirements
from agents.service_design_agent import design_services
from agents.code_generation_agent import generate_fastapi_service


def run_pipeline(feature_text: str):

    print("\n[1] Running Requirement Agent...\n")

    requirements = extract_requirements(feature_text)

    print(json.dumps(requirements, indent=2))

    print("\n[2] Running Service Design Agent...\n")

    service_design = design_services(requirements)

    print(json.dumps(service_design, indent=2))

    print("\n[3] Running Code Generation Agent...\n")

    generated_services = []

    for service in service_design["microservices"]:

        folder = generate_fastapi_service(service)

        generated_services.append(folder)

    print("\nGenerated Services:\n")

    for folder in generated_services:
        print(f"- {folder}")

    print("\nPipeline completed successfully.")


if __name__ == "__main__":

    sample_feature = """
    Vehicle Health Monitoring:
    Monitor ECU failures,
    detect anomalies,
    and report diagnostics via OTA.
    """

    run_pipeline(sample_feature)