# prompt: email automation with fun facts

# Import necessary libraries
import smtplib
import datetime
import requests
import schedule
import time

# Replace these values with your own
SENDER_EMAIL = "your_sender_email"
SENDER_PASSWORD = "your_sender_password"
RECEIVER_EMAIL = "your_receiver_email"

# Function to send a fun fact email
def send_fun_fact():
    # Get the current date
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")

    # Get a random fact from the Fun Fact API
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    fun_fact = response.json()["text"]

    # Create the email message
    message = f"Subject: Fun Fact for {current_date}\n\n{fun_fact}"

    # Send the email
    with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
        smtp.starttls()
        smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
        smtp.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message)

# Schedule the email to be sent every day at 9am
schedule.every().day.at("09:00").do(send_fun_fact)

# Keep the program running until interrupted
while True:
    schedule.run_pending()
    time.sleep(1)