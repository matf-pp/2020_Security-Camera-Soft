import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
email = 'mail1@gmail.com'
password = 'pass'
send_to_email = 'mail2@gmail.com'
subject = 'Subject'
message = 'This is some message'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message,'plain'))

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email,password)
text = msg.as_string()
server.sendmail(email,send_to_email,text)
server.quit()