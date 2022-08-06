import requests

class monster_adapter():
    def __init__(self) -> None:
        pass

    @classmethod
    def get_all_monsters(cls):
        url = "https://www.dnd5eapi.co/api/monsters"
        return requests.get(url=url).json()

    @classmethod
    def get_monster(cls, name):
        url = f"https://www.dnd5eapi.co/api/monsters/{name}"
        return requests.get(url=url).json()