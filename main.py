import os
from crew import my_crew

os.environ["OPENAI_API_KEY"] = "***"
os.environ["OPENAI_MODEL_NAME"] = 'gpt-4o'

def run():
    inputs = {
        "customer": "DeepLearningAI",
        "person": "Andrew Ng",
        "inquiry": "I need help with setting up a Crew and kicking it off, specifically how can I add memory to my crew?"
    }
    result = my_crew.kickoff(inputs=inputs)
    print("\n✅ Support process complete.")

if __name__ == "__main__":
    run()
