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



