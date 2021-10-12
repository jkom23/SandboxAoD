import csv
# # with open("Datasets\\favorite_colors.csv", "w") as f:
# #   print(f)

# with open("Datasets/favorite_colors.csv", "r") as f:
#   data = csv.DictReader(f)
#   for row in data:
#     print(row)

# with open("Datasets/favorite_colors.csv", "r") as f:
#   data = csv.reader(f)
#   for row in data:
#     print(row)

# Write a Python file to analyze `favorite_colors.csv` and create a **nested dictionary** that contains the answers to the following questions:
# 1. How many students in 9th grade put blue as their favorite color?
# 1. How many students in total put yellow as their favorite color?


import csv
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
    

def csvToDict():
  with open("Datasets/favorite_colors.csv", "r") as file:
    table={"Total":{}}
    data = csv.reader(file)
    next(data)
    for i in data:
        if i[0] not in table:
          table[i[0]]={}
        if i[1] not in table[i[0]]:
          table[i[0]][i[1]] = 1
        if i[0] not in table["Total"]:
          table["Total"][i[0]]=1
        else:
          table[i[0]][i[1]]+=1
          table["Total"][i[0]]+=1
        
    
  print(table)

csvToDict()

# def csvToTable():
#   table={"B":{}, "Y":{}, "R":{}}
#   nineBlue=0
#   yellowTotal=0
#   with open("Datasets/favorite_colors.csv", "r") as file:
#     data = csv.reader(file)
#     for i in data:
#       grade = i[0]
#       favorite_color =i[1]
#       if (grade=="9" and favorite_color=="blue"):
#         nineBlue+=1
#         ans["Q1"]["# of 9th graders whose favorite color is blue"] = nineBlue
#       elif (favorite_color=="yellow"):
#         yellowTotal+=1
#         ans["Q2"]["# of Students whose favorite color is yellow"] = yellowTotal
#   print(ans)