MFD Daily Numbers Project
=========================
About
-----
This is a project aimed at using XML files to access daily operational information within an orignization. 

Brief Discription of file structure:
====================================

SFTP_MAIN.py
------------
This files takes in args from the command line and performs the desired functionality on 'sftp_Client.py'
**NOTE:**
This script will not work on COM Guest Wifi.

sftp_Client.py
--------------
This file uses paramiko to establish the SFTP server connection and download the files

request_config.py
-----------------
This file hold different args that SFTP_MAIN.py can make. Then this file returns the configurtation parameters in dict format to be passed through to the SFTP server and executed.

_secrets.py
-----------
Holds the log in credentials and file paths to be passed though as arguments. 

Crontab
-------
Executes every 15 minutes;

To execute script.py -> launch shell and type -> "crontab -e"
expression -> "15/15 * * * * name/of/file/path/filename.py"
