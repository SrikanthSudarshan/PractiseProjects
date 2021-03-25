import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()

with open('password.txt', 'r') as f:
    password = f.read()

server.login('emailmname@email.dom', password)

msg = MIMEMultipart()
msg['From'] = 'sender'
msg['To'] = 'vishal10420@gmail.com'
msg['Subject'] = 'Welcome'

with open('message.txt', 'r') as f:
    message = f.read()

msg.attach(MIMEText(message, 'plain'))

filename = 'Gayatri1.jpg'
attachment = open(filename, 'rb')

p = MIMEBase ('application', 'octet-stream' )
p.set_payload(attachment.read())

encoders.encode_base64(p)
p.add_header('Content-Disposition', f'attachment; filename= {filename}')
msg.attach(p)

text = msg.as_string()
server.sendmail('emailmname@email.dom','vishal10420@gmail.com, text')