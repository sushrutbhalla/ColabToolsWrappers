import argparse

parser = argparse.ArgumentParser(description='Download file from Google Drive to Google Colab.')
parser.add_argument('fileID', metavar='file_id', type=str, nargs='+',
                    help='file_id of the drive file to download')
parser.add_argument('destinationFile', metavar='dest_file', type=str, nargs='+',
                    help='destination file name in Colab to store contents of file')

args = parser.parse_args()
download_location = args.destinationFile
file_id = args.fileID
debug = False

#setup access to google drive from colab
from google.colab import auth
from googleapiclient.discovery import build
import io , requests, os
import sys
auth.authenticate_user()
from googleapiclient.discovery import build
drive_service = build('drive', 'v3')

import tensorflow as tf
import timeit

config = tf.ConfigProto()
config.gpu_options.allow_growth = True

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

# Authenticate and create the PyDrive client.
auth.authenticate_user()
gauth = GoogleAuth()
gauth.credentials = GoogleCredentials.get_application_default()
drive = GoogleDrive(gauth)

# #list files in the google drive
# file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
# for file1 in file_list:
#   print('title: %s, id: %s' % (file1['title'], file1['id']))

from googleapiclient.http import MediaIoBaseDownload
request = drive_service.files().get_media(fileId=file_id)
downloaded = io.BytesIO()
downloader = MediaIoBaseDownload(downloaded, request)
done = False
while done is False:
  status, done = downloader.next_chunk()
  if status:
      print("Download %%%d%%." % int(status.progress() * 100))
  print("Download Complete!")

downloaded.seek(0)

if debug:
    print('Downloaded file contents are: {}'.format(downloaded.read()))
    
with open(download_location, 'wb') as f:
    f.write(downloaded.read())
    
print ('File written to {}'.format(download_location))