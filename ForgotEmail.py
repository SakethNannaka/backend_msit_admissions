import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Email_helper import *

def forgot_email(receiver_email,otp):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "msitadmissions12@gmail.com"
    password = "Msit@2k19"
    message = MIMEMultipart("alternative")
    message["Subject"] = "RESEST PASSWORD "
    message["From"] = sender_email
    message["To"] = receiver_email

    
    # Turn these into plain/html MIMEText objects
    html_f=htm_f+str("""<p style="margin: 0;">Dear, User To reset your password Here's the OTP {otp}</p>""")+htm2_f
    part1 = MIMEText(text_f, "plain")
    part2 = MIMEText(html_f, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email. ... The EHLO command tells the receiving server it supports extensions compatible with ESMTP.
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted

        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

