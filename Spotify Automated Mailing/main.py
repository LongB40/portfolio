import smtplib
from email.message import EmailMessage

def main():
    email = EmailMessage()
    gmail_server = smtplib.SMTP('smtp.gmail.com', 587)
    gmail_server.starttls()
    gmail_server.login('long.automated.mail@gmail.com', '5uper.Secur3@!')

    email['from'] = 'long.automated.mail@gmail.com'
    email['to'] = 'dinhbaolongvn@gmail.com'
    email['subject'] = "This is a reminder for you to pay, Long!"
    email.set_content('test')
    gmail_server.send_message(email)
    gmail_server.quit()
    print ("Your mail has been sent successfully")
    
main()