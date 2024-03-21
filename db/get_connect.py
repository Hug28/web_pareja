import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

def get_conn():
    try:
        conn = psycopg2.connect(database=os.getenv("DATABASE"), user=os.getenv("USER_DB"), password=os.getenv("PASSWORD_DB"))
        return conn
    except Exception as e:
        print(e)
        return "Ocurrio un error con la conexion"
    