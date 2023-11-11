def userEntity (user: dict) -> dict:
    return {
        'username': str(user['username']),
        'email': str(user['email'])
    }

def userEntity(entity) -> list:
    return [userEntity(user) for user in entity]