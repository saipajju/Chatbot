import os
import smtplib
from email.message import EmailMessage

feedback = input('Help us improve.What do you want more in chatbot? ')
EMAIL_ADDRESS = 'sparjanya@gmail.com'
EMAIL_PASSWORD = 'thtldgzodrodpebf'

msg = EmailMessage()
msg['Subject'] = 'Feedback'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'saiparjanyam@gmail.com'
msg.set_content(feedback)


with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
