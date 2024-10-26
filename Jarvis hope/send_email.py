import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os

def send_email(to_address, subject, message):
    # Load email credentials from environment variables
    email_address = os.getenv('EMAIL_USER')
    email_password = os.getenv('EMAIL_PASS')

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = email_address
    msg['To'] = to_address
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Connect to the server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(email_address, email_password)
            server.sendmail(email_address, to_address, msg.as_string())
        print("Jarvis: Email sent successfully.")
    except Exception as e:
        print(f"Jarvis: Failed to send email - {e}")
