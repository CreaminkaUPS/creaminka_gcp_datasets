# Importamos los módulos necesarios
from google.cloud import storage
import os

def upload_folder_to_bucket(folder_path, bucket_name, client_json):
    # Cargamos las credenciales desde el archivo JSON
    storage_client = storage.Client.from_service_account_json(client_json)
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file!=".gitkeep":
                print(root, file)
                file_path = os.path.join(root, file)
                # Obtenemos el bucket
                bucket = storage_client.bucket(bucket_name)
                # Subimos el archivo ZIP al bucket
                bucket.blob(file).upload_from_filename(file_path)


def download_and_unzip_file(bucket_name,path_to, client_json):
    # Cargamos las credenciales desde el archivo JSON
    storage_client = storage.Client.from_service_account_json(client_json)
    
    # Obtenemos el bucket
    bucket = storage_client.bucket(bucket_name)
    # Obtiene todos los archivos del bucket
    blobs = bucket.list_blobs()

    # Imprime el nombre de cada archivo
    for blob_n in blobs:
        print(blob_n.name)
        # Descargamos el archivo ZIP del bucket
        blob = bucket.blob(blob_n.name)
        blob.download_to_filename(os.path.join(path_to,blob_n.name))