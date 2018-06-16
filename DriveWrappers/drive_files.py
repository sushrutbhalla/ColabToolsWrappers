from google.colab import auth
from googleapiclient.discovery import build
import io , requests, os
import sys
from googleapiclient.discovery import build

import tensorflow as tf
import timeit

from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from google.colab import auth
from oauth2client.client import GoogleCredentials

class drive_files:
	def __init__(self):
		#setup access to google drive from colab
		auth.authenticate_user()
		self.drive_service = build('drive', 'v3')

		config = tf.ConfigProto()
		config.gpu_options.allow_growth = True

		# Authenticate and create the PyDrive client.
		auth.authenticate_user()
		gauth = GoogleAuth()
		gauth.credentials = GoogleCredentials.get_application_default()
		self.drive = GoogleDrive(gauth)

	def get_drive(self):
		return self.drive 
	def get_drive_service(self):
		return self.drive_service
		
	def list_files(self):
		file_list = self.drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
		for file1 in file_list:
			print('title: %s, id: %s' % (file1['title'], file1['id']))

	def download_file(self, file_id, download_location):
		'''Use this function to download files which aren't utf-8 encoded.
		This function dowloads the file (file_id) and writes it to a location file
		'''
		from googleapiclient.http import MediaIoBaseDownload
		request = self.drive_service.files().get_media(fileId=file_id)
		downloaded = io.BytesIO()
		downloader = MediaIoBaseDownload(downloaded, request)
		done = False
		while done is False:
		  status, done = downloader.next_chunk()
		  if status:
		      print("Download %%%d%%." % int(status.progress() * 100))
		  print("Download Complete!")

		downloaded.seek(0)		    
		with open(download_location, 'wb') as f:
		    f.write(downloaded.read())
		    
		print ('File written to {}'.format(download_location))
		return downloaded

