
import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

load_dotenv()

set_tracing_disabled(disabled=True)

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

if not OPENROUTER_API_KEY:
    raise Exception("OPENROUTER_API_KEY is not set")

#-------------------------Ye Provider hai-----------------------------------------
client=AsyncOpenAI(
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
)

agent = Agent(
    model = OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free", openai_client=client),
    name = "Bisma_Agent",
    instructions="You are a helpful assistant",
)


#------------------------------------------------------------------

res = Runner.run_sync(agent, "I am Yumna, Who are You?")

print(res.final_output)