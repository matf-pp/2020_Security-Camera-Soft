import gui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys
import cv2
import numpy as np
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path
import time
import re

# Absolute path to the directory of the program
absolute_dirpath = os.path.abspath(os.path.dirname(__file__))

# Function that checks if the email is in the correct form
def checkEmail(email):
        if re.match(r"\b[\w.-]+@[\w.-]+(\.[\w.-]+)*\.[A-Za-z]{2,4}\b", email) is None:
            return False
        else:
            return True

class CameraClass(gui.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(CameraClass, self).__init__()
        self.setupUi(self)
        self.optionLabel.adjustSize()
        # Not possible to resize the window
        self.setFixedSize(942, 594)
        self.statusBar.setSizeGripEnabled(False)

        # Set action on radio buttons
        self.videoFrame.setVisible(False)
        self.computerCamera.toggled.connect(
        				lambda: self.recording(self.computerCamera.isChecked()))

        # Start the program
        self.pushButton.clicked.connect(lambda: self.start())

    def exError(self, video, times):
        video.release()
        times.close()
        cv2.destroyAllWindows()

    def recording(self, check):
        # Check type of recording where you detect motion
        if(check):
            self.videoFrame.setVisible(False)

        else:
            self.videoFrame.setVisible(True)

    def start (self):
    	# Get informations from the gui
        iemail = str(self.i_email.text())
        ipassword = str(self.i_password.text())

        # Report problem if the password is empty
        if ipassword == "":
            self.errorMessage("password")
            return

        # Call email function for check
        emailResult = checkEmail(iemail)

        if emailResult == False:
            self.errorMessage("sender")
            return

        # Call email function for check
        temail = str(self.receiveEmail.text())
        emailResult = checkEmail(temail)

        if emailResult == False:
            self.errorMessage("receiver")
            return

        # File where the time will be stored
        try:
            times = open('times.txt', 'a+')
        except IOError:
            print('Error while opening file times.txt!')

        # Delete previous times
        try:
            times.truncate(0)
        except:
            print('times.txt truncate error')

        # Open a window with live video where 0 is camera port
        vid = 0 if self.computerCamera.isChecked() else self.videoName.text()

        # If user didn't enter the path of the video
        if self.video.isChecked() and self.videoName.text() == "":
            times.close()
            self.errorMessage("video")
            return

        try:
            video = cv2.VideoCapture(vid)
        except:
            print("cv2.VideoCapture method error!")
            self.exError(video,times)
            return

        # Algorithm that detects changes/motions in the frame based on 300 previous frames
        try:
            fgbg = cv2.createBackgroundSubtractorMOG2(300, 200, True)
        except:
            print("cv2.createBackgroundSubtractorMOG2 method error!")
            self.exError(video,times)
            return

		# Frame count
        a = 0

        moving = 0
        firstTime = True
        timeNow = time.time()
        imagesPath = absolute_dirpath +'/images'

        # ID of an image that will be stored in a folder
        imageID = 0

        # Delete images from the previous detection
        try:
            filelist = [ f for f in os.listdir(imagesPath) ]
            for f in filelist:
                os.remove(os.path.join(imagesPath, f))
        except:
            print("Error trying to remove content on images directory")
            self.exError(video,times)
            return

        while True:
            a = a + 1

			# Capture frame-by-frame
            try:
                _, frame = video.read()
            except:
                print("video.read method error!")
                self.exError(video,times)
                return

			# Foreground mask
            try:
                fgmask = fgbg.apply(frame)
            except:
                print("fgbg.apply method error!")
                self.exError(video,times)
                return

            # Count all the non zero pixels within the mask - white pixels are non zero
            try:
                count = np.count_nonzero(fgmask)
            except:
                print("np.count_nonzero method error!")
                self.exError(video,times)
                return

			# If the motion is big enough to be valid:
			# - a > 1 because first frame is all black
            if a > 1 and count > 3000:
                #print(a)
                moving += 1

                if moving > 10:

                    moving -= 10
					# Time when detection of the motion was made
                    seconds = time.time()
                    ltime = time.ctime(seconds)

                    try:
                        times.write(ltime + "\n")
                    except:
                        print("Unable to write in times.txt file")
                        self.exError(video,times)
                        return

                    fileName = 'image' + str(imageID) + '.jpg'
                    imageID += 1

                    # Save an image
                    try:
                        cv2.imwrite(os.path.join(imagesPath, fileName), frame)
                    except:
                        print("cv2.imwrite method error!")
                        self.exError(video,times)
                        return

                    timeLast = timeNow
                    timeNow = time.time()
                    timeDelta = timeNow - timeLast

                    # Send new notification if more than 5 minutes have passed between the two saved images
                    if timeDelta > 300 or firstTime:
                        firstTime = False

                        # Account you are sending mail from
                        email = iemail
                        password = ipassword
                        send_to_email = temail
                        subject = 'Motion detected'
                        message = ltime

                        # Creates the container email message
                        try:
                            msg = MIMEMultipart()
                        except:
                            print("Failed to create container email message")
                            self.exError(video,times)
                            return

                        # The contents of email
                        msg['From'] = email
                        msg['To'] = send_to_email
                        msg['Subject'] = subject

                        # Attach your message
                        try:
                            msg.attach(MIMEText(message, 'plain'))
                        except:
                            print("Failed to attach your message")
                            self.exError(video,times)
                            return

                        # Move to images directory
                        try:
                            os.chdir(imagesPath)
                        except:
                            print("Failed changing the current directory")
                            self.exError(video,times)
                            return

                        # Open file in binary format
                        try:
                            attachment = open(fileName, "rb")
                        except IOError:
                            print("Unable to open file")
                            self.exError(video,times)
                            return

                        part = MIMEBase('application', 'octet-stream')
                        part.set_payload((attachment).read())
                        encoders.encode_base64(part)

                        try:
                            part.add_header('Content-Disposition',"attachment; filename= %s" % fileName)
                        except:
                            print("Unable to attach image")
                            self.exError(video,times)
                            return

                        msg.attach(part)

                        try:
                            os.chdir(absolute_dirpath)
                        except:
                            print("Failed changing the current directory")
                            self.exError(video,times)
                            return

                        # Set up the connection to the gmail server
                        try:
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                        except:
                            print("Unable to set up connection to the gmail server")
                            self.exError(video,times)
                            return

                        # Log in to account that is sending mail
                        try:
                            server.login(email,password)
                        except:

                            # Error message
                            self.errorMessage("authorization")

                            # End everything
                            self.exError(video,times)
                            return

                        text = msg.as_string()

                        try:
                            server.sendmail(email,send_to_email, text)
                        except:
                            print("Unable to send email")
                            self.exError(video,times)
                            return

                        # End connection to the server
                        server.quit()

            # Functions to display an image in a window
            try:
                cv2.imshow('capturef', frame)
                cv2.imshow('capture', fgmask)
            except:
                self.exError(video, times)
                return

            # Waits for a key stroke
            key = cv2.waitKey(1) & 0xff

            # Convert to unicode and check if it is 'q'
            if key == ord('q'):
                break

        video.release()

        times.close()

        # To destroy all the windows that are created
        cv2.destroyAllWindows()

    # Show popup window with the notice about mistake
    def errorMessage(self, problem):
        msg = QMessageBox()

        if problem == "sender":
            msg.setWindowTitle("Email")
            msg.setText("You entered the wrong form of the sender's email.")
        elif problem == "receiver":
            msg.setWindowTitle("Email")
            msg.setText("You entered the wrong form of the receiver's email.")
        elif problem == "authorization":
            msg.setWindowTitle("Authorization")
            msg.setText("You entered the wrong email or password.")
        elif problem == "password":
            msg.setWindowTitle("Password")
            msg.setText("You left empty password.")
        elif problem == "video":
            msg.setWindowTitle("Video")
            msg.setText("You didn't enter the relative path of the video.")

        msg.setIcon(QMessageBox.Critical)

        # Show message
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    camera = CameraClass()
    camera.show()
    sys.exit(app.exec_())