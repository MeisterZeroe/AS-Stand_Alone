# mail.py

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_password_reset_email(user_email, username, reset_link):
    # set up the SMTP client
    smtp_client = smtplib.SMTP(host='smtp.gmail.com', port=587)
    smtp_client.starttls()
    smtp_client.login('alphashot.reset@gmail.com', 'gqscunrirosfofql')

    msg = MIMEMultipart()  # create a message

    # setup the parameters of the message
    msg['From']="alphashot.reset@gmail.com"
    msg['To']=user_email
    msg['Subject']="Password Reset Link for AlphaShot Inventory System"

    # add in the message body
    message = f"Hi {username},\n\nHere is your password reset link: {reset_link}\n\nBest,\nAlphaShot Team"
    msg.attach(MIMEText(message, 'plain'))

    # send the message via the SMTP client
    smtp_client.send_message(msg)

    del msg

    print("Password reset email sent successfully.")
