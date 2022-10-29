import glob
import os
from upload_db import baseDeDatos, comparar_tablas
from consumir import descargarData
from normalizar import columns_norm
import pandas as pd
import subprocess
import requests
from bs4 import BeautifulSoup
from pwn import *


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


if __name__ == "__main__":
    if os.path.exists("archivos"):
        pass
    else:
        os.mkdir("archivos")
        
    p1 = log.progress("Cultura Argentina")
    page = requests.get('https://datos.cultura.gob.ar/dataset/espacios-culturales-argentina-sinca/archivo/01c6c048-dbeb-44e0-8efa-6944f73715d7')
    bsoup = BeautifulSoup(page.content, 'html.parser')
    link_list = bsoup.find_all('a')
    p1.status("Consumiendo data")
    for link in link_list:
        link2 = link.attrs["href"]
        if "https" in link2:
            if "cine" in link2 or "museo" in link2 or "biblioteca" in link2:
                descargarData(link2)

    
    archivos, directorios = _archivos(os.getcwd())
    subprocess.run(["./postgres.sh"])
    for i in directorios:
        p1.status("Subiendo data a base de datos")
        df = pd.read_csv(i)
        df = columns_norm(df)
        if "cine" in i:
            if comparar_tablas(df,"cines") == True:
                baseDeDatos(df, "cines")
        elif "museo" in i:
            if comparar_tablas(df,"museos") == True:
                baseDeDatos(df, "museos")
        elif "biblioteca" in i:
            if comparar_tablas(df,"bibliotecas") == True:
                baseDeDatos(df, "bibliotecas")
    p1.status("Finalizado!")