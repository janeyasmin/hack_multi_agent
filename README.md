# Hackathon Book Agent: ADK, MCP Toolbox for Databases and A2A

This sample uses the Agent Development Kit (ADK) to create a root (consuming) agent and a remote agent which communicate with each other via ADK and interact with a Cloud SQL PostgreSQL database via MCP Toolbox for Databases.

## Overview

The Book Search A2A sample consists of:

- **Root Agent** (`agent.py`): A root agent that uses a tool to search for a book's ISBN and then queries a remote library agent for book information.
- **Remote Library Agent** (`hack_library_agent/agent.py`): The remote agent that provides information about book location and number of copies, based on ISBN.

## Architecture

```
┌─────────────────┐    ┌────────────────────┐
│ Root Book Agent │───▶│ Remote A2A Library │
│                 │    │        Agent       │
| (localhost:8000)│    |   (GCR_URL:8001)   │
└─────────────────┘    └────────────────────┘
```

## Key Features

### 1. **A2A and MCP**

- The `hack_book_agent` connects to a remote A2A agent `hack_library_agent` for library queries.
- Both the `hack_book_agent` and hack_library_agent connect with a database using MCP Toolbox for Databases.
- Demonstrates distributed agent deployment using A2A architecture and MCP Toolbox for Databases.

### 2. **Uvicorn Server Deployment**

- The remote agent is served using uvicorn, a lightweight ASGI server.
- Shows how to expose A2A agents as standalone web services.

### 3. **Agent Functionality**

- **Book Search**: Looks up ISBN codes by book title using a tool.
- **Library Query**: Uses the ISBN to get location and copy count from the remote agent.

## Setup

Same as https://google.github.io/adk-docs/get-started/quickstart/#set-up-environment-install-adk :

#### Create & Activate Virtual Environment (Recommended):

python -m venv .venv

**Activate (each new terminal)**

- macOS/Linux: source .venv/bin/activate

- Windows CMD: .venv\Scripts\activate.bat

- Windows PowerShell: .venv\Scripts\Activate.ps1

**Install ADK and A2A**

pip install google-adk google-adk[a2a]

#### Setup gcloud environment

```
touch .env
```

1. Set up a Google Cloud project and enable the Vertex AI API.
2. Set up the gcloud CLI.
3. Authenticate to Google Cloud from the terminal by running gcloud auth application-default login.
4. When using Python, open the `.env` file located inside (`hack_book_agent/`). Copy-paste the following code and update the project ID and location.

```
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT=YOUR_PROJECT_ID
GOOGLE_CLOUD_LOCATION=LOCATION
```

## Run the Agent

Authenticate with Google Cloud. Ensure you have the Vertex AI user role required to use the LLMAgent.

```
gcloud auth application-default login
```

**Run the Main Agent in the root directory** (the remote agent is already running on Cloud Run):

```bash
# In a separate terminal, run the adk web server
adk web .
```

**Step 1**: Open the URL provided (usually http://localhost:8000 or http://127.0.0.1:8000) directly in your browser.

**Step 2**. In the top-left corner of the UI, you can select your agent in the dropdown. Select "hack_book_agent".

## Example Interactions

Once both services are running, you can interact with the root agent:

**Book Location:**

```
User: What is the ISBN code of Norwegian Wood
Bot: The ISBN code of Norwegian Wood is XXX-XXXXXXXXXX
```

**Number of Copies:**

```
User: How many copies of 'No Longer At Ease' are available?
Bot: There are X copies available.
```

---
