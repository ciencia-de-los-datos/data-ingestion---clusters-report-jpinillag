"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd

def ingest_data():

    df = pd.read_fwf("clusters_report.txt",skiprows = 4,names = ["cluster", "cantidad_de_palabras_clave","porcentaje_de_palabras_clave", "principales_palabras_clave"])
    df.fillna(method="ffill", inplace=True)
    df = df.groupby(["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave"])["principales_palabras_clave"].apply(' '.join).reset_index()
    df["cluster"]=df["cluster"].apply(lambda x: int(x))
    df["cantidad_de_palabras_clave"]=df["cantidad_de_palabras_clave"].apply(lambda x: int(x))
    df["porcentaje_de_palabras_clave"]=df["porcentaje_de_palabras_clave"].apply(lambda x: x.replace(",", "."))
    df["porcentaje_de_palabras_clave"]=df["porcentaje_de_palabras_clave"].apply(lambda x: x[:len(x)-2])
    df["porcentaje_de_palabras_clave"]=df["porcentaje_de_palabras_clave"].apply(lambda x: float(x))
    df["principales_palabras_clave"]=df["principales_palabras_clave"].apply(lambda x: str(x))
    return df
