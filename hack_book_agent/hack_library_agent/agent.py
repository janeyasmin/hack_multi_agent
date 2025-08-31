from google.adk.agents import Agent
from google.adk.a2a.utils.agent_to_a2a import to_a2a
from dotenv import load_dotenv
from toolbox_core import ToolboxSyncClient

load_dotenv()

toolbox = ToolboxSyncClient("https://toolbox-cloudrun-848568081556.us-central1.run.app")

search_number_of_copies_by_isbn = toolbox.load_tool("search-number-of-copies")
search_book_location = toolbox.load_tool("search-book-location")

root_agent = Agent(
    name="book_search_agent",
    model="gemini-2.5-flash",
    description="An agent that finds the location of a book in the library and "
    "the number of copies of the book using its ISBN code as input.",
    tools=[search_book_location, search_number_of_copies_by_isbn],
)

a2a_app = to_a2a(
    root_agent,
    host="library-a2a-agent-848568081556.us-central1.run.app",
    port=443,
    protocol="https",
)
