# Dictionaries
Examine and run the following code:

```py
story = {
  "title": "Invisible Planets",
  "author": "Hao Jingfang",
  "published": 2013
}
```

## Access
1. Describe what information the dictionary named `story` contains.
It has a title string variable, an author string variable, and a year published int variable
1. What does `story['author']` return?
It returns "Hao Jingfang"
1. How does Python know that `"Hao Jingfang"` is related to `author`? Where is that relationship defined?
In the story dictionary we have set author to Hao Jingfang
1. In the line `story['author']`, what does the value in the square brackets represent?
the variable in the story dictionary that we want to access
1. Write a line of code to print the title of the story.
print(story['title'])
1. How would you describe the **keys** and **values** of this dictionary?
The keys are the variable labels and the values are the what goes in them, ex strings or ints, 
## Mutation
1. Run this code: `story["words"] = 6359`, and then print `story`. What changes?
We have added a new key into the story dictionary and it is word count; we set it to 6359
1. Run this code: `story["title"] = "Folding Beijing"`. What changes?
We have reset the title to be Folding Beijing
1. Describe what the assignment operator (`=`) does in the context of dictionaries.
It will reset the key to whaterver value is being given
1. Write a line of code to add the key `"translator"` and value `"Ken Liu"` to `story`.
story["translator"] = "Ken Liu"

1. Run this code: `del story['published']`. What happens?
It removed the published key (and its corresponding value) from the dictionary
1. Write a line of code to change the value of a key `"B48"` to `15` in a dictionary named `classrooms`.
classrooms["B48"]=15
1. Write a line of code to delete the entry with key `"B48"` in a dictionary named `classrooms`.
del classrooms["B48"]
## Iteration
1. What gets printed in the following snippet of code?
    ```py
    for x in story:
      print(x)
    ```
  It will iterate through the story dictionary and print each key
1. What is a better name for the variable than `x`?
key
1. How do we iterate through a dictionary's values?
```py
 for x in story:
      print(story[x])
```
1. Explain what is happening in the following snippet of code. Some useful terms are **tuple** and **unpacking**.
    ```py
    for k, v in story.items():
	print("Key:", k)
	print("Value:", str(v))
    ```
    We are turing the dictioary into a list of tuples (via story.items), and are now unpacking the tuples list instead of both the key and values seperatly. unpacking seperatly returns too many values

## Application
1. Write a function `count()` that takes a list of strings as input and outputs a dictionary where each unique string is a key, and its count is the value. For example, `count(["hello", "hello", "world", "hello"])` should return `{"hello": 3, "world": 1}`
```py

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

```