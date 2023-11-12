def user_entity(user: dict) -> dict:
    return {
        "user_id": user["user_id"],
        "username": user["username"],
        "email": user["email"],
        "full_name": user["full_name"],
        "phone_number": user["phone_number"],
    }


def users_entitys(entity) -> list:
    return [user_entity(user) for user in entity]
