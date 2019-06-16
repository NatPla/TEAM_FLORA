import requests
from dotenv import dotenv_values
mail_configuration = dotenv_values()

def send_message(email, message):
  mail_api_key= mail_configuration["MAILGUN_API_KEY"]
  mail_domain = mail_configuration["MAILGUN_DOMAIN"]
  sender = "Excited User <mailgun@{}>".format(mail_domain)

  return requests.post(
    "https://api.mailgun.net/v3/{}/messages".format(mail_domain),
      auth=("api", mail_api_key),
      data={
        "from": sender,
        "to": [email],
        "subject": "Greetings!",
        "text": message
      })
