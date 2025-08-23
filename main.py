import schedule
import time
from news_scraper import scrape_all_news
from ai_summarizer import setup_openai, summarize_news
from email_sender import send_news_email
from config import OPENAI_API_KEY
import datetime

def daily_news_process():
    """Main function to run the daily news process"""
    print(f"Starting daily news process at {datetime.datetime.now()}")
    
    try:
        # Step 1: Scrape news
        print("Scraping news headlines...")
        headlines = scrape_all_news()
        
        if not headlines:
            print("No headlines found. Skipping today's summary.")
            return
        
        # Step 2: Generate AI summary
        print("Generating AI summary...")
        setup_openai()
        summary = summarize_news(headlines)
        
        # Step 3: Send email
        print("Sending email...")
        if send_news_email(summary):
            print("Daily news process completed successfully!")
        else:
            print("Failed to send email.")
            
    except Exception as e:
        print(f"Error in daily news process: {e}")

def run_once():
    """Run the news process once (for testing)"""
    daily_news_process()

def schedule_daily():
    """Schedule the news process to run daily at 8 AM"""
    schedule.every().day.at("08:00").do(daily_news_process)
    
    print("News summarizer scheduled to run daily at 8:00 AM")
    print("Press Ctrl+C to stop")
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    print("New York News Summarizer")
    print("=" * 30)
    
    if not OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your API keys")
        exit(1)
    
    print("Choose an option:")
    print("1. Run once (test)")
    print("2. Schedule daily at 8:00 AM")
    
    choice = input("Enter your choice (1 or 2): ").strip()
    
    if choice == "1":
        run_once()
    elif choice == "2":
        schedule_daily()
    else:
        print("Invalid choice. Running once as default.")
        run_once()
