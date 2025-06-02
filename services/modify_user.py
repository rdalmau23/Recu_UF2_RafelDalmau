from database import connect_db

conn = connect_db.connection_db()

def modify_user(lastname, direction):
    cursor = conn.cursor()
    sql= """
    UDATE SET user_lastname = $s, user_direction WHER user_id = $s
    """
    values = (lastname, direction )

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()