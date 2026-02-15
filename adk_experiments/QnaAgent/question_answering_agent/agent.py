from google.adk.agents import Agent

### Root Agent ###
question_answering_agent = Agent(
    name="question_answering_agent",
    model = "gemini-2.5-flash",
    description="An agent that answers questions based on the provided context.",
    instruction=
    """
    You are a helpful assistant that answers questions based on the user's preferences.
    Here is the context you can use to answer the question:
    Name:
    {user_name}
    Preferences:
    {user_preferences}
    """
)