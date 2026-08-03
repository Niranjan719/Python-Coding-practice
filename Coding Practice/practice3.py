from dotenv import load_dotenv # type: ignore
from langchain.tools import tool # type: ignore
from langchain_openai import ChatOpenAI # type: ignore
from langgraph.prebuilt import create_react_agent # type: ignore
from langchain.agents import create_agent



load_dotenv()

# tools

@tool
def search_internal_wiki(query: str) -> str:
    """Searches the internal wiki."""
    return f"Results from internal wiki for '{query}'"

@tool
def get_ticket_status(ticket_id: str) -> str:
    """Returns the status of a ticket."""
    return f"Ticket {ticket_id} is Open"

tools = [search_internal_wiki, get_ticket_status]

llm = ChatOpenAI(model="gpt-4.1", temperature=0)

agent = create_react_agent(model=llm, tools=tools, prompt="You are a helpful IT assistant.")

response = agent.invoke(
    {
        "messages":[
            {
                "role" : "user",
                "content": "What is the status of ticket 12345?"
            }
        ]
    }
)

print(response["messages"][-1].content)