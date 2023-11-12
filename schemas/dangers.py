async def danger_entity(danger: dict) -> dict:
    return {
        'user_id': danger['user_id'],
        'name': danger['name'],
        'description': danger['description'],
        'coordinates': danger['coordinates'],
        'date_time': str(danger['date_time']),
    }


async def danger_and_user_entity(danger: dict, user: dict) -> dict:
    return {
        'user_id': danger['user_id'],
        'name': danger['name'],
        'description': danger['description'],
        'coordinates': danger['coordinates'],
        'date_time': str(danger['date_time']),
        'username': user['username'],
    }
