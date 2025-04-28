"""
Agent logic for generating ice breaker questions using LinkedIn data.
"""

import os
import sys
from dotenv import load_dotenv
from langchain.tools import tool, Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

# Add the project root to the Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

# Now we can import from tools
from tools.tools import get_profile_url_tavily

# Load environment variables
load_dotenv()

@tool
def lookup(name: str) -> str:
    """
    Look up the LinkedIn profile URL for a given name using an LLM agent.
    The name parameter can include additional context like company and location.
    Args:
        name (str): The search string, which can include name, company, and location
                   (e.g., "John Doe at Google in London")
    Returns:
        str: The LinkedIn profile URL for the given name.
    """
    tools_for_agent = [
        Tool(
            name="crawl_google_and_linkedin_profile_page",
            func=get_profile_url_tavily,
            description="useful for when you need to find someone's LinkedIn profile URL. Input should be the person's full name, optionally followed by company and location."
        )
    ]
    
    llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0)
    react_prompt = hub.pull("hwchase17/react")
    
    agent = create_react_agent(
        llm=llm,
        tools=tools_for_agent,
        prompt=react_prompt,
    )
    
    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools_for_agent,
        verbose=True,
        max_iterations=5,  # Allow up to 5 iterations
        early_stopping_method="generate",  # Stop if agent determines it has the answer
        handle_parsing_errors=True  # Handle parsing errors gracefully
    )
    
    # Run the agent executor with the input name
    result = agent_executor.invoke(
        {
            "input": f"Find the LinkedIn profile URL for {name}. Return only the URL, no additional text or formatting."
        }
    )
    return result["output"]

if __name__ == "__main__":
    # Example usage
    name = "Adam Round at Google in London"
    url = lookup(name)
    print(f"LinkedIn profile URL for {name}: {url}") 