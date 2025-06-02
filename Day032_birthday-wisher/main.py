##################### Extra Hard Starting Project ######################
import random
import smtplib

import pandas
import datetime as dt

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.


BDAY_FILE = "birthdays.csv"
NAME_PLACEHOLDER = "[NAME]"
SMTP_SERVER = "" #Replace with your smtp server
EMAIL_FROM = "" ## "<your email address>"
EMAIL_PASS = "" #"<your app password>"
SUBJECT = "It's your birthday!"


def read_bday_file():
    #returns list of bday+person records

    df = pandas.read_csv(BDAY_FILE)
    now = dt.datetime.now()
    current_day = now.day # Get current day, month
    current_month = now.month

    # Get all records with current month and further filter by day's bday
    df = df[df.month == current_month]
    df = df[df.day == current_day]

     # Return as a list of dictionaries
    # ex: [{'name': 'Test002', 'email': 'me@gmail.com', 'year': 1961, 'month': 5, 'day': 16}]
    return df.to_dict(orient="records")



def get_email_message(name):
    # get random letter file then replace name
    letter_file_name = "./letter_templates/letter_" + str(random.randint(1, 4)) + ".txt"

    # open file:
    with open(letter_file_name) as letter_file:
        mail_content = letter_file.read()
        mail_content = mail_content.replace(NAME_PLACEHOLDER, name)

    return mail_content


def compose_email(email_addr, msg):
    with smtplib.SMTP(SMTP_SERVER) as conn:
        conn.starttls()
        conn.login(user=EMAIL_FROM, password=EMAIL_PASS)
        conn.sendmail(
            from_addr=EMAIL_FROM,
            to_addrs=email_addr,
            msg=f"Subject:{SUBJECT}\n\n{msg}"
        )


people_with_bdays = read_bday_file()
for bday in people_with_bdays:
    msg = get_email_message(bday["name"])
    compose_email(bday["email"], msg)