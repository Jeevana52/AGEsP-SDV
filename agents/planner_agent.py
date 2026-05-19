import json


def create_plan(feature_text: str):

    plan = {
        "tasks": [
            {
                "step": 1,
                "agent": "Requirement Agent",
                "goal": "Extract SDV requirements from feature text"
            },
            {
                "step": 2,
                "agent": "Service Design Agent",
                "goal": "Convert requirements into microservice architecture"
            },
            {
                "step": 3,
                "agent": "Code Generation Agent",
                "goal": "Generate FastAPI microservice skeletons"
            },
            {
                "step": 4,
                "agent": "Critic Agent",
                "goal": "Validate generated services and detect missing components"
            }
        ]
    }

    return plan


if __name__ == "__main__":

    sample_feature = """
    Vehicle diagnostics and OTA anomaly reporting
    """

    result = create_plan(sample_feature)

    print(json.dumps(result, indent=2))