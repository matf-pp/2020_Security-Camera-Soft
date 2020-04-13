import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
fileLocation = '/home/korisnik/Desktop/pp/projekat/slika.jpg'

email = 'something@gmail.com'
password = 'pass'
send_to_email = 'something2@gmail.com'
subject = 'Subject'
message = 'This is some message'

msg = MIMEMultipart()
msg['From'] = email
msg['To'] = send_to_email
msg['Subject'] = subject

msg.attach(MIMEText(message,'plain'))

filename = os.path.basename(fileLocation)
attachment = open(fileLocation, "rb")
part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= %s" % filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email,password)
text = msg.as_string()
server.sendmail(email,send_to_email,text)
server.quit()