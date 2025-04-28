from typing import Tuple
from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import lookup as linkedin_lookup_agent
from output_parsers import summary_parser
import re

def clean_linkedin_url(url: str) -> str:
    """
    Clean up the LinkedIn URL to ensure it's in the correct format.
    """
    # Extract the URL from markdown format if present
    url_match = re.search(r'\[(.*?)\]\((.*?)\)', url)
    if url_match:
        url = url_match.group(2)
    
    # Remove any trailing characters or spaces
    url = url.strip()
    
    # Ensure it starts with https://
    if not url.startswith('https://'):
        url = 'https://' + url
        
    return url

def ice_break_with(name: str) -> tuple:
    """
    Generate a summary and interesting facts about a person based on their LinkedIn profile.
    
    Args:
        name: The name of the person to look up
        
    Returns:
        tuple: (summary object, profile picture URL)
    """
    linkedin_username = linkedin_lookup_agent(name)
    # Clean up the LinkedIn URL
    linkedin_username = clean_linkedin_url(linkedin_username)
    linkedin_data = scrape_linkedin_profile(linkedin_profile_url=linkedin_username)
    
    summary_template = """
    given the Linkedin information {information} about a person I want you to create:
    
    1. A short summary
    
    2. two interesting facts about them

    Use information from Linkedin
    \n{format_instructions}
    """
    
    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template,
        partial_variables={
            "format_instructions": summary_parser.get_format_instructions()
        },
    )
    
    llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")
    chain = summary_prompt_template | llm | summary_parser
    summary = chain.invoke(input={"information": linkedin_data})
    
    # Extract profile picture URL from LinkedIn data
    profile_pic_url = linkedin_data.get("person", {}).get("photoUrl")
    if not profile_pic_url:
        # Use a default profile picture if none is available
        profile_pic_url = "https://picsum.photos/200"
    
    return summary, profile_pic_url

if __name__ == "__main__":
    load_dotenv()
    print("Ice Breaker Enter")
    summary, profile_pic_url = ice_break_with(name="Adam Round")
    print(f"Summary: {summary.summary}")
    print("Interesting Facts:")
    for fact in summary.interesting_facts:
        print(f"- {fact}")
    print(f"Profile Picture URL: {profile_pic_url}")

