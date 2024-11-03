import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("nilabh2020@gmail.com", "APP_pass")
# message to be sent
message = input("Message: ")
receiver_email_id = input("Who do you want to send to? : ")
s.sendmail("nilabh2020@gmail.com", receiver_email_id, message)
# terminating the session
s.quit()
