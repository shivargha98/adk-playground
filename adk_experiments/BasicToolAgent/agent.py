from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from google.adk.tools import google_search

from time import time
from datetime import datetime

### Custom tool ###
def get_current_time() -> dict:
    '''    
    Function that returns the current time in the format YYYY-MM-DD HH:MM:SS
    :return: Current time
    :rtype: dict
    '''
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

### Search agent -> Agent as a tool ###
search_agent = Agent(
    name='SearchAgent',
    model='gemini-2.5-flash',
    description= 'Agent for Google Search',
    instruction='You are an assistant, which searches the web.\
                    Use this tool - Google Search',
    tools=[google_search]
)

root_agent = Agent(
    name='BasicToolAgent',
    model='gemini-2.5-flash',
    description= 'Agent with Tools',
    instruction='You are an assistant, which searches the web or gets the current time.\
                    Use these tools - 1.SearchAgent  2.get_current_time',

    tools=[get_current_time, AgentTool(agent=search_agent)] ## Using Custom tools with Built in tools ##
)




