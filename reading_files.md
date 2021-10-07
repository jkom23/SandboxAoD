# Reading Files
Download `favorite_colors.csv` and put it in a folder named `datasets` in your Art of Data folder.

## Model A
1. What does `csv` stand for?
1. What information does `favorite_colors.csv` contain?

## Model B
Examine and run the following snippet of code.
```py
with open("datasets/favorite_colors.csv", "r") as f:
  print(f)
```

1. What is printed when you run this code?
1. Explain the syntax of the `open()` function.
1. Explain what you would need to change if you wanted to _write_ to the file.
1. Explain why `open()` is called inside a **`with` statement**.

## Model C
Examine and run the following snippet of code.
```py
import csv
with open("datasets/favorite_colors.csv", "r") as f:
  data = csv.reader(f)
  for row in data:
    print(row)
```

1. What **module** is being imported? Link to the official documentation for this module.
1. What does `csv.reader()` return?
1. What is printed when you run this code?
1. Explain how to interpret the for-loop and `row` in terms of the `csv` file.

## Model D
Examine and run the following snippet of code.
```py
import csv
with open("datasets/favorite_colors.csv", "r") as f:
  data = csv.DictReader(f)
  for row in data:
    print(row)
```

1. What does `csv.DictReader()` return, and how is this different from `csv.reader()`?
1. What is printed when you run this code?
1. Explain how to interpret the for-loop and `row` in terms of the `csv` file.

## Application
Write a Python file to analyze `favorite_colors.csv` and create a **nested dictionary** that contains the answers to the following questions:
1. How many students in 9th grade put blue as their favorite color?
1. How many students in total put yellow as their favorite color?
