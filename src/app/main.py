import asyncio

from agents import Agent, Runner,SQLiteSession

from instructions import get_orchestrator_instruction
from tools import get_career_roadmap
from external_model import MODEL
from my_agents import career_agent, skill_agent, job_agent


def orchestrator_agent() -> Agent:
    """
    This function creates an orchestrator agent that manages the workflow of other agents.
    It can be used to coordinate tasks, manage dependencies, and ensure that the overall
    process runs smoothly.
    """
    # Create an instance of the Agent class for the orchestrator

    agent = Agent(
        name="orchestrator_agent",
        instructions=get_orchestrator_instruction(),
        tools=[get_career_roadmap],
        handoffs=[
            career_agent(),
            skill_agent(),
            job_agent(),
        ],
        model=MODEL,
    )

    return agent

    # Start the agent runner


async def main():
    agent = orchestrator_agent()
    session = SQLiteSession("user_hunain", "conversation.db")

    print("Ask anything:")
    while True:
        query = input("You: ")
        if query.lower() in ["exit", "quit"]: break

        result = await Runner.run(
            agent,
            input=query,
            session=session
        )

        print(f"Mentor: {result.final_output}\n")

if __name__ == "__main__":
    asyncio.run(main())