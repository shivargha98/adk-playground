from google.adk.agents import Agent

## root agent is required, acts as the entry point ##
root_agent = Agent(
    name = 'BasicAgent',
    model='gemini-2.5-flash',
    description='Greeting Agent',
    instruction='''
    You are a helpful assistant that greets the user.
    Ask the user's name, use that name to greet the user.
    '''
)