import csv
import time
import os
from datetime import date
import requests
import pandas as pd


def descargarData(url):

    pos = url.find("download")
    nom = url[pos + 9:-4]
    fecha = date.today()
    nom_direc = "./archivos/{}".format(nom)
    nom_direc2 = str(fecha.year) + "-" + str(fecha.strftime("%B"))


    r = requests.get(url)
    data_cv = csv.reader(r.content.decode('utf-8').splitlines(),delimiter=',')
    df = pd.DataFrame(data_cv)
    df = df.set_axis(df.iloc[0], axis = 1)
    df = df.drop(0 , axis = 0)


    if os.path.exists(nom_direc):
        if nom_direc2 in os.listdir(nom_direc):
            pass
        else:
            os.mkdir(nom_direc + "/" + nom_direc2)
    else:
        os.mkdir(nom_direc)
        os.mkdir(nom_direc + "/" + nom_direc2)
    
   
    

    nom2 = nom + "-" + str(fecha) + ".csv"
    direc = nom_direc + "/" + nom_direc2
    # path_ = nom_direc + "/" + nom_direc2 + "/" + nom2
    # if nom2 in os.listdir(nom_direc + "/" + nom_direc2):
    #     df2 = pd.read_csv(path_)
    #     if df2.shape == df.shape:
    #         os.remove(path_)
    #         df2.to_csv(path_, index=False)

    if len(os.listdir(nom_direc + "/" + nom_direc2)) > 0:
        for i in os.listdir(direc):
            os.remove(direc + "/" + i)
        df.to_csv(nom_direc + "/" + nom_direc2 + "/" + nom2, index=False)
    else:
        df.to_csv(nom_direc + "/" + nom_direc2 + "/" + nom2, index=False)
        