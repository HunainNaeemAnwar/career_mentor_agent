from agents import Agent,function_tool

from instructions import get_tool_instruction
from external_model import MODEL


from agents import Agent, Runner, function_tool
from instructions import get_tool_instruction
from external_model import MODEL


@function_tool
async def get_career_roadmap(career: str) -> str:
    agent = Agent(
        name="career_roadmap_agent",
        instructions=get_tool_instruction(),
        model=MODEL,
    )

    print(f"Generating career roadmap for {career}...")

    # ❌ Wrong: response = await agent.run(career=career)
    # ✅ Correct:
    response = await Runner.run(agent, input=career)

    roadmap = response.final_output.strip()
    print("Generated roadmap:", roadmap)

    return roadmap
