# from urllib import response
# import requests
# from pprint import pprint

# # let's get the JSON from this endpoint using urllib
# url = "https://www.dnd5eapi.co/api/monsters/orc"

# response = requests.get(url=url)
# pprint(response.json())

from monster_adapter import monster_adapter
from pprint import pprint

pprint(monster_adapter.get_all_monsters())