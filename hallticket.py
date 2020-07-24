import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase 
from email import encoders 

def send_hallticket(receiver_email):
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = "msitadmissions12@gmail.com"
    password = "Msit@2k19"
    message = MIMEMultipart("alternative")
    message["Subject"] = "MSIT ADMISSIONS 2020"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of your message
    text = """\
    Hi,
    How are you?
    Real Python has many great tutorials:
    www.realpython.com"""

    html = f"""\

    <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0 Transitional//EN">
    <html>
    <head>
    <link rel="stylesheet" type="text/css" href="style.css"/>
    </head>
    <body>
    <div style="position:absolute;top:0.64in;left:1.60in;width:6.17in;line-height:0.35in;"><span style="font-style:normal;font-weight:bold;font-size:20pt;font-family:Times;color:#000000">Consortium of Institutions of Higher Learning </span><span style="font-style:normal;font-weight:bold;font-size:20pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:1.02in;left:1.43in;width:6.42in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">IIIT Campus, Gachibowli, Hyderabad - 32, Phone: 040-23001970,Mobile: 7799834583, 7799834585</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <img style="position:absolute;top:1.29in;left:1.07in;width:6.96in;height:0.03in" src="ri_1.jpeg" />
    <img style="position:absolute;top:1.50in;left:1.07in;width:1.50in;height:0.73in" src="ri_2.jpeg" />
    <div style="position:absolute;top:1.55in;left:3.21in;width:4.15in;line-height:0.25in;"><span style="font-style:normal;font-weight:bold;font-size:14pt;font-family:Times;color:#000000">Master of Science in Information Technology</span><span style="font-style:normal;font-weight:bold;font-size:14pt;font-family:Times;color:#000000"> </span><br/><DIV style="position:relative; left:1.17in;"><span style="font-style:normal;font-weight:bold;font-size:14pt;font-family:Times;color:#000000">Entrance Test 2019</span><span style="font-style:normal;font-weight:bold;font-size:14pt;font-family:Times;color:#000000"> </span><br/></SPAN></DIV></div>
    <div style="position:absolute;top:2.14in;left:4.45in;width:1.69in;line-height:0.28in;"><span style="font-style:normal;font-weight:bold;font-size:16pt;font-family:Times;color:#000000">HALLTICKET</span><span style="font-style:normal;font-weight:bold;font-size:16pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:2.94in;left:1.12in;width:1.29in;line-height:0.21in;"><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000">Hall Ticket No :</span><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:2.94in;left:3.26in;width:0.91in;line-height:0.21in;"><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000">197G00485</span><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:3.37in;left:1.12in;width:1.94in;line-height:0.21in;"><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000">Name of the Candidate :</span><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:3.37in;left:3.26in;width:2.13in;line-height:0.21in;"><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000">SAI SAKETH NANNAKA</span><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:3.80in;left:1.12in;width:1.28in;line-height:0.21in;"><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000">Payment Type :</span><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:3.80in;left:3.26in;width:0.76in;line-height:0.21in;"><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000">ONLINE</span><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <img style="position:absolute;top:2.36in;left:6.87in;width:1.50in;height:1.93in" src="https://admissionsimagebucket.s3.ap-south-1.amazonaws.com/nannakasaisaketh%40gmail.com.jpeg" />
    <img style="position:absolute;top:4.72in;left:1.20in;width:7.09in;height:2.21in" src="ri_5.jpeg" />
    <div style="position:absolute;top:5.08in;left:3.40in;width:0.54in;line-height:0.21in;"><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000">Venue</span><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:5.00in;left:6.67in;width:1.06in;line-height:0.19in;"><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000">Time &amp; Date</span><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000"> </span><br/><DIV style="position:relative; left:0.10in;"><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000">of the Test</span><span style="font-style:normal;font-weight:bold;font-size:12pt;font-family:Times;color:#000000"> </span><br/></SPAN></DIV></div>
    <div style="position:absolute;top:5.61in;left:1.42in;width:3.42in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">G Narayanamma Institute of Technology &amp; Science,</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:5.83in;left:1.42in;width:2.37in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">(LIB Block New Building) Shaikpet,</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:6.04in;left:1.42in;width:3.60in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">Mehdipatnam(Hi-Tech City Road), Hyderabad-500008</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:6.30in;left:1.42in;width:1.49in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">Contact: Col MS Raju</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:6.51in;left:1.42in;width:2.25in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">Phone: 9949159160, 040-23565648</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:5.95in;left:6.91in;width:0.64in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">09:00AM</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:5.70in;left:6.86in;width:0.74in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">26-05-2019</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:7.01in;left:1.12in;width:2.62in;line-height:0.24in;"><span style="font-style:normal;font-weight:bold;font-size:14pt;font-family:Times;color:#000000">Instructions for Candidates:</span><span style="font-style:normal;font-weight:bold;font-size:14pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:7.37in;left:1.33in;width:5.71in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">1. Any error/change in your name/address must be communicated immediately through</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:7.59in;left:1.33in;width:2.55in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">email to : enquiries@msitprogram.net.</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:7.80in;left:1.33in;width:5.56in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">2. The candidate is being conditionally allowed to appear in the entrance examination</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:8.02in;left:1.33in;width:5.68in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">without verifying whether he/she satisfies the eligibility criterion. This will be examined</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:8.23in;left:1.33in;width:2.66in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">at the time of final admission, if granted.</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:9.39in;left:1.76in;width:1.78in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">Signature of the Candidate</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <div style="position:absolute;top:9.39in;left:6.49in;width:0.94in;line-height:0.17in;"><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000">(Dean, CIHL)</span><span style="font-style:normal;font-weight:bold;font-size:10pt;font-family:Times;color:#000000"> </span><br/></SPAN></div>
    <img style="position:absolute;top:8.80in;left:5.93in;width:1.72in;height:0.42in" src="ri_6.jpeg" />
    </body>
    </html>

    """
    # Turn these into plain/html MIMEText objects
    filename = "sample.pdf"
    attachment = open("/home/saketh/Desktop/Deploy MSIT/msit-admissions/sample.pdf","rb") 
    p = MIMEBase('application', 'octet-stream') 
  
    # To change the payload into encoded form 
    p.set_payload((attachment).read()) 
      
    # encode into base64 
    encoders.encode_base64(p) 
       
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
      
    # attach the instance 'p' to instance 'msg' 
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part1)
    # message.attach(part2)
    message.attach(p) 

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        # Extended HELO (EHLO) is an Extended Simple Mail Transfer Protocol (ESMTP) command sent by an email server to identify itself when connecting to another email server to start the process of sending an email. ... The EHLO command tells the receiving server it supports extensions compatible with ESMTP.
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted

        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())

