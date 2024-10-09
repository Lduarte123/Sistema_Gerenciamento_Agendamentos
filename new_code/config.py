import psycopg2
from psycopg2 import OperationalError

def create_connection():
    try:
        connection = psycopg2.connect(
            user="postgres",
            password="postgres",
            host="localhost",
            port="5432",
            database="senac"
        )
        print("Conexão com PostgreSQL bem-sucedida")
        return connection
    except OperationalError as e:
        print(f"O erro '{e}' ocorreu")
        return None

