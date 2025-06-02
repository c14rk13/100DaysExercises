import configparser
import smtplib

CONFIG_FILE = "config.ini"

def read_config():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILE)

    config_values = {
        'smtp': config.get("Email", "smtp"),
        'from': config.get("Email", "from"),
        'password': config.get("Email", "passw"),
        'to': config.get("Email", "to")
    }
    return config_values


def email_me(msg):
    config_data = read_config()
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