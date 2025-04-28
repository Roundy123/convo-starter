# Conversation Starter

A web application that helps you find interesting conversation starters based on someone's LinkedIn profile.

## Features

- Enter a name to get conversation starters
- View a summary of the person's background
- Discover interesting facts about them
- Get their profile picture

## Local Development

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
5. Run the application:
   ```bash
   python app.py
   ```
6. Open http://localhost:5001 in your browser

## Deployment

This application is configured for deployment on Render.com:

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following environment variables:
   - `OPENAI_API_KEY`: Your OpenAI API key
4. Deploy!

## Technologies Used

- Python
- Flask
- LangChain
- OpenAI API
- LinkedIn API