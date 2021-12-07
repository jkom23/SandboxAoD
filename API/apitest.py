import requests
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
ENDPOINT = "tepig"
API_KEY = "abcd1234"

payload = {'key': API_KEY, 'q': "X"}

response = requests.get(BASE_URL+ENDPOINT) #params not always needed
if response.ok:
    data = response.json()
    print(data.keys())
    print(data["types"])
else:
    print(response.status_code, response.text)

