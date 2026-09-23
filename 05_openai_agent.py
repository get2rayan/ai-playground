import asyncio
import os
from agents import Agent, OpenAIChatCompletionsModel, Runner, trace
from openai import AsyncOpenAI
from dotenv import load_dotenv
load_dotenv()

# Judge LLM agent - GROQ
groq_client = AsyncOpenAI(
    base_url="https://api.groq.com/openai/v1",
    api_key=os.getenv('GROQ_API_KEY')
)
groq_model = OpenAIChatCompletionsModel(
    model="openai/gpt-oss-120b",
    openai_client=groq_client
)
judge_instructions="""You are an expert in judging the quality of an email. When given a set of emails, pick the best email."""
judge_agent = Agent(name="judge_agent",
                    model=groq_model,
                    instructions=judge_instructions,
                    )



base_instruction = "You are a helpful assistant who can write emails."
input = "Write an email about the AI's reach in the next decade"

agent1 = Agent(
    name='witty_agent',
    instructions=base_instruction + ' You are specialized in writing witty, humorous cold email.',
    model="gpt-5-nano"
)

agent2 = Agent(
    name='serious_agent',
    instructions=base_instruction + ' You are specialized in writing serious cold email.',
    model = "gpt-4o-mini"
)

async def get_agent_responses():
    with trace('Email Agent Handoff'):
        # Run both agents and collect their results
        # witty_result = await Runner.run(agent1, input=input)
        # serious_result = await Runner.run(agent2, input=input)
    
        witty_result, serious_result = await asyncio.gather(
            Runner.run(agent1, input=input),
            Runner.run(agent2, input=input)
        )
    # Now handoff both results to the judge agent
    # The judge agent needs to wait for both handoffs before making a decision
    judge_result = await Runner.run(
        judge_agent,
        input=f"Email 1: \n{witty_result.final_output}\n\nEmail 2: \n{serious_result.final_output}"
    )
    
    return witty_result, serious_result, judge_result


async def main():
    responses = await get_agent_responses()
    for i, result in enumerate(responses):
        print(f"Response {i+1} : {result.final_output}\n\n") 



if __name__ == "__main__":
    asyncio.run(main())