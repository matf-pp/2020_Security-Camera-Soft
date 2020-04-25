# Security Camera Soft.

## :scroll: Description:
This is software that detects movements and sends a notification to the user by email. There are two options:
1. To detect movements on the camera of your computer
2. To detect movements on an arbitrary recording that you assign to it

If you check option "Video", you need to give the relative path of the video.

You need to specify the email address and password from which the email will be sent, as well as the email address of the account to which the email will be sent. Email service of the sender must be gmail.

If it detects any movement in a recording or live broadcast from your camera, it will record that image and send you an email notification along with the image it recorded and the time the image was taken.

The project is written in the programming language Python and uses the background substrackion algorithm MOG2.

## :wrench: Installation:

#### Requirements:
In order to start the project you need to have installed different libraries and packages:
  * OpenCv library: <code> pip install opencv-python </code>
  * NumPy library: <code> pip3 install numpy </code>
  * Email package: <code> pip install email </code>
  * SMTPLib library: <code> pip install smtplib </code>
  * QT5 framework: [Installation guide](https://wiki.qt.io/Install_Qt_5_on_Ubuntu)
  
Also you will need to enable Gmail to allow less secure apps:
1. While logged into your gmail account press on the circle in top right corner
2. Click on "Manage google account"
3. On the left choose "Security"
3. Scroll down to the part that says "Allow less secure apps"
4. Turn ON "allow less secure apps".

#### Downloading and executing: 
* <code> git clone https://github.com/matf-pp/2020_Security-Camera-Soft.git </code> <br>
* <code> cd 2020_Security-Camera-Soft </code> <br>
* <code> pyuic5 -x gui.ui -o gui.py </code> <br>
* <code> python3 program.py </code>


## :e-mail: Authors:
The project was done by:
* Nikola Jovanovic, contact informations: <br>
          <code> nikolajovanov998@gmail.com </code> <br>
          <code> mi17078@alas.matf.bg.ac.rs </code>

* Milos Milakovic, contact informations: <br>
          <code> milos.milakovic98@gmail.com </code> <br>
          <code> mi17152@alas.matf.bg.ac.rs </code>
