# New York News Summarizer

A simple Python project that scrapes news from New York sources and sends daily email summaries using AI.

## Features

- Scrapes headlines from multiple New York news sources
- Uses OpenAI API to generate intelligent summaries
- Sends daily email summaries automatically
- Simple and easy to understand code structure

## Setup

1. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a `.env` file with your API keys (copy from `env_example.txt`):
   - Get an OpenAI API key from https://platform.openai.com/
   - For Gmail, use an App Password (not your regular password)

3. Update the `.env` file with your actual API keys and email settings

## Usage

### Test Run
```
python main.py
```
Choose option 1 to test the system once.

### Schedule Daily
```
python main.py
```
Choose option 2 to schedule daily runs at 8:00 AM.

## How It Works

1. **News Scraping**: The program visits New York news websites and extracts headlines
2. **AI Summarization**: OpenAI processes the headlines to create a coherent summary
3. **Email Delivery**: The summary is sent via email to your specified address

## News Sources

- The New York Times
- New York Post
- AM New York
- Brooklyn Eagle

## Notes

- The program includes delays between requests to be respectful to news websites
- If the AI API fails, it falls back to a simple manual summary
- Make sure your computer stays on for scheduled daily runs
