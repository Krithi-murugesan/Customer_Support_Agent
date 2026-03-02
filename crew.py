from crewai import Crew
from agents import support_agent, support_qa_agent
from tasks import inquiry_resolution, quality_assurance_review

my_crew = Crew(
    agents=[support_agent, support_qa_agent],
    tasks=[inquiry_resolution, quality_assurance_review],
    verbose=True,
    memory=True
)
