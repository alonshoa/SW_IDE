import os
import shutil
import zipfile
import glob
import sys
import time
import datetime
import subprocess
import re
import pdb
import logging
import logging.handlers
import argparse
import getpass
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from os.path import basename
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


def get_logger(log_file):
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=10485760, backupCount=5)
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_args():
    parser = argparse.ArgumentParser(description='Collect all log files from a folder and put them in google drive')
    parser.add_argument('-f', '--folder', help='Folder to collect log files from', required=True)
    parser.add_argument('-d', '--drive_path', help='Google drive path to put the compressed file', required=True)
    parser.add_argument('-l', '--log_file', help='Log file', required=True)
    args = parser.parse_args()
    return args


def collect_all_logs(folder):
    files = glob.glob(folder + '/log*.txt*')
    return files


def zip_all_files(files, zip_file):
    with zipfile.ZipFile(zip_file, 'w') as zip_file:
        for file in files:
            zip_file.write(file)


def put_in_google_drive(zip_file, drive_path):
    SCOPES = 'https://www.googleapis.com/auth/drive'
    store = file.Storage('token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('drive', 'v3', http=creds.authorize(Http()))
    file_metadata = {'name': zip_file, 'parents': [drive_path]}
    media = service.files().create(body=file_metadata, media_body=zip_file).execute()


def main():
    args = get_args()
    logger = get_logger(args.log_file)
    files = collect_all_logs(args.folder)
    zip_file = args.folder + '/logs.zip'
    zip_all_files(files, zip_file)
    put_in_google_drive(zip_file, args.drive_path)


if __name__ == '__main__':
    main()

