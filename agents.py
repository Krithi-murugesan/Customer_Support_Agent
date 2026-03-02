from crewai import Agent

support_agent = Agent(
    role="Senior Support Representative",
    goal="Be the most friendly and helpful support representative.",
    backstory="You work at crewAI. Provide complete answers with no assumptions.",
    allow_delegation=False,
    verbose=True
)

support_qa_agent = Agent(
    role="Support Quality Assurance Specialist",
    goal="Ensure the highest quality support standards.",
    backstory="You ensure every response is accurate and friendly.",
    verbose=True
)
