from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session
import pandas as pd
# from dotenv import load_dotenv

# load_dotenv(".env")

USER = "#############"
PASSWORD = "#############"
HOST = "#############"
PORT = "#############"
DBNAME = "#############"


DATABASE_URL = f"postgresql+psycopg2://{USER}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}?sslmode=require"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

with Session(engine) as session: 

    output = session.execute(text("""SELECT * FROM movimenti_conto"""))

    result = output.fetchall()

    print(pd.DataFrame(result))


