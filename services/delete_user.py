from database import connect_db


conn = connect_db.connection_db()

def delete_user():
    cur = conn.cursor()
    query = "DELETE FROM users WHERE user_id = %s;"
    cur.execute(query, (user_id))
    conn.commit()
    cur.close()
    conn.close()
