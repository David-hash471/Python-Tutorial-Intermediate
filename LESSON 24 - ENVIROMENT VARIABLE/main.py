import os, smtplib
from email.message import EmailMessage
from dotenv import load_dotenv

def send_email(to_adress, subject, body):
    msg = EmailMessage()
    msg['From'] = os.getenv('EMAIL_ADDRESS')
    msg['To'] = to_adress
    msg['Subject'] = subject
    msg.set_content(body)
    
    with smtplib.SMTP(os.getenv('SMTP_SERVER'), int(os.getenv('SMTP_PORT'))) as smtp:
        smtp.starttls()
        smtp.login(os.getenv('EMAIL_ADDRESS'), os.getenv('EMAIL_PASSWORD'))
        smtp.send_message(msg)
            
    


def main():
    send_email(
        'simon.girdlestone@gmail.com',
        'An email using programing',
        'This email was sent created and sent using a python file rather than using gmail or outlook. \n Love David'

    )

if __name__ == "__main__":
    main()