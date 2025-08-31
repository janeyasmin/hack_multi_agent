from toolbox_core import ToolboxSyncClient
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent
from google.adk.agents.remote_a2a_agent import AGENT_CARD_WELL_KNOWN_PATH
from google.adk.agents import Agent
import httpx

toolbox = ToolboxSyncClient("https://toolbox-cloudrun-848568081556.us-central1.run.app")

# Load tool
search_isbn_tool = (toolbox.load_tool("search-isbn-code-by-book-title"),)

library_agent = RemoteA2aAgent(
    name="library_agent",
    agent_card=(
        f"https://library-a2a-agent-848568081556.us-central1.run.app"
        f"{AGENT_CARD_WELL_KNOWN_PATH}"
    ),
    httpx_client=httpx.AsyncClient(timeout=120.0),
)

root_agent = Agent(
    name="book_search_agent",
    model="gemini-2.5-flash",
    instruction=(
        """
        You are a helpful assistant that can answer questions about books.

        Workflow
        * First, greet the user and tell them what you can do.
        * If a user asks about a book's location or number of copies,
        ALWAYS first use search_isbn_tool to get the ISBN code of the book.
        * Then, use that ISBN code to call the library_agent to get either the
        book's location or the number of copies available.
        """
    ),
    tools=search_isbn_tool,
    sub_agents=[library_agent],
)
