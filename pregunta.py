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

    df = pd.read_fwf("clusters_report.txt",skiprows = 4,names = ["cluster", "cantidad _de_palabras_clave","porcentaje_de_palabras_clave", "principales_palabras_clave"])
    df.fillna(0, inplace=True)
    i=1
    while i < len(df["cluster"]):
        if(df["cluster"].iloc[i]<df["cluster"].iloc[i-1]):
            df["cluster"].iloc[i]=df["cluster"].iloc[i-1]
        if(df["cantidad _de_palabras_clave"].iloc[i]==0):
            df["cantidad _de_palabras_clave"].iloc[i]=df["cantidad _de_palabras_clave"].iloc[i-1]
        if(df["porcentaje_de_palabras_clave"].iloc[i]==0):
            #print("es 0")
            df["porcentaje_de_palabras_clave"].iloc[i]=df["porcentaje_de_palabras_clave"].iloc[i-1]
        i+=1
    
    df = df.groupby(["cluster","cantidad _de_palabras_clave","porcentaje_de_palabras_clave"])["principales_palabras_clave"].apply(' '.join).reset_index()

    return df
