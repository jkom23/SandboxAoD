'''
Jack Komaroff
CS Lab: Reading Files Practice
'''

import csv
#import our csv module

#how to find the average bill length of a penguin species by reading a csv and iterating through the data
def penguinAvgBillLength(filepath):
#find the average bill length of each species of penguin
  with open(filepath, "r") as file:
    #open up our csv file
    table={}
    #make an empty table to start
    data = csv.reader(file)
    #set up our iterable object
    next(data)
    #skip headers
    for i in data:
    #iterate through the data
        if i[0] not in table:
        #if new species
          table[i[0]]={}
          #add the species as a subdictionary to the table dict
          table[i[0]]["Total Bill Length"]=0
          #set a key in the subdictionary for total bill length
          table[i[0]]["Number of Penguins"]=0
          #set a key in the subdictionary for number of penguins
        if i[0] in table:
          #if species in table
          if i[2]=="":
          #if no length given
            i[2]=0
            #set length to 0
          else:
            #if length is given
            i[2] = float(i[2])
            #make length a float
            table[i[0]]["Total Bill Length"]+=i[2]
            #add the length to our total bill length
            table[i[0]]["Number of Penguins"]+=1
            #increase number of penguins by 1
    for species in table:
        table[species]["Average Bill Length"]=(table[species]["Total Bill Length"])/(table[species]["Number of Penguins"])
        #calculate our average bill length 
  print(table)
  #print our table dictionary


def penguinAvgMass(filepath):
  #find the average mass of each species of penguin
  with open(filepath, "r") as file:
    #open up our csv file
    table={}
    #make an empty table to start
    data = csv.reader(file)
    #set up our iterable object
    next(data)
    #skip headers
    for i in data:
    #iterate through data
        if i[0] not in table:
        #if the species is not in the table
          table[i[0]]={}
          #add species as a subdictionary to the table dict
          table[i[0]]["Total Mass"]=0
          #set a key in the subdictionary for total mass
          table[i[0]]["Number of Penguins"]=0
          #set a key in the subdictionary for number of penguins
        if i[0] in table:
          #if species in table
          if i[5]=="":
          #if no mass given
            i[5]=0
            #set mass to 0
          else:
            i[5] = float(i[5])
            #make mass a float
            table[i[0]]["Total Mass"]+=i[5]
            #add the mass to our total
            table[i[0]]["Number of Penguins"]+=1
            #increase number of penguins by 1
        table[i[0]]["Average Mass"]=(table[i[0]]["Total Mass"])/(table[i[0]]["Number of Penguins"])
        #calculate our average mass  
  print(table)
  #print our table dictionary


def chinstrapOnDream(filepath):
#find how many Chinstrap penguins on Dream Island
  numChinstrapOnDream=0
  #set our counter to 0
  with open(filepath, "r") as file:
    #open up our csv file
    data = csv.reader(file)
    #set up our iterable object
    next(data)
    #skip headers
    for i in data:
    #iterate through data
        if i[0]=="Chinstrap" and i[1]=="Dream":
        #if the specific penguin is a chinstrap penguin AND also on Dream island
            numChinstrapOnDream+=1
            #increase counter by 1
  print(numChinstrapOnDream)
  #print out our counter of the number of chinstrap penguins on dream island


penguinAvgBillLength("Datasets/penguins.csv")
penguinAvgMass("Datasets/penguins.csv")
chinstrapOnDream("Datasets/penguins.csv")

#call our methods to read and analyze the csv

'''
Answers

1. Which species of penguins has the longest bills (on average)?

After running method "penguinAvgBillLength()", we can easily read our nested dictionary to see that Chinstrap penguins have the longest bills.
They have an average length of 48.83 millimeters.

2. Which species of penguins is the most massive (on average)?

After running method "penguinAvgMass()", we can easily read our nested dictionary to see that Gentoo penguins are the most massive.
They have an average mass of 5076.02 grams.

3. How many Chinstrap penguins are on Dream island?

After running method "chinstrapOnDream()", we can see that there are 68 Chinstrap penguins on Dream Island.
'''