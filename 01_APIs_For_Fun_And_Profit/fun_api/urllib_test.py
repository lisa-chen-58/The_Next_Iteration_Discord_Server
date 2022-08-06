from urllib import request
import json
from pprint import pprint
# let's get the JSON from this endpoint using urllib
url = "https://www.dnd5eapi.co/api/monsters/orc"

response = request.urlopen(url)
data = response.read()
decoded_data = data.decode()
dict_data = json.loads(decoded_data)

pprint(dict_data)
print(type(dict_data))
print(dict_data['armor_class'])