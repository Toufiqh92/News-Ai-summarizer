import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER
import datetime

def send_news_email(summary):
    try:
        # Create message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_SENDER
        msg['To'] = EMAIL_RECEIVER
        msg['Subject'] = f"Daily New York News Summary - {datetime.datetime.now().strftime('%B %d, %Y')}"
        
        # Create email body
        body = f"""
        Good morning!
        
        Here's your daily New York news summary:
        
        {summary}
        
        This summary was generated automatically from local New York news sources.
        
        Best regards,
        Your News Summarizer
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        
        text = msg.as_string()
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, text)
        server.quit()
        
        print("News summary email sent successfully!")
        return True
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return False

def test_email():
    """Test email functionality"""
    test_summary = "This is a test summary to check if email sending works."
    return send_news_email(test_summary)

if __name__ == "__main__":
    test_email()
