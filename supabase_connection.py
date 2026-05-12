from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import Session
from sqlalchemy.dialects.postgresql import insert
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv("chiavi.env")

USER = os.getenv("DB_USER")
PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("DB_HOST")
PORT = os.getenv("DB_PORT")
DBNAME = os.getenv("DBNAME")


DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

engine = create_engine(DATABASE_URL)


path_pc_desktop = r'C:\GianC\expense\contabilita\file_da_caricare.csv'
path_mac = r'/Users/gianluigimosti/WorkPlace/PersonalRepo/file_da_caricare.csv'

df = pd.read_csv(path_mac, sep=",")


metadata = MetaData()
table = Table("rawData", metadata, autoload_with=engine)

records = df.to_dict(orient="records")
ops = insert(table).values(records)

ops = ops.on_conflict_do_nothing(
    index_elements=[col for col in df.columns]
)

with engine.begin() as conn: 
    
    conn.execute(ops)