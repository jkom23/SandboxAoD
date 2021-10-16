import csv

'''
with open("Datasets/favorite_colors.csv", "w") as f:
  print(f)

with open("Datasets/favorite_colors.csv", "r") as f:
  data = csv.DictReader(f)
  for row in data:
    print(row)

with open("Datasets/favorite_colors.csv", "r") as f:
  data = csv.reader(f)
  for row in data:
    print(row)
'''



def csvToDict():
  ans={"Q1":{},"Q2":{}}
  nineBlue=0
  yellowTotal=0
  with open("Datasets/favorite_colors.csv", "r") as file:
    data = csv.reader(file)
    for i in data:
      grade = i[0]
      favorite_color =i[1]
      if (grade=="9" and favorite_color=="blue"):
        nineBlue+=1
        ans["Q1"]["# of 9th graders whose favorite color is blue"] = nineBlue
      elif (favorite_color=="yellow"):
        yellowTotal+=1
        ans["Q2"]["# of Students whose favorite color is yellow"] = yellowTotal
  print(ans)
    

def csvToTable():
  with open("Datasets/favorite_colors.csv", "r") as file:
    table={"Total":{}}
    data = csv.reader(file)
    next(data)
    for i in data:
        if i[0] not in table:
          table[i[0]]={}
        if i[1] not in table[i[0]]:
          table[i[0]][i[1]] = 1
        else:
          table[i[0]][i[1]]+=1
        if i[1] not in table["Total"]:
          table["Total"][i[1]]=1
        else: 
          table["Total"][i[1]]+=1
  print(table)




def csv2Table(fp):
  print(fp)
  with open(fp, "r") as file:
    d={"total" : {}}
    data = csv.DictReader(file)
    for i in data:
      if i["grade"] not in d.keys():
      
         #if we have not seen the new grade
        d[i["grade"]] = {i["favorite_color"] : 1}
        #make a new subdictionary named the grade, and have its key be the color, and its value as 1
      else: #if we have seen the grade before
        if i["favorite_color"] not in d[i["grade"]].keys():
          #if we have seen this grade - color combination
          d[i["grade"]][i["favorite_color"]]=1
          #then make a new color key in the grade subdictionary with value 1
        else: 
         d[i["grade"]][i["favorite_color"]]+=1
         #add 1 to the the color key becuase we have seen this grade-color combo before
  return d
  
  
print(csv2Table("Datasets/favorite_colors.csv"))