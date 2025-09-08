import openai
from config import OPENAI_API_KEY

'''
 most of the code here is for summarizing news using OpenAI's GPT model and handling errors. 
 The summarization function formats the headlines and sends them to the AI for a concise summary. 
 It also uses code proveded by open ai's documentation and examples to ensure best practices are followed.
'''
# this function sets up the OpenAI API key. This is called in main.py before any AI requests are made.

def setup_openai():
    openai.api_key = OPENAI_API_KEY
# this function summarizes the news headlines using OpenAI's GPT model.
def summarize_news(headlines):
    if not headlines:  # safety check
        return "No news headlines found to summarize."
    try:
        # Format titles + links
        formatted_headlines = [
            f"- {h['title']} ({h['url']})" if h.get("url") else f"- {h['title']}"
            for h in headlines
        ]
        prompt = f"""
        Here are today's top New York news headlines. Please provide a brief, professional summary of the main stories:
        {chr(10).join(formatted_headlines)}
        
        Summary:
        """
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[ 
                {
                    "role": "system",
                    "content": (
                        "For each article, you are given a headline and a link. "
                        "Summarize each article in 1-2 sentences. "
                        "At the end of each summary, include the article's link in parentheses. "
                    )
                },
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e: # these are error handling. If the AI fails, we fall back to manual summary
        print(f"Error getting AI summary: {e}")
        return create_manual_summary(headlines)

def create_manual_summary(headlines): 
    if not headlines:
        return "No news headlines available."
    # simple manual summary
    summary = "Today's Top New York News:\n\n"

#this algorithm lists the top 10 headlines with their links if available. This is an alogrithm created to fall back on if the AI fails.
# Loops through the first 10 headline

    for i, h in enumerate(headlines[:10], 1): # makes numbering start at 1 instead of 0.
        if isinstance(h, dict): 
            title = h.get("title", "No title") # safety check
            url = f" ({h['url']})" if h.get("url") else "" # safety check
            summary += f"{i}. {title}{url}\n"
        else: # in case the headline is just a string
            summary += f"{i}. {h}\n" # safety check
    summary += f"\nTotal stories: {len(headlines)}" # count of stories
    return summary 
if __name__ == "__main__": # this is for testing purposes only
    # Example headlines for testing
    test_headlines = [
        {"title": "New York City Announces New Transportation Plan", "url": "https://example.com/transport"},
        {"title": "Local Business Owners React to Economic Changes", "url": "https://example.com/business"},
        {"title": "Weather Alert: Storm Expected This Weekend", "url": "https://example.com/weather"},
    ]
    setup_openai()
    summary = summarize_news(test_headlines)
    print(summary)