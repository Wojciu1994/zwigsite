#!/usr/bin/python2.7

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

FROM = 'ziwg.projekt@gmail.com'
TO = ["@student.pwr.edu.pl"]
SUBJECT = "Ukonczono tworzenie modelu"
TEXT = "Ukonczono tworzenie modelu. Link: "

def send(recipients, linkstr):

    msg = MIMEMultipart()
    msg['Subject'] = SUBJECT
    msg['From'] = FROM
    msg['To'] = ", ".join(recipients)
    text = MIMEText(TEXT + linkstr, 'plain')
    msg.attach(text)

    server = smtplib.SMTP('smtp.gmail.com:587');
    server.ehlo();
    server.starttls();
    server.login('ziwg.projekt@gmail.com','zaq123wsx');
    server.sendmail(FROM, recipients, msg.as_string());
    server.quit();

if __name__ == '__main__':
    send(TO, "pusty_link"); 
