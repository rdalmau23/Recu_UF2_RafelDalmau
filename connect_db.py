import psycopg2

def connection_db():
    conn = psycopg2.connect(
        database="db",
        password="1234",
        user="postgres",
        host="localhost",
        port="8000"
    )
    print("Conexió a la bbdd")
    return conn