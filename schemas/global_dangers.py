async def global_danger_entity(danger: dict) -> dict:
    return {
        "name": danger["name"],
        "description": danger["description"],
        "link": danger["link"],
    }
