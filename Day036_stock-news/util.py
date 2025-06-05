import configparser
import smtplib
import  yaml

CONFIG_FILE = "config.yaml"
EMAIL_SECTION = "EMAIL"
TWILIO_SECTION = "TWILIO"
API_SECTION = "API"

def read_config():
    with open(CONFIG_FILE) as file:
        config = yaml.safe_load(file)

    config_values = {}

    config_values = {
            'smtp': config[EMAIL_SECTION]["smtp"],
            'email_from': config[EMAIL_SECTION]["from"],
            'password': config[EMAIL_SECTION]["passw"],
            'email_to': config[EMAIL_SECTION]["to"],
            'auth_token': config[TWILIO_SECTION]["auth_token"],
            'twilio_from': config[TWILIO_SECTION]["from"],
            'whatsapp_from': config[TWILIO_SECTION]["whatsapp_from"],
            'whatsapp_to': config[TWILIO_SECTION]["whatsapp_to"],
            'stock_api_key': config[API_SECTION]["stock_api_key"],
            'news_api_key': config[API_SECTION]["news_api_key"],
        }

    return config_values


def email_me_messages(messages, config_data):
    my_email = config_data["email_from"]
    password = config_data["password"] # App password
    to_address = config_data["email_to"]
    smtp_server = config_data["smtp"]


    with smtplib.SMTP(smtp_server) as connection: # using "with" closes the connection automatically after
        connection.starttls()
        connection.login(user=my_email, password=password)
        for msg in messages:
            connection.sendmail(
                from_addr=my_email,
                to_addrs=to_address,
                msg=msg
            )