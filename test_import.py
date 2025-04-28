import sys
import os

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

# Try to import the function
from tools.tools import get_profile_url_tavily

# Test the function
url = get_profile_url_tavily("John Doe")
print(f"Test URL: {url}") 