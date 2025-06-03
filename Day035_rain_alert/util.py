import configparser
import smtplib

CONFIG_FILE = "config.ini"
EMAIL_SECTION = "Email"
WEATHER_SECTION = "Weather"
TWILIO_SECTION = "Twilio"

def read_config(section):
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    config_values = {}

    if section == EMAIL_SECTION:
        config_values = {
            'smtp': config.get(section=EMAIL_SECTION, option="smtp"),
            'from': config.get(section=EMAIL_SECTION, option="from"),
            'password': config.get(section=EMAIL_SECTION, option="passw"),
            'to': config.get(section=EMAIL_SECTION, option="to")
        }
    elif section == WEATHER_SECTION:
        config_values ={
            'api_key': config.get(section=WEATHER_SECTION, option="api_key")
        }
    elif section == TWILIO_SECTION:
        config_values ={
            'account_sid': config.get(section=TWILIO_SECTION, option="account_sid"),
            'auth_token': config.get(section=TWILIO_SECTION, option="auth_token"),
            'from': config.get(section=TWILIO_SECTION, option="from"),
            'whatsapp_from': config.get(section=TWILIO_SECTION, option="whatsapp_from"),
            'whatsapp_to': config.get(section=TWILIO_SECTION, option="whatsapp_to"),
        }

    return config_values


def email_me(msg):
    config_data = read_config(EMAIL_SECTION)
    my_email = config_data["from"]
    password = config_data["password"] # App password
    to_address = config_data["to"]
    smtp_server = config_data["smtp"]


    with smtplib.SMTP(smtp_server) as connection: # using "with" closes the connection automatically after
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to_address,
            msg=msg
        )