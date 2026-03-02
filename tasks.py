from crewai import Task
from agents import support_agent, support_qa_agent
from tools import docs_scrape_tool

inquiry_resolution = Task(
    description="{customer} has an inquiry: {inquiry}. {person} is the contact.",
    expected_output="A detailed response with references.",
    tools=[docs_scrape_tool],
    agent=support_agent,
    output_file="draft_inquiry_result.md"
)

quality_assurance_review = Task(
    description="Review the draft and ensure high quality.",
    expected_output="A final, detailed, and informative response.",
    agent=support_qa_agent,
    output_file="final_support_response.md"
)
