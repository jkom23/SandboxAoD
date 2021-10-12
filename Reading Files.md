# Reading Files
Download `favorite_colors.csv` and put it in a folder named `datasets` in your Art of Data folder.

## Model A
1. What does `csv` stand for?
Comma-seperated values
1. What information does `favorite_colors.csv` contain?
Grade of a student and their favorite color

## Model B
Examine and run the following snippet of code.
```py
with open("Datasets/favorite_colors.csv", "r") as f:
  print(f)
```

1. What is printed when you run this code?
<_io.TextIOWrapper name='Datasets/favorite_colors.csv' mode='r' encoding='cp1252'>
1. Explain the syntax of the `open()` function.
It takes the path and file name, and then a mode (ex r for read, a for append, w for write, x for create)
1. Explain what you would need to change if you wanted to _write_ to the file.
```py
with open("Datasets/favorite_colors.csv", "w") as f:
  print(f)
```

it prints:
<_io.TextIOWrapper name='Datasets/favorite_colors.csv' mode='w' encoding='cp1252'>
1. Explain why `open()` is called inside a **`with` statement**.
It allows us to bypass the opening and closing rules for files so the files close after the code runs
## Model C
Examine and run the following snippet of code.
```py
import csv
with open("Datasets/favorite_colors.csv", "r") as f:
  data = csv.reader(f)
  for row in data:
    print(row)
```
1. What **module** is being imported? Link to the official documentation for this module.
We are importing the csv module.
https://docs.python.org/3/library/csv.html
1. What does `csv.reader()` return?
Returns a list of the values for the two variables; just prints out the comma sperated values

1. What is printed when you run this code?

['12', 'blue']
['9', 'red']
['10', 'red']
and so on...
1. Explain how to interpret the for-loop and `row` in terms of the `csv` file.
we are iterating row by row (group of comma seperated value, then another group of comma sepeated values. this is a "row") and just printing out the comma seperated values for all the rows (each row prints after the next row)

## Model D
Examine and run the following snippet of code.
```py
import csv
with open("datasets/favorite_colors.csv", "r") as f:
  data = csv.DictReader(f)
  for row in data:
    print(row)
```
We are iterating through each row in the csv and printing our the row
1. What does `csv.DictReader()` return, and how is this different from `csv.reader()`?
 csv.DictReader() returns the csv as a dictionary, csv.reader() just returns the comma seperated values
1. What is printed when you run this code?
the above code prints the entire row with both variables and their values for said row.
1. Explain how to interpret the for-loop and `row` in terms of the `csv` file.
We are taking the csv read as a dictionary and interating through that and printing out each row
## Application
Write a Python file to analyze `favorite_colors.csv` and create a **nested dictionary** that contains the answers to the following questions:
1. How many students in 9th grade put blue as their favorite color?
1. How many students in total put yellow as their favorite color?

```py
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
    table={}
    data = csv.reader(file)
    for i in data:
        if i not in table:
          table={i:{}}
        
      # grade = i[0]
      # favorite_color =i[1]
      # if (grade=="9" and favorite_color=="blue"):
      #   nineBlue+=1
      #   ans["Q1"]["# of 9th graders whose favorite color is blue"] = nineBlue
      # elif (favorite_color=="yellow"):
      #   yellowTotal+=1
      #   ans["Q2"]["# of Students whose favorite color is yellow"] = yellowTotal
  print(ans)
```