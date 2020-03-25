import os
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
from google.colab import auth
from oauth2client.client import GoogleCredentials
import argparse

import time
import datetime

def export_folder(filename, out_drive_folder_id):
  '''Export colab folder to drive folder '''
  file = drive.CreateFile({"parents": [{"kind": "drive#fileLink",
                                        "id": out_drive_folder_id}]})
  # Zip folder
  #!echo '/content/sample_data'
  new_name = get_filename()
  cmd = "zip -r out-{}.zip ".format(new_name) + filename
  returned_value = os.system(cmd)
  print('returned value:', returned_value)

  # Export file
  file.SetContentFile('out-{}.zip'.format(new_name))#
  file.Upload()
  #!rm out.zip
  return True

def get_filename():
  ts = time.time()
  st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M')
  return st

def upload_weight2drive(filename, out_drive_folder_id):
  # Create & upload a text file.
  # uploaded = drive.CreateFile({})
  uploaded = drive.CreateFile({"parents": [{"kind": "drive#fileLink",
                                        "id": out_drive_folder_id}],
                               'title': filename.split("/")[-1]})
  uploaded.SetContentFile(filename)
  uploaded.Upload()
  print('Uploaded file with ID {}'.format(uploaded.get('id')))

if __name__ == '__main__':
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-f", "--filename", required=True, help="Filename for upload", type=str)
    args = vars(ap.parse_args())

    filename = args['filename']
    out_drive_folder_id = os.environ.get('OUTPUT_FOLDER_ID')
    # print("Exporting to Drive: {} {}".format(filename, out_drive_folder_id)

    # Authenticate and create the PyDrive client.
    # This only needs to be done once per notebook.
    auth.authenticate_user()
    gauth = GoogleAuth()
    gauth.credentials = GoogleCredentials.get_application_default()
    drive = GoogleDrive(gauth)

    upload_weight2drive(filename, out_drive_folder_id)
