import smtplib

def send_email():
    sender_email = "email"
    app_password = "Pass"  # Use the actual app password here

    try:
        # Create SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender_email, app_password)

        # Collect message details
        receiver_email_id = input("Who do you want to send to? : ")
        subject = input("Subject: ")
        message = input("Message: ")

        # Format the email
        full_message = f"Subject: {subject}\n\n{message}"

        # Send the email
        s.sendmail(sender_email, receiver_email_id, full_message)
        print("Jarvis: Email sent successfully!")

    except Exception as e:
        print(f"Jarvis: Failed to send email - {e}")

    finally:
        # Terminating the session
        s.quit()
