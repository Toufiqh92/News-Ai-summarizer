'''
this file contains configuration settings for the News AI Summarizer application.
    It loads environment variables from a .env file using the python-dotenv library.
    It defines constants for the OpenAI API key, email settings, and news sources.
'''

import os
from dotenv import load_dotenv
load_dotenv()
# API Keys
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Email Settings
EMAIL_SENDER = os.getenv('EMAIL_SENDER')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
EMAIL_RECEIVER = os.getenv('EMAIL_RECEIVER')
# News Sources - you can add more sources here
NEWS_SOURCES = [
    'https://www.nytimes.com',
    'https://nypost.com',
    'https://www.amny.com',
    'https://brooklyneagle.com'
]
