import csv

#this method inputs the csv file and will find the average speed of all digimon by iterating through the csv
#each line it will the current speed to a total speed counter and add 1 to the total digimon counter
#then it returns the average
def avgSpeed(filePath):
    numDigimon=0
    speedDigimon=0
    with open(filePath, "r") as file:
        data = csv.reader(file)
        next(data)
        for i in data:
            i[12]=int(i[12])
            #turns data into ints so we can average
            numDigimon+=1
            speedDigimon+=i[12]
    return (speedDigimon/numDigimon)



#this method will input a csv file, an characteristic of a digimon, and a value for that characteristic
#it will then return how many digimon in the csv have that characteristic with that specific value
def countDigimon(filePath,characteristic,value):
    counter=0
    with open(filePath, "r") as file:
        data = csv.DictReader(file)
        for i in data:
            if i[characteristic]==value:
                counter+=1
            #if the row has a characteristic value equal to the desired characteristic value, then add 1 to counter
    return counter


#this method will input a csv file, a desired number of digimon on the team, a desired attack total, and a desired memory total
#it will find a team that meets those specifications and return the team roster (with team info) as a dictionary
def findDigimonTeam(filePath, desiredNumDigimon, desiredAttackTotal, desiredMemoryTotal):
    myTeam={"Total Attack Power":{},"Total Memory":{}, "Number of Digimon on Team":{}}
    #if the user inputted more than 3 digimon desired, we need to set it to 3 because 3 digimon is the maximum number per team
    if desiredNumDigimon>3:
        desiredNumDigimon=3
    numDigimon=0
    totalAttackPower=0
    totalMemoryUsed=0
    atkPerDigimon=desiredAttackTotal/desiredNumDigimon
    memPerDigimom=desiredMemoryTotal/desiredNumDigimon
    with open(filePath, "r") as file:
        data = csv.reader(file)
        next(data)
        for i in data:
            #make our data ints
            i[9]=int(i[9])
            i[5]=int(i[5])
            #if the specific digimon has suffienct attack power, not too much memory, and we havent filled a team roster yet
            if (i[9] >= atkPerDigimon) and (i[5]<=memPerDigimom) and (numDigimon<=(desiredNumDigimon-1)):
                numDigimon+=1
                totalAttackPower+=i[9]
                totalMemoryUsed+=i[5]
                myTeam["Teammate #"+str(numDigimon)]={"Digimon": i[1], "ID": i[0], "Attack Power":i[9], "Memory":i[5]}
                #add this digimon to our team roster and include the specific info for that digimon in our table
        myTeam["Total Attack Power"]=totalAttackPower
        myTeam["Total Memory"]=totalMemoryUsed
        myTeam["Number of Digimon on Team"]=numDigimon
    return myTeam

print(avgSpeed("Datasets/digimon.csv"))
#how many digimon have a type of vaccine type
print(countDigimon("Datasets/digimon.csv","Type","Vaccine"))
#how many digimon have a attribute of Fire
print(countDigimon("Datasets/digimon.csv","Attribute","Fire"))
#I have set the parameters to be 3 digimon, 300 minimum attack power, and 15 maximum memory (the lab specifications), but we could change these parameters depending on the situation
print(findDigimonTeam("Datasets/digimon.csv",3,300,15))