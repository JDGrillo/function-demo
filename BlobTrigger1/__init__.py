import azure.functions as func
from io import BytesIO

from BlobTrigger1.helpers import download_blob, upload_new_blob, convert_filename, read_certain_csv

def main(myblob: func.InputStream):
    downloaded_blob = download_blob(myblob)
    stream = BytesIO()
    downloaded_blob.readinto(stream)
    stream.seek(0)
    
    df = (read_certain_csv(stream))
    data = BytesIO(df.to_csv(index=False).encode())

    new_filename = convert_filename(myblob.name[myblob.name.find('/')+1:])
    upload_new_blob(data, new_filename)
