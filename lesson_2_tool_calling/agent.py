from google.adk.agents.llm_agent import Agent

def get_weather(city: str) -> str:
    """
    This is a tool that can be called by the agent to get the weather information.
    For the sake of simplicity, we'll just return a static response.
    """
    return f"The weather in {city} is sunny"

# agent with a tool calling capability
root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant for user questions and weather information.',
    instruction='Answer user questions to the best of your knowledge and provide weather information for the given city.',
    tools=[get_weather],
)

# run "adk web" in terminal to see the agent in action