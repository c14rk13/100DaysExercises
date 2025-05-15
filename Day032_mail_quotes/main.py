import datetime as dt
import random
import smtplib

DAY_OF_WEEK_TO_SEND = 4 #Monday
QUOTES_FILE = "quotes.txt"
SMTP_SERVER = "smtp.gmail.com" #Replace with your smtp server
EMAIL_FROM = "<your email address>"
EMAIL_PASS = "<your app password>"
EMAIL_TO = "<email/s to send to>"
SUBJECT = "Your Monday quote"

def get_a_quote():
    with open(QUOTES_FILE) as quotes_file:
        all_quotes = quotes_file.readlines()

    chosen_quote = random.choice(all_quotes)
    chosen_quote = str(chosen_quote)
    # chosen_quote.replace("\"", "")

    return chosen_quote

def send_email_quote():
    quote_to_send = get_a_quote()
    with smtplib.SMTP(SMTP_SERVER) as conn:
        conn.starttls()
        conn.login(user=EMAIL_FROM, password=EMAIL_PASS)

        conn.sendmail(
            from_addr=EMAIL_FROM,
            to_addrs=EMAIL_TO,
            msg=f"Subject:{SUBJECT}\n\n{quote_to_send}"
        )


now = dt.datetime.now()
current_day_of_week = now.weekday()

if current_day_of_week == DAY_OF_WEEK_TO_SEND:
    #send an email containing quote
    send_email_quote()
    pass
