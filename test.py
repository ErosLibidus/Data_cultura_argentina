import glob
import os
from upload_db import baseDeDatos
from consumir import descargarData
import pandas as pd
import subprocess


def _archivos(path):
    dire = path + "/*/*/*/*"
    fiches = glob.glob(dire)
    archivos = []
    directorios = []
    for name in fiches:
        arch = os.path.basename(name)
        if arch[-4:] == ".csv":
            archivos.append(arch)
            directorios.append(name)
    return archivos, directorios

# arc, dire = _archivos(os.getcwd())
# print(arc)
if os.path.exists("./archivos/ca"):
    print("caca")