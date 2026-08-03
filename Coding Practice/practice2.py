# Using LangChain (or pseudocode close to it), write a minimal agent that has 
# two tools - 'search_internal_wiki' and 'get_ticket_status' - and can decide 
# which to call based on the user's question.

# pip install python-dotenv langchain langchain-openai

from dotenv import load_dotenv # type: ignore

from langchain.tools import tool # type: ignore
from langchain.agents import create_agent # type: ignore
from langchain_openai import ChatOpenAI # type: ignore

load_dotenv()


@tool
def search_internal_wiki(query: str) -> str:
    """Searches the internal wiki."""
    return f"Results from internal wiki for '{query}'"


@tool
def get_ticket_status(ticket_id: str) -> str:
    """Returns the status of a ticket."""
    return f"Ticket {ticket_id} is Open"


tools = [search_internal_wiki, get_ticket_status]


llm = ChatOpenAI(
    model="gpt-4.1",
    temperature=0
)


agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt="You are a helpful IT assistant."
)


response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the status of ticket 12345?"
            }
        ]
    }
)

# print(response)
print(response["messages"][-1].content)