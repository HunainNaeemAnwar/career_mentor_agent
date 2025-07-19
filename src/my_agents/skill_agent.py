from agents import Agent

from instructions import get_skill_instruction
from external_model import MODEL


# Function to create a SkillAgent with specific instructions
def skill_agent() -> Agent:
    """An agent that provides skill-building roadmaps for a specific career."""
    agent = Agent(name="Skill Building Agent", instructions=get_skill_instruction())
    return agent
