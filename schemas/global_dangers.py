async def global_danger_entity(global_danger: dict) -> dict:
    return {
        'name': global_danger['name'],
        'description': global_danger['description'],
        'link': global_danger['link'],
    }
