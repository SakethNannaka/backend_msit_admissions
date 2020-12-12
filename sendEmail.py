import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Email_helper import *

def send_email(receiver_email,token_url):
    port = 587  # For ssl for ttl it's 587
    smtp_server = "smtp.gmail.com"
    sender_email = "msitadmissions12@gmail.com"
    password = "Msit@2k19"
    message = MIMEMultipart("alternative")
    message["Subject"] = "MSIT ADMISSIONS 2020"
    message["From"] = sender_email
    message["To"] = receiver_email

    html = htm+str("""<td align="center" style="border-radius: 3px;" bgcolor="#FFA73B"><a href="https://flask-deploy-admissions.herokuapp.com/confirm_email/{token_url}" target="_blank" style="font-size: 20px; font-family: Helvetica, Arial, sans-serif; color: #ffffff; text-decoration: none; color: #ffffff; text-decoration: none; padding: 15px 25px; border-radius: 2px; border: 1px solid #FFA73B; display: inline-block;">Confirm Account</a></td>"""
    )+html2

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)
    
    context = ssl.create_default_context()
    # try:
    with smtplib.SMTP(smtp_server, port) as server:
        # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email. ... The EHLO command tells the receiving server it supports extensions compatible with ESMTP.
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            # server.ehlo()  # Can be omitted
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.close()
    # except:
        # print("login/email sending failed")
