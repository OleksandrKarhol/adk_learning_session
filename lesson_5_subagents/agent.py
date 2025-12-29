from google.adk.agents.llm_agent import Agent
import asyncio
import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import Agent
from google.adk.sessions import InMemorySessionService
from google.adk.runners import Runner
from google.genai import types
import warnings
warnings.filterwarnings("ignore")
import logging
logging.basicConfig(level=logging.ERROR)


def get_weather(city: str) -> dict:

    return f'The weather in {city} is sunny'


def get_current_time(city: str) -> dict:

    return f'The current time in {city} is {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S %Z%z")}'

# Agent with Sub agents
weather_agent = Agent(
    name="weather_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the weather in a city."),
    instruction=("You are a helpful agent who can answer user questions about the weather in a city."),
    tools=[get_weather],
)

time_agent = Agent(
    name="time_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the time in a city."),
    instruction=("You are a helpful agent who can answer user questions about the time in a city."),
    tools=[get_current_time],
)

root_agent = Agent(
    name="weather_time_agent",
    model="gemini-2.0-flash",
    description=("Agent to answer questions about the time and weather in a city."),
    instruction=("You are a helpful agent who can answer user questions about the time and weather in a city."),
    sub_agents=[weather_agent, time_agent], 
)