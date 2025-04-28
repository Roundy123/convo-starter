"""
LinkedIn API integration utilities.
"""
from typing import Dict, Optional
import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool = False) -> Dict:
    """
    Scrape information from LinkedIn profile using Scrapin.io API.
    
    Args:
        linkedin_profile_url: URL of the LinkedIn profile to scrape
        mock: Whether to use mock data (deprecated, kept for backwards compatibility)
        
    Returns:
        Dict containing profile information
    """
    api_endpoint = "https://api.scrapin.io/enrichment/profile"
    params = {
        "apikey": os.getenv("SCRAPIN_API_KEY"),
        "linkedinUrl": linkedin_profile_url
    }
    response = requests.get(api_endpoint, params=params, timeout=10)
    
    data = response.json()
    print(f"Scrapin.io response: {data}")  # Debug log
    
    # Clean up empty fields
    if "person" in data:
        person = data["person"]
        for key in list(person.keys()):
            if not person[key]:
                del person[key]
        print(f"Profile picture URL: {person.get('profile_pic_url')}")  # Debug log
    
    return data

if __name__ == "__main__":
    # Example usage
    linkedin_profile_url = "https://www.linkedin.com/in/adam-round-1665367a/"
    data = scrape_linkedin_profile(linkedin_profile_url, mock=False)
    print(data)

class LinkedInAPI:
    """Wrapper for LinkedIn API interactions."""
    
    def __init__(self):
        """Initialize LinkedIn API client with credentials."""
        self.api_key = os.getenv("LINKEDIN_API_KEY")
        self.api_secret = os.getenv("LINKEDIN_API_SECRET")
        self.access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
        
    def get_profile(self, profile_id: str) -> Optional[Dict]:
        """
        Get LinkedIn profile information.
        
        Args:
            profile_id: LinkedIn profile ID or URL
            
        Returns:
            Dict containing profile information or None if not found
        """
        # TODO: Implement LinkedIn API call
        pass
    
    def search_profiles(self, query: str) -> Optional[Dict]:
        """
        Search LinkedIn profiles.
        
        Args:
            query: Search query string
            
        Returns:
            Dict containing search results or None if error
        """
        # TODO: Implement LinkedIn API call
        pass 