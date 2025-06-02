from database import connect_db

from user import users_schema

conn = connect_db.connection_db()

def get_users():
    cursor = conn.cursor()
    sql = "SELECT * FROM users"
    cursor.execute(sql)
    result = cursor.fetchall()
    return users_schema(result)


