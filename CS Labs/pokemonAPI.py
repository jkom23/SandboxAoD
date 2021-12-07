from pip._vendor import requests
import csv
BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
ENDPOINT = "greninja"


class Pokemon:
  def __init__(self, id, name, height, weight, type1, type2):
        self.id = id
        self.name=name
        self.height=height
        self.weight=weight
        self.type1=type1
        self.type2=type2

  def __str__(self):
    return f"{self.id},{self.name},{self.height},{self.weight},{self.type1},{self.type2}"
    
def cleanDataset():
  with open("pokemon_mess.csv", "r") as file1, open("pokemon_clean.csv", "w") as file2:
    data = csv.DictReader(file1)
    file2.write("id, name, height, weight, type1, type2\n")
    for i in data:
      endpoint=(i["name"]).lower()
      #set endpoint as current name (made lowercase)
      pokeData = requests.get(BASE_URL + endpoint)
        #get info for that pokemon
      if pokeData.ok:
        pokeStats = pokeData.json()
        #if request is ok then get json object data
        if len(pokeStats["types"]) > 1:
          #if two types, then add both types (and other relevant info) to the new csv
          fixedData = Pokemon(pokeStats["id"], pokeStats["name"], pokeStats["height"], pokeStats["weight"], pokeStats["types"][0]["type"]["name"], pokeStats["types"][1]["type"]["name"])
        else:
          #if one type, add that type and the other stats to new csv
          fixedData = Pokemon(pokeStats["id"], pokeStats["name"], pokeStats["height"], pokeStats["weight"], pokeStats["types"][0]["type"]["name"],"none")
        file2.write(str(fixedData)+"\n")
      else:
        print(pokeData.status_code, pokeData.text)  
cleanDataset()