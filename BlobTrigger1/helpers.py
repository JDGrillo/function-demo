import os
import pandas as pd
from azure.storage.blob import BlobServiceClient, ResourceTypes
from dotenv import load_dotenv
load_dotenv()

ACCOUNT_KEY = os.environ["ACCOUNT_KEY"]
ACCOUNT_NAME = os.environ["ACCOUNT_NAME"]
SOURCE_CONTAINER = os.environ["SOURCE_CONTAINER"]
DESTINATION_CONTAINER = os.environ["DESTINATION_CONTAINER"]

source_blob_service_client = BlobServiceClient(
    account_url=f'https://{ACCOUNT_NAME}.blob.core.windows.net/', credential=ACCOUNT_KEY)
source_container_client = source_blob_service_client.get_container_client(
    SOURCE_CONTAINER)

destination_container_client = source_blob_service_client.get_container_client(
    DESTINATION_CONTAINER)

def download_blob(myblob):
    source_blob = source_container_client.get_blob_client(myblob.name)
    download_blob = source_container_client.download_blob(source_blob.blob_name[source_blob.blob_name.find('/')+1:])
    return download_blob

def upload_new_blob(stream, name):
    destination_container_client.upload_blob(data=stream, name=name, blob_type="BlockBlob")

def convert_filename(filename):
    for key in conversion_dict:
        if filename.startswith(key):
            return filename.replace(key, conversion_dict[key])
    return filename


def read_certain_csv(stream):
    return pd.read_csv(stream, usecols=important_cols)

conversion_dict = {
    "My_File_Name": "Cool_File",
    "Sprint": "Iteration"
}

important_cols = ['ID', 'Work Item Type', 'Step Action']