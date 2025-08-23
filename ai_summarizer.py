import openai
from config import OPENAI_API_KEY

def setup_openai():
    """Setup OpenAI client"""
    openai.api_key = OPENAI_API_KEY

def summarize_news(headlines):
    """Use OpenAI to summarize the news headlines"""
    if not headlines:
        return "No news headlines found to summarize."
    
    try:
        # Create a simple prompt
        prompt = f"""
        Here are today's top New York news headlines. Please provide a brief, professional summary of the main stories:
        
        {chr(10).join([f"- {headline}" for headline in headlines])}
        
        Summary:
        """
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful news summarizer. Provide concise, professional summaries of news headlines."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7
        )
        
        summary = response.choices[0].message.content.strip()
        return summary
        
    except Exception as e:
        print(f"Error getting AI summary: {e}")
        # Fallback to manual summary
        return create_manual_summary(headlines)

def create_manual_summary(headlines):
    """Create a simple manual summary if AI fails"""
    if not headlines:
        return "No news headlines available."
    
    summary = "Today's Top New York News:\n\n"
    for i, headline in enumerate(headlines[:10], 1):
        summary += f"{i}. {headline}\n"
    
    summary += f"\nTotal stories: {len(headlines)}"
    return summary

if __name__ == "__main__":
    # Test with sample headlines
    test_headlines = [
        "New York City Announces New Transportation Plan",
        "Local Business Owners React to Economic Changes",
        "Weather Alert: Storm Expected This Weekend"
    ]
    
    setup_openai()
    summary = summarize_news(test_headlines)
    print(summary)
