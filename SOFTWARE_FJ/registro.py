import logging
import os

#RUTA DE LA CARPETA DEL PROYECTO
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


#CREAR CARPETA DE LOGS
CARPETA_LOGS = os.path.join(BASE_DIR, "logs")
os.makedirs(CARPETA_LOGS, exist_ok=True)

#CONFIGURAR EL REGISTRO
logger = logging.getLogger("SoftwareFJ")
logger.setLevel(logging.DEBUG)

#ARCHIvO PARA GUARDAR LOS REGISTROS
ruta_archivo = os.path.join(CARPETA_LOGS, "software_fj.log")
archivo = logging.FileHandler(ruta_archivo, mode="a", encoding="utf-8")

#FORMATO DE LOS MENSAJES
formato = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
archivo.setFormatter(formato)

#CONECTAR EL ARCHIVO AL LOGGER
logger.addHandler(archivo)