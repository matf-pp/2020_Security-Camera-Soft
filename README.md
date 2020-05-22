# Security Camera Soft

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f405c857b9864b0dafd18d1759c8406a)](https://app.codacy.com/gh/matf-pp/2020_Security-Camera-Soft?utm_source=github.com&utm_medium=referral&utm_content=matf-pp/2020_Security-Camera-Soft&utm_campaign=Badge_Grade_Dashboard)

## :scroll: Description
This is software that detects movements and sends a notification to the user by email. There are two options:
1.  To detect movements on the camera of your computer
2.  To detect movements on an arbitrary recording that you assign to it

If you check option "Video", you need to give the relative path of the video.

You need to specify the email address and password from which the email will be sent, as well as the email address of the account to which the email will be sent. Email service of the sender must be gmail.

Clicking on the start button will open two new windows. In one you will see the actual image of the recording and in the other it will show a black and white image. Black shows the background, respectively, objects that are static and white represents objects that move, and that movement will be detected. <br>
Press <kbd>q</kbd> when you want to finish detection.
<br>
If it detects any movement in a recording or live broadcast from your camera, it will record that image and send you an email notification along with the image it recorded and the time the image was taken. <br>
Program sends only the first created image together with its creation time.<br>
If more than 5 minutes have passed between the two saved images, the program will send a new notification.
<br>
All captured images will be saved in the "images" directory, the times the images were taken will be saved in the "times.txt" file.
<br>
The project was written in the programming language Python and uses the background subtraction algorithm MOG2.
<br>
The program is compatible with the LUbuntu and Ubuntu operating systems of any version on which the libraries listed below can be installed.

![gui](https://github.com/matf-pp/2020_Security-Camera-Soft/blob/master/Screenshots/screen1.jpg)

## :wrench: Installation - two options
*   Program startup is possible by downloading the released version of the software, unpacking it 
and then accessing the "program" directory. In directory find the executable file named "program" and run it. In this case you won't need to download all the libraries, however, you will still need to enable Gmail
to allow less secure apps ([guide](#you-will-need-to-enable-gmail-to-allow-less-secure-apps)).
*   You can run it manually by downloading all of the requirements bellow and following further steps.<br>

### Requirements
In order to manually start the project you need to have installed different libraries and packages:
*   OpenCv library: <code> pip install opencv-python </code>
*   NumPy library: <code> pip3 install numpy </code>
*   Email package: <code> pip install email </code>
*   SMTPLib library: <code> pip install smtplib </code>
*   PyQt5 framework: [Installation guide](https://gist.github.com/ujjwal96/1dcd57542bdaf3c9d1b0dd526ccd44ff)

### You will need to enable Gmail to allow less secure apps
1.  While logged into your gmail account press on the circle in top right corner
2.  Click on "Manage google account"
3.  On the left choose "Security"
4.  Scroll down to the part that says "Allow less secure apps"
5.  Turn ON "allow less secure apps".

### Downloading and executing
*   <code>git clone <https://github.com/matf-pp/2020_Security-Camera-Soft.git></code><br>
*   <code>cd 2020_Security-Camera-Soft</code><br>
*   <code>pyuic5 -x gui.ui -o gui.py</code><br>
*   <code>python3 program.py</code>

## :e-mail: Authors
The project was done by:
*   Nikola Jovanovic, contact informations: <br>
          <code> [nikolajovanov998@gmail.com](<mailto:nikolajovanov998@gmail.com>) </code> <br>
          <code> [mi17078@alas.matf.bg.ac.rs](<mailto:mi17078@alas.matf.bg.ac.rs>) </code>

*   Milos Milakovic, contact informations: <br>
          <code> [milos.milakovic98@gmail.com](<mailto:milos.milakovic98@gmail.com>) </code> <br>
          <code> [mi17152@alas.matf.bg.ac.rs](<mailto:mi17152@alas.matf.bg.ac.rs>) </code>
