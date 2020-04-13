import gui
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import cv2
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
fileLocation = '/home/korisnik/Desktop/pp/projekat/slika.jpg'

class CameraClass(gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(CameraClass, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.start())
        

    def start (self):
        iemail = self.i_email.text()
        ipassword = self.i_password.text()
        video = cv2.VideoCapture(0)
        fgbg = cv2.createBackgroundSubtractorMOG2(300,200,True)

        a = 0
        first_frame = None
        tmp = False
        moving = 0

        while True:
            a = a+1
            check, frame = video.read()

            fgmask = fgbg.apply(frame)
            
            count = np.count_nonzero(fgmask)

            if a > 1 and count > 3000:
                print(a)
                moving += 1
                if tmp == False and moving > 10:
                    tmp = True
                    cv2.imwrite("slika.jpg", frame)

                    email = '@gmail.com'
                    password = 'pass'
                    send_to_email = iemail
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

            cv2.imshow('capturef',frame)
            cv2.imshow('capture',fgmask)
            key = cv2.waitKey(1)
            if key == ord('q'):
                break

        print(a)
        video.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    camera = CameraClass()
    camera.show()
    sys.exit(app.exec_())