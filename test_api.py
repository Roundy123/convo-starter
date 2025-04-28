from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize the client
client = OpenAI()

try:
    # Make a simple API call
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Say hello"}],
        max_tokens=5
    )
    print("API Key is valid!")
    print("Response:", response.choices[0].message.content)
except Exception as e:
    print("Error:", str(e)) 