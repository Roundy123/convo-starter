"""
Custom tools for the tools package.
"""

from langchain_community.tools.tavily_search import TavilySearchResults
import os
from dotenv import load_dotenv

load_dotenv()

def get_profile_url_tavily(name: str) -> str:
    """
    Use Tavily to search for the LinkedIn profile URL for the given name.
    Args:
        name (str): The full name of the person to look up.
    Returns:
        str: The LinkedIn profile URL for the given name, or a LinkedIn search URL if not found.
    """
    tavily = TavilySearchResults()
    query = f"{name} LinkedIn"
    results = tavily.run(query)
    # Try to find a LinkedIn URL in the results
    for result in results:
        url = result.get("url", "")
        if "linkedin.com/in/" in url:
            return url
    # Fallback: return a LinkedIn search URL
    return f"https://www.linkedin.com/search/results/all/?keywords={name.replace(' ', '%20')}"

# Add your custom tool implementations here. 