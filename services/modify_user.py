from database import connect_db

from user import users_schema

conn = connect_db.connection_db()

def modify_user():
    cursor = conn.cursor()
    sql= """
    UDATE SET user_lastname = $s,
    """
    values = (lastname, direction )

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()