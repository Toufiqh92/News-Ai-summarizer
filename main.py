import schedule # Importing the schedule library to schedule tasks
import time # Importing the time library to add delays
from news_scraper import scrape_all_news # Importing the scrape_all_news function from news_scraper.py file
from ai_summarizer import setup_openai, summarize_news  # Importing the setup_openai and summarize_news functions from ai_summarizer.py file
from email_sender import send_news_email
from config import OPENAI_API_KEY 
import datetime

def daily_news_process():
    """Main function to run the daily news process""" 
    print(f"Starting daily news process at {datetime.datetime.now()}")
    
    try:
        # Step 1: Scrape news
        print("Scraping news headlines...")
        headlines = scrape_all_news() # Call the function to scrape news headlines from news_scraper.py file
        # Check if headlines were found if not, skip the rest of the process
        if not headlines:
            print("No headlines found. Skipping today's summary.")
            return
        
        # Step 2: Generate AI summary
        print("Generating AI summary...")
        setup_openai() # calling the setup_openai function to set the API key
        summary = summarize_news(headlines) # Call the function to summarize news headlines from ai_summarizer.py file
        
        # Step 3: Send email
        print("Sending email...") #
        if send_news_email(summary): # Call the function to send email from email_sender.py file
            print("Daily news process completed successfully!")
        else:
            print("Failed to send email.")
 # erorr handling if email fails to send
    except Exception as e:
        print(f"Error in daily news process: {e}")

def run_once():
    """Run the news process once (for testing)"""
    daily_news_process()

#   Schedule the news process to run daily at 8 AM
def schedule_daily():
    """Schedule the news process to run daily at 8 AM"""
    schedule.every().day.at("08:00").do(daily_news_process) # Schedule the job at 8:00 AM every day
    print("News summarizer scheduled to run daily at 8:00 AM") # Inform the user
    print("Press Ctrl+C to stop") # Inform the user how to stop the program 
    
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every minute
# Entry point
if __name__ == "__main__":
    print("New York News Summarizer")
    print("=" * 30)
    # Ensure the API key is set 
    # prompt user if there is no API key

    if not OPENAI_API_KEY:
        print("Error: OPENAI_API_KEY not found in environment variables")
        print("Please create a .env file with your API keys")
        exit(1) 
    # User menu
    
    print("Choose an option:")
    print("1. Run once (test)")
    print("2. Schedule daily at 8:00 AM")
    
    choice = input("Enter your choice (1 or 2): ").strip() # .strip() is a function to remove any extra spaces so the user input is clean
    
    if choice == "1":
        run_once()
    elif choice == "2":
        schedule_daily()
    else:
        print("Invalid choice. Running once as default.") # if a user enters invalid input  
        run_once()
