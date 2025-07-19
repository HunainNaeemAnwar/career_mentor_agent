from agents import Agent

from instructions import get_career_instruction
from external_model import MODEL


# Function to create a CareerAgent with specific instructions
def career_agent() -> Agent:
    """An agent that suggests careers based on user interests."""
    agent = Agent(
        name="Career Suggestion Agent",
        instructions=get_career_instruction(),
        model=MODEL,
    )
    return agent
