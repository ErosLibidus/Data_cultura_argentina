from fuzzywuzzy import process
import pandas as pd

def limpiar_acentos(text):
	acentos = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'Á': 'A', 'E': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U'}
	for acen in acentos:
		if acen in text:
			text = text.replace(acen, acentos[acen])
	return text


def columns_norm(df):

    correctos = ['cod_localidad', 'id_provincia', 'id_departamento', 
                'categoria','provincia', 'departamento', 
                'localidad', 'nombre', 'direccion', 
                'cp', 'web', 'latitud', 
                'longitud', 'tipo_latitud_longitud', 'fuente',
                'año_actualizacion']

    for i in df.columns:
        b = process.extractOne(i,correctos)
        if b[1] > 70 and i != "Subcategoria" and i != "subcategoria":
            df.rename(columns={i:b[0].lower()}, inplace=True)
        else:
            c = i.lower()
            df.rename(columns={i:c}, inplace=True)
        if i == "direccion":
            df.rename(columns={i:"domicilio"}, inplace=True)
        
        a = limpiar_acentos(i)
        df.rename(columns={i:a.lower()}, inplace=True)

    if "telefono" not in df.columns and "mail" not in df.columns:
        df["telefono"] = 0
        df["mail"] = "s/d"
    
    return df