# Create a simple text email with  Subject  \‘Greetings’ in Python and send it to multiple recipients. Write your own
# message. Send it ot your lecturer and to one or two of your friends.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

send_mail_id = "gideondaniels.dragoonix@gmail.com"
receiver_email_id = ["gideon.daniels@yahoo.com", "thapelo.thapelo@gmail.com", "aslamedien9@gmail.com"]
password = input("Enter your password")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = subject
msg['To'] = ", ".join(receiver_email_id)
body = "Hello fellow students and lecturer.\n"
body = body + "How are you doing today"
msg.attach(MIMEMultipart(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(send_mail_id, password)  # Authentication
s.starttls()
s.login(send_mail_id, password)  # message to be send
s.sendmail(send_mail_id, receiver_email_id, text)  # send the mail
s.quit()
