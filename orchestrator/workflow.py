import json

from agents.planner_agent import create_plan
from agents.requirement_agent import extract_requirements
from agents.service_design_agent import design_services
from agents.code_generation_agent import generate_fastapi_service
from agents.critic_agent import review_services


def run_pipeline(feature_text: str):

    print("\n========== PLANNER AGENT ==========\n")

    plan = create_plan(feature_text)

    print(json.dumps(plan, indent=2))

    print("\n========== REQUIREMENT AGENT ==========\n")

    requirements = extract_requirements(feature_text)

    print(json.dumps(requirements, indent=2))

    print("\n========== SERVICE DESIGN AGENT ==========\n")

    service_design = design_services(requirements)

    print(json.dumps(service_design, indent=2))

    print("\n========== CODE GENERATION AGENT ==========\n")

    generated_services = []

    for service in service_design["microservices"]:

        folder = generate_fastapi_service(service)

        generated_services.append(folder)

    print("\nGenerated Services:\n")

    for folder in generated_services:
        print(f"- {folder}")

    print("\n========== CRITIC AGENT ==========\n")

    review = review_services(service_design)

    print(json.dumps(review, indent=2))

    print("\nPipeline completed successfully.")


if __name__ == "__main__":

    sample_feature = """
    Vehicle Health Monitoring:
    Monitor ECU failures,
    detect anomalies,
    and report diagnostics via OTA.
    """

    run_pipeline(sample_feature)