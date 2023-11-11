def user_entity(user: dict) -> dict:
    return {
        '_id': str(user['_id']),
        'username': user['username'],
        'email': user['email'],
        'password': user['password'],
    }


def users_entitys(entity) -> list:
    return [user_entity(user) for user in entity]
