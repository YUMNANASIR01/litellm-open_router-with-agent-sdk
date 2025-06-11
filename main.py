
import os
from dotenv import load_dotenv
from agents import Agent, Runner, set_tracing_disabled 
from agents.extensions.models.litellm_model import LitellmModel 
import litellm

litellm.disable_aiohttp_transport = True

load_dotenv()
set_tracing_disabled(disabled=True)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini/gemini-1.5-flash"

agent = Agent(
    name="my_agent",
    instructions="You are a helpful assistant",
    model=LitellmModel(model=MODEL, api_key=GEMINI_API_KEY),
)
res = Runner.run_sync(agent, "I am Yumna, Who are You?")
print(res.final_output)