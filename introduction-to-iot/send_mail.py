import smtplib
import time
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.mime.image import MIMEImage
import datetime

print "Sending email"
fromaddr = "FROM@EMAIL.com"
toaddr = "TO@EMAIL.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Face detected!"

body = "Face has been detected - " + str(datetime.datetime.now())
msg.attach(MIMEText(body, 'plain'))
msg.attach(MIMEImage(file("face.jpg").read()))
text = msg.as_string()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("USER@EMAIL.com", "PASSWORD")
server.sendmail(fromaddr, toaddr, text)
server.quit()

