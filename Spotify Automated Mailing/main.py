import smtplib, json, io
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from user import User

def main():
    """
    This is our main function, where it will handles most of the logistic of the system.
    TODO: 
    - Automated the whole thing.
    - Fix the error, that the content of email doesn't show correctly
    """

    # Initialize our bot to store the main user email information and the list of recievers.
    bot = User()
    
    # Initialize our connection with gmail.com server
    gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_server.starttls()
    gmail_server.login(bot.EMAIL_ADDRESS, bot.EMAIL_PASSWORD)

    # Retrieve list of recipients from our bot
    receiver_list = json.loads(bot.getList())

    # Go through each reciepents and send them an email.
    for key in receiver_list:
        # Initialize the object for structure our email.
        email = MIMEMultipart()
        message, subject = process_content('content.txt', key)
        email['from'] = bot.EMAIL_ADDRESS
        email['to'] = receiver_list[key]
        email['subject'] = subject
        email.attach(MIMEText(message, "plain"))
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
    with io.open(filename, 'r', encoding='utf8') as file:
        file_content = file.readlines()

    # seperate the subject and the message from the content file
    subject = file_content[0]
    message = ""
    for segment in file_content[1:]:
        message += segment

    # Replace @ with the recipent name
    message = message.replace("@", recipient_name) 

    file.close()

    return message, subject

main()
