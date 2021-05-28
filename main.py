# Create a simple text email with  Subject  \‘Greetings’ in Python and send it to multiple recipients. Write your own
# message. Send it ot your lecturer and to one or two of your friends.

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

mailers_id = "gideondaniels.dragoonix@gmail.com"
email_receiver_id = ["gideon.daniels@yahoo.com", "thapelo.thapelo@gmail.com", "aslamedien9@gmail.com"]
password = input("Enter your password")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = subject
msg['To'] = ", ".join(email_receiver_id)
body = "Hello fellow students and lecturer.\n"
body = body + "How are you doing today"
msg.attach(MIMEMultipart(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP("smtp.gmail.com", 587)
s.starttls()
s.login(mailers_id, password)  # Authentication
s.starttls()
s.login(mailers_id, password)  # message to be send
s.sendmail(mailers_id,email_receiver_id, text)  # send the mail
s.quit()
