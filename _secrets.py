import os

"""
Copyright (c) 2023 Jesse Meekins
See project 'license' file for more informations
"""

# Web Portal Login 
from datetime import datetime as dt
xml_website = 'https://memphistn-wfts-xfer.kronos.net/EFTClient/Account/Login.htm'


class Secrets:
    # IP address and port for SFTP service
    IP_ADDRESS = '158.228.129.229'
    PORT = '22'
    EXPORT_FILE_EXTENSION = '/PROD/export/'
    BDE_FILE_EXTENSION = '/PROD/export/bulk_data_export/'

    SERVER_PATH = "exports/"
    LOCAL_PATH = f'/Users/jessemeekins/Desktop/XML_EXPORTS/'
    TEST_PATH = f'/Users/jessemeekins/Desktop/XML_EXPORTS/'
    PROJECT_PATH = "/Users/jessemeekins/Documents/VS_CODE/PythonProjectTemplate/app/data/exports/"

    # Login Credentials for both website and SFTP connection
    SFTP_USERNAME = 'citphi-1@memphistn.gov'
    SFTP_PASSWORD = 'j54!GPu6j!3T3Avw6pIb'

    # Memphis Fire personnal FTP server IP and crednetials 
    LOCAL = "172.17.16.23"
    FTP_USERNAME = "sa_fireftp"
    FTP_PASSWORD = "RkK1$*4uKQf4H7"

# Set the environment variables
os.environ["IP_ADDRESS"] = Secrets.IP_ADDRESS
os.environ["PORT"] = Secrets.PORT
os.environ["EXPORT_FILE_EXTENSION"] = Secrets.EXPORT_FILE_EXTENSION
os.environ["BDE_FILE_EXTENSION"] = Secrets.BDE_FILE_EXTENSION
os.environ["DOCKER_PATH"] = Secrets.SERVER_PATH
os.environ["LOCAL_PATH"] = Secrets.LOCAL_PATH
os.environ["TEST_PATH"] = Secrets.TEST_PATH
os.environ["PROJECT_PATH"] = Secrets.PROJECT_PATH
os.environ["SFTP_USERNAME"] = Secrets.SFTP_USERNAME
os.environ["SFTP_PASSWORD"] = Secrets.SFTP_PASSWORD
os.environ["LOCAL"] = Secrets.LOCAL
os.environ["FTP_USERNAME"] = Secrets.FTP_USERNAME
os.environ["FTP_PASSWORD"] = Secrets.FTP_PASSWORD


