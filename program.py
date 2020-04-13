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

# Absolute path to the directory of the program
absolute_dirpath = os.path.abspath(os.path.dirname(__file__))
fileName = 'slika.jpg'

class CameraClass(gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        
        super(CameraClass, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(lambda: self.start())
        

    def start (self):
    
    	# Get informations from the gui
        iemail = self.i_email.text()
        ipassword = self.i_password.text()
        
        # Open a window with live video where 0 is camera port
        # TODO IN VIDEOCAPTURE IF YOU WANT PLACE VIDEO THAT YOU HAVE
        video = cv2.VideoCapture(0)
        
        # Algorithm that detects changes/motions in the frame based on 300 previous frames
        fgbg = cv2.createBackgroundSubtractorMOG2(300, 200, True)

		# Frame count
        a = 0
        
        first_frame = None
        tmp = False
        moving = 0

        while True:
            a = a + 1
			
			# Capture frame-by-frame
            check, frame = video.read()

			# Foreground mask
            fgmask = fgbg.apply(frame)
            
            # Count all the non zero pixels within the mask - white pixels are non zero
            count = np.count_nonzero(fgmask)

			# If the motion is big enough to be valid:
			# - a > 1 because first frame is all black
            if a > 1 and count > 3000:
                print(a)
                moving += 1
                
                if tmp == False and moving > 10:
                    tmp = True
                    
                    # Save an image
                    cv2.imwrite(os.path.join(absolute_dirpath, fileName), frame)

					# Account you are sending mail from
                    email = '@gmail.com'
                    password = 'pass'
                    send_to_email = iemail
                    subject = 'Subject'
                    message = 'This is some message'

					# Creates the container email message
                    msg = MIMEMultipart()
                    
     				# The contents of email
                    msg['From'] = email
                    msg['To'] = send_to_email
                    msg['Subject'] = subject

					# Attach your message
                    msg.attach(MIMEText(message, 'plain'))
                    
                    # Open file in binary format
                    attachment = open(fileName, "rb")
                    
                    part = MIMEBase('application', 'octet-stream')
                    part.set_payload((attachment).read())
                    encoders.encode_base64(part)
                    part.add_header('Content-Disposition',"attachment; filename= %s" % fileName)

                    msg.attach(part)

					# Set up the connection to the gmail server
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.starttls()
                    
                    # Log in to account that is sending mail
                    server.login(email,password)
                    text = msg.as_string()
                    server.sendmail(email,send_to_email, text)
                    
                    # End connection to the server
                    server.quit()
                    
            # Functions to display an image in a window
            cv2.imshow('capturef', frame)
            cv2.imshow('capture', fgmask)
				    
            # Waits for a key stroke
            key = cv2.waitKey(1) & 0xff
            
            # Convert to unicode and check if it is 'q'
            if key == ord('q'):
                break

        print(a)
        video.release()
        
        # To destroy all the windows that are reated
        cv2.destroyAllWindows()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    camera = CameraClass()
    camera.show()
    sys.exit(app.exec_())
