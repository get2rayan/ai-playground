import asyncio
from agents import Agent, Runner
from dotenv import load_dotenv
load_dotenv()

base_instruction = "You are a helpful assistant who can write emails."
input = "Write an email about the AI's reach in the next decade"

agent1 = Agent(
    name='witty_agent',
    instructions=base_instruction + ' You are specialized in writing witty humorous emails.',
    model="gpt-5-nano"
)

agent2 = Agent(
    name='serious_agent',
    instructions=base_instruction + ' You are specialized in writing serious emails.',
    model = "gpt-4.1-mini"
)

async def get_responses():
    return await asyncio.gather(
        Runner.run(agent1, input=input),
        Runner.run(agent2, input=input)
    )


async def main():
    responses = await get_responses()
    print (f"Agent responses: \n",  {result.final_output for result in responses})


if __name__ == "__main__":
    asyncio.run(main())