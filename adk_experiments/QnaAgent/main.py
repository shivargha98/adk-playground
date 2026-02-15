import uuid
from dotenv import load_dotenv
from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from question_answering_agent import question_answering_agent
from google.genai import types
import asyncio
load_dotenv()

session_service = InMemorySessionService() ## Session state to store conversation history and other relevant information
## Inital Session State ###
initial_session_state = {
    "user_name":"Jeet",
    "user_preferences":"""

    1. I like to play & watch cricket.
    2. I love learning about AI and its applications.
    3. I enjoy traveling and exploring new cultures.
    4. I am a foodie and love trying out new cuisines.
    5. I am interested in technology and gadgets.
    """

}
### Create the session for the agent ###
## Session -> stores initial state, conversation history etc. 

APP_name = "QnaAgent"
USER_ID = "Jeet_98"
SESSION_ID = str(uuid.uuid4()) ## Unique session ID for each conversation
async def main():
    stateful_session = await session_service.create_session(
        app_name = APP_name,
        session_id = SESSION_ID,
        user_id = USER_ID,
        state = initial_session_state
    )

    print(f"Session created with ID: {SESSION_ID}")
    ### Create the runner for the agent -- Runner contains the ageent, the session and other relevant information to run the agent.###
    runner = Runner(
        agent=question_answering_agent,
        app_name=APP_name,
        session_service=session_service
    )
    ## genai - sdk Content for creating a message for the agent ###
    message = types.Content(
        role= "user", parts=[types.Part(text="What is Jeet's favorite sport?")]
    )

    async for event in runner.run_async(
        user_id=USER_ID,
        session_id=SESSION_ID,
        new_message=message
    ):
        #print(event)
        if event.is_final_response():
            if event.content and event.content.parts:
                print("Agent's final response:", event.content.parts[0].text)


    print("Session State after conversation:")
    session_state_now = await session_service.get_session(app_name=APP_name,
                                                user_id = USER_ID,
                                                session_id=SESSION_ID)

    print(session_state_now.state.items())

asyncio.run(main())