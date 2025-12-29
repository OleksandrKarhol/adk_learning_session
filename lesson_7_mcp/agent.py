import sys
import os
import numpy as np
import warnings
warnings.filterwarnings("ignore")

from google.adk.agents.llm_agent import LlmAgent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams           


root_agent = LlmAgent(
    name='root_agent',
    model='gemini-2.5-flash',
    instruction='You are a helpful assistant that helps to query the Big Query database. You are used by the product analytics team to query the database and provide the data they need. Use the MCP to perform queries.',
    tools=[
        McpToolset(
            connection_params=SseConnectionParams(
                url="http://127.0.0.1:5000/mcp/sse"
            ),
        )
    ]
)