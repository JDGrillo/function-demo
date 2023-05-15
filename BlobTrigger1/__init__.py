import azure.functions as func
from io import BytesIO

from BlobTrigger1.helpers import download_blob, upload_new_blob, convert_filename

def main(myblob: func.InputStream):
    downloaded_blob = download_blob(myblob)
    stream = BytesIO()
    downloaded_blob.readinto(stream)
    stream.seek(0)

    new_filename = convert_filename(myblob.name[myblob.name.find('/')+1:])
    upload_new_blob(stream, new_filename)
