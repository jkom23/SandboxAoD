story = {
  "title": "Invisible Planets",
  "author": "Hao Jingfang",
  "published": 2013
}

print(story['author'])
story["words"] = 6359
story["title"] = "Folding Beijing"
story["translator"] = "Ken Liu"
del story['published']
print(story)

for k, v in story.items():
	print("Key:", k)
	print("Value:", str(v))

bakery = ["Brownie", "hello", "CupCake", "Brownie", "Cupcake", "Cookie", "Cookie"]

def count(list):
  newDict = {}
  for i in list:
      if i in newDict:
        newDict[i]=newDict[i]+1
      else:
        newDict[i]=1
  print(newDict)


count(bakery)


amazonPurchase = {
  "item": "TV",
  "Seller": "Samsung",
  "Price": 999
}

def dictToList(dict):
    list=[]
    for k, v in dict.items():
        list.append(k)
        list.append(v)
    print(list)

dictToList(amazonPurchase)

testString= "applesauce"

def stringToDict(string):
    n=0
    stringDict = {}
    for i in string:
      n+=1
      nth=str(n)
      stringDict[("#"+nth+" character")]=i
    print(stringDict)
