import smtplib
from email.message import EmailMessage
from user import User
import json
import codecs


def main():
    bot = User()
    email = EmailMessage()
    gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_server.starttls()
    gmail_server.login(bot.EMAIL_ADDRESS, bot.EMAIL_PASSWORD)

    receiver_list = json.loads(bot.getList())

    for key in receiver_list:
        email['from'] = bot.EMAIL_ADDRESS
        email['to'] = receiver_list[key]
        email['subject'] = "This is a reminder for you to pay, Long!"
        email.set_content(process_main_content('content.txt', key))
        gmail_server.send_message(email)
    
    gmail_server.quit()

    print ("Your mail has been sent successfully")


def process_main_content(filename, recipient_name):
    with codecs.open(filename, 'r', "utf-8") as file:
        message = file.read()

    message = message.replace("@", recipient_name)

    file.close()

    return message


main()
