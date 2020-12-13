import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Email_helper import *
import sendgrid
import os
from sendgrid.helpers.mail import *


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
    html_f=htm_f+f"""<p style="margin: 0;">Dear, User To reset your password Here's the OTP {otp}</p>"""+str(htm2_f)
    part1 = MIMEText(text_f, "plain")
    part2 = MIMEText(html_f, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP(smtp_server, port) as server:
            # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email. ... The EHLO command tells the receiving server it supports extensions compatible with ESMTP.
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted

            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
    except:        
        sg = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        from_email = Email("test@example.com")
        to_email = To(receiver_email)
        subject = "Sending with SendGrid is Fun"
        content = message.as_string()
        mail = Mail(from_email, to_email, subject, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        print(response.status_code)
        print(response.body)
        print(response.headers)
