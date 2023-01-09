# Herramienta de descarga
## Configuración de entorno virtual
Escribe el siguiente comando para crear un entorno virtual llamado "creaminka_datasets" con Python 3.9:
```bash
conda create --name creaminka_datasets python=3.9
```
Activa el entorno virtual con el comando:
```bash
conda activate creaminka_datasets
```
Instala las librerías necesarias con el comando:
```bash
conda install google-cloud-storage
```

## Subir archivos al repositorio
Para ejecutar el código, asegúrate de tener el entorno virtual activado y la llave de cliente del bucket con los accesos adecuados, luego escribe:
```bash
python "Script Upload.py"
```

## Descargar archivos del repositorio
Para ejecutar el código, asegúrate de tener el entorno virtual activado y la llave de cliente del bucket con los accesos adecuados, luego escribe:
```bash
python "Script Download.py"
```