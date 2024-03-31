# blogWorld

# Steps to execute the above project

1] To use the "**django-project**" in your device first clone it with github desktop or download the .zip file and then extract it.
<br><br>
2] To start it's execution first open the first project directory(eComm) and inside the terminal create the python virtual environment using the command "**virtualenv envName**" or "**python -m virtualenv envName**", now it's path can be shown as below <br>
"**(envName) localDriveName:\blogWebSite>**"
<br><br>
3] Now activate the virtualenv using command "**envName\Scripts\activate**".
<br><br>
4] Now install django by executing the command "**pip install django**" inside the terminal.
<br><br>
5] Now in the terminal, change the directory using command "**cd blogApp**", now it's path can be shown as below <br>
"**(envName) localDriveName:\blogWebSite> cd blogApp**"
<br><br>
6] In order to execute and run this project you need to **first install XAMPP software from https://www.apachefriends.org/download.html**
<br><br>
7] After it's completion of installation you need to connect the xampp database with your django-project inside the **settings.py** project file by making below corrections.<br>
a] Execute the **import os** module command. <br><br>
b] Also for the smooth execution oftemplates, static files and media folder use below statements: <br>
i] For templates files & folder: <br>
'DIRS': [os.path.join(BASE_DIR, 'templates')],<br>
ii] For static files & folder: <br>
STATIC_URL = 'static/'<br>
STATICFILES_DIRS = [<br>
&nbsp;&nbsp;os.path.join(BASE_DIR, 'static')<br>
]<br>
iii] For media files & older:
MEDIA_URL = '/media/'<br>
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')<br><br>
c] Inside the settings.py file make below changes: <br>
DATABASES = {<br>
&nbsp;&nbsp;'default': {<br>
&nbsp;&nbsp;&nbsp;&nbsp;'ENGINE': 'django.db.backends.mysql',<br>
&nbsp;&nbsp;&nbsp;&nbsp;'NAME': 'your-database-name',<br>
&nbsp;&nbsp;&nbsp;&nbsp;'HOST': 'localhost',<br>
&nbsp;&nbsp;&nbsp;&nbsp;'USER': 'root',<br>
&nbsp;&nbsp;&nbsp;&nbsp;'PASSWORD': '',<br>
&nbsp;&nbsp;&nbsp;&nbsp;'POST': '3306',<br>
&nbsp;&nbsp;}<br>
}<br><br>

8] For email integration make below changes in your settings.py file<br>
&nbsp;&nbsp;# EMAIL SETTINGS<br>
&nbsp;&nbsp;EMAIL_HOST = "smtp.gmail.com"<br>
&nbsp;&nbsp;EMAIL_HOST_USER = "yourname@example.com"<br>
&nbsp;&nbsp;EMAIL_HOST_PASSWORD = "YOUR-EMAIL-APP-PASSWORD"<br>
&nbsp;&nbsp;EMAIL_PORT = 587<br>
&nbsp;&nbsp;EMAIL_USE_TLS = True<br>
&nbsp;&nbsp;EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"<br><br>

9] In application views.py file make the changes in the send_user_email function i.e. change the defaultmail to your default mail
![image](https://github.com/SiddheshP1996/blogWorld/assets/67057053/dd3a8a9a-6599-4f10-afae-d70d63c33e73)
<br><br>
10] First check whether the database is connected or not using 2 commands "**python manage.py makemigrations**" and "**python manage.py migrate**".
<br><br>
11] In order to run the project execute the command "**python manage.py runserver**" inside the terminal. 
<br><br>
![image](https://github.com/SiddheshP1996/blogWorld/assets/67057053/91395239-d74e-4f21-8fdc-a5374356ac16)
<br><br>
12] Now as per the above image click on the link generated stating : "**Starting development server at http://127.0.0.1:8000/**" and start exploring the project and it's smooothness in it's dynamic nature of event handling.
<br><br>
13] To stop the running/execution of project go to the terminal and type **ctrl + C**.
<br><br>
14] Now inside the terminal execute the command **cd ..**, so as to exit the project working directory i.e. "**(envName) localDriveName:\folderName\blogWebSite\blogApp>cd..**".
<br><br>
15] You will be directed to the folder location of "**(envName) localDriveName:\folderName\blogWebSite>**".
<br><br>
16] Now to deactivate the virtual environment inside the terminal at current working dfirectory use the command **deactivate** i.e. "**(envName) localDriveName:\folderName\blogWebSite>deactivate**"
<br><br>
17] Now you will be taken out of the virtual environment to your noraml folder path i.e. **localDriveName:\blogWebSite>**
<br><br>
18] Now to exit from the terminal execute the **exit** command then the terminal will be closed i.e. **localDriveName:\blogWebSite>exit**
<br><br>

**Provide Your Valuable Feedback on the Project.**
<br><br>
**Thank You !!**
<br><br>
