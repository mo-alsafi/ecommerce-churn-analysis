from pathlib import Path
import pandas as pd 
from sqlalchemy import create_engine


BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "E Commerce Dataset.xlsx"

df = pd.read_excel(DATA_PATH, sheet_name=1)
print(df.head())

DB_USER = "root"
DB_PASS = "root123"
DB_PORT= "3306"
DB_HOST = "localhost"
DB_NAME = "ecommerce-churn-data"

conn_string = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(conn_string)

df.to_sql(
    name="ecommerce_churn",
    if_exists='replace',
    con=engine,
    index=False
)

print("## Insgistioned to sql")