from agents import Agent

from instructions import get_job_instruction
from external_model import MODEL


# Function to create a JobAgent with specific instructions
def job_agent() -> Agent:
    """An agent that provides job-related information for a specific career."""
    agent = Agent(
        name="Job Information Agent", instructions=get_job_instruction(), model=MODEL
    )
    return agent
