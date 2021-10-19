import csv

def avgSpeed(filePath):
    numDigimon=0
    speedDigimon=0
    with open(filePath, "r") as file:
        data = csv.reader(file)
        next(data)
        for i in data:
            i[12]=float(i[12])
            numDigimon+=1
            speedDigimon+=i[12]
    return (speedDigimon/numDigimon)


def countDigimon(filePath,attribute,value):
    counter=0
    with open(filePath, "r") as file:
        data = csv.DictReader(file)
        for i in data:
            if i[attribute]==value:
                counter+=1
    return counter

print(avgSpeed("Datasets/digimon.csv"))
print(countDigimon("Datasets/digimon.csv","Type","Vaccine"))