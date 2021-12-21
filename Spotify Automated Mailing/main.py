import smtplib
from email.message import EmailMessage
from user import User
import json
import codecs


def main():
    """
    This is our main function, where it will handles most of the logistic of the system.
    TODO: 
    - Automated the whole thing.
    """

    # Initialize our bot to store the main user email information and the list of recievers.
    bot = User()

    # Initialize the object for structure our email.
    email = EmailMessage()

    # Initialize our connection with gmail.com server
    gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_server.starttls()
    gmail_server.login(bot.EMAIL_ADDRESS, bot.EMAIL_PASSWORD)

    # Retrieve list of recipients from our bot
    receiver_list = json.loads(bot.getList())

    # Go through each reciepents and send them an email.
    for key in receiver_list:
        message, subject = process_content('content.txt', key)
        print(message)
        exit()
        email['from'] = bot.EMAIL_ADDRESS
        email['to'] = receiver_list[key]
        email['subject'] = subject
        email.set_content(message)
        gmail_server.send_message(email)
    
    # Clean up and notification.
    gmail_server.quit()

    print ("Your mail has been sent successfully")


def process_content(filename, recipient_name):
    """
    This function is for processing the content.txt file.
        @Filename: The name of our content file
        @recipient_name: who is the one will be reciving this message

    TODO: 
    - Adding a generated joke or memes
    """
    
    # Open content file with utf-8 encoded
    with codecs.open(filename, 'r', "utf-8") as file:
        file_content = file.readlines()

    # seperate the subject and the message from the content file
    subject = file_content[0]
    message = ""
    for segment in file_content[2:]:
        message += segment

    # Replace @ with the recipent name
    message = message.replace("@", recipient_name) 

    file.close()

    return message, subject

main()
