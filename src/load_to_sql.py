import os
import pandas as pd 
from pathlib import Path
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "E Commerce Dataset.xlsx"

df = pd.read_excel(DATA_PATH, sheet_name=1)
print(df.head())

DB_USER, DB_PASS = os.getenv("DB_USER"), os.getenv("DB_PASS")
DB_NAME, DB_HOST, DB_PORT = os.getenv("DB_NAME"), os.getenv("DB_HOST"), os.getenv("DB_PORT")

conn_string = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(conn_string)

df.to_sql(
    name="ecommerce_churn",
    if_exists='replace',
    con=engine,
    index=False
)

print("## Insgistioned to sql")