def user_schema(user) -> dict:
    response = {"id": user[0],
                "username": user[1],
                "lastname": user[2],
                "email": user[3],
                "decription": user[4],
                "curs": user[5],
                "year": user[6],
                "direction": user[7],
                "postal_code": user[8],
                "password": user[9]
                }
    return response


def users_schema(users) -> list[dict]:
    response = [user_schema(user) for user in users]
    return response