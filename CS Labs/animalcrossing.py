from pip._vendor import requests
import csv
BASE_URL="https://hm-cs.herokuapp.com"
ENDPOINT="/sockOptions"
API_KEY = "ArtOfDataKEY123"
#payload setup and imports



def generateCSV():
    #make API requests and generate a CSV
    n=0
    payload= {'key': API_KEY, 'idx': n}
    with open("Datasets/animalCrossing.csv", "w") as file1:
        response = requests.get(BASE_URL+ENDPOINT,params=payload)
        response_text=response.text[1:]
        while response.ok:
            #while no API request errors, continue to change payload and get new socks items
            file1.write(response_text+"\n")
            n+=1

            payload= {'key': API_KEY, 'idx': n}
            #change our payload as we iterate through the API until we get errors and no more socks are left
            response = requests.get(BASE_URL+ENDPOINT,params=payload)
            response_text=response.text
            #turn this get object into a text object that we write to our csv


def sockTypeVariations():
    with open("Datasets/animalCrossing.csv", "r") as file2:
        data = list(csv.reader(file2))[1:]
        sockOptions={}
        #open the generated csv and make a table that will store the sock types
        for i in data:
            if i[0] not in sockOptions.keys():
                sockOptions[i[0]]=1
            else:
                sockOptions[i[0]]+=1
        #iterate through the csv, if the sock type isnt in the csv then add its type to the csv
        #if the sock type is in the csv then add 1 to that sock type value

        mostNumVariations = max(sockOptions.values())
        sockTypeWithMostVariations = []
        #find the largest value in the csv, the sock type with those values have the most possible variations
        #we will make a new list that has all of these sock types

        for keys in sockOptions:
            if sockOptions.get(keys)==mostNumVariations:
                sockTypeWithMostVariations.append(keys)
        #iterate through the sock types, if their value is the same as the max variation value, then add it to our special list
        #if not, then it doesnt have the most variations and doesnt go in the special list
    print(sockTypeWithMostVariations)


def sockColorOptions():
    with open("Datasets/animalCrossing.csv", "r") as file3:
        data = csv.reader(file3)
        colorOptions = {}
        next(data)
    #iterate through the generated csv and check for all the sock colors
    #if the sock color1 isnt in our color options dictionary then we add it, if it is there then increase our count of that color by 1
        for i in data:
            if i[5] not in colorOptions.keys():
                colorOptions[i[5]] = 1
            else:
                colorOptions[i[5]] += 1
    #repeat this process for color 2
            if i[6] not in colorOptions.keys():
                colorOptions[i[6]] = 1
            else:
                colorOptions[i[6]] += 1
    #if color 1 and color 2 are the same then remove one instance of it so we dont double count
            if i[5] == i[6]:
                colorOptions[i[6]] -=1 

        print(colorOptions)




generateCSV()
sockTypeVariations()
sockColorOptions()

#these functions give us our answers


