from database import connect_db

conn = connect_db.connection_db()

def insert_user(username, lastname, year, email, direction, postal_code, curs, description):
    cur = conn.cursor()
    sql = """
        INSERT INTO users ( user_name, user_lastname , user_year, user_email, user_curs, user_direction, user_description)
        VALUES ( %s, %s, %s, %s)
        """
    values = (username, lastname, year, email, direction, postal_code, curs, description)

    cur.execute(sql, values)
    conn.commit()



