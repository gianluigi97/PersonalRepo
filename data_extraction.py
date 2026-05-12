import pandas as pd 
import os 
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

def format_number(number: str) -> str:

    if number.count(".") > 1:

        k, u, d = number.split(".")

        return f'{k+u}.{d}'
    
    else: 
        return number
        

def file_prep(file_path: str) -> pd.DataFrame:
    col_name = {
        'Data Registrazione' : 'd_registrazione', 
        'Data valuta' : 'd_valuta',
        'Descrizione' : 'descrizione',
        'Importo (EUR)' : 'importo'
    }
    dati = pd.read_csv(file_path, sep=";", dtype=str)
    dati = dati.drop(columns=["Unnamed: 4"]).rename(columns=col_name)
    dati['descrizione'] = dati['descrizione'].apply(lambda x: " ".join(x.split()))
    dati['importo'] = dati['importo'].apply(lambda x: x.replace(",", "."))
    dati['importo'] = dati['importo'].apply(format_number)


    return dati

path = r'C:\GianC\expense\contabilita\estratto_unicredit'
file = '20260504.csv'

df = file_prep(os.path.join(path, file))

# print(df)

file = df.to_csv("file_da_caricare.csv", index=False)