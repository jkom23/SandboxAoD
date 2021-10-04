# Lists
This worksheet is adapted from [Lisa Olivieri's](https://www.chc.edu/faculty/lisa-olivieri) work.

Jack Komaroff 
9/30/21
## Model A | Access and Iteration

1. Examine the following **lists**:
    ```py
    digits = [0,1,2,3,4,5,6,7,8,9]
    title = ["A", "Hundred", "Ghosts", "Parade", "Tonight"]
    story = ["A Hundred Ghosts Parade Tonight", "Xia Jia", 2012]
    ```
    1. How many **elements** does the list named `digits` contain?
    10
    1. What type of data is stored in each list?
    digits = ints
    title= strings
    story= strings and ints
1. How would you define a **list**?
A set of values ordered from 0 to the list length
    ### Type and enter the following Python code:
    ```py
    book = ["Minor","Feelings","by","Cathy", "Park", "Hong"]
    print(book[0])
    ```
1. What is printed for `book[0]`?
Minor
1. What value in the list does `book[3]` represent?
Cathy
1. Write a line of code that prints the last value.
print(book[5])
1. What happens if you try to print `book[6]`? Why?
error, there is no 6th value. 
1. What does `book[-1]` return?
Hong
1. Explain how positive and negative **indexes** locate specific elements.
They go from start to end of the list and end to start of the list, respectivly
1. What is printed with this statement: `print(book)`? How is the information displayed?
all of the values of the list, with brackets at start and end, '' on each value, and commas to deliniate
1. A veterinarian stores the names of each pet they examine.

    ```py
    pets = ["Apollo", "Bandit", "Nova", "Ginger",
    "Mochi", "Honey", "Buster", "Arthur", "Taro"]
    ```

    1. Examine the following code. What is being stored in `pet` for each iteration of the loop?
        ```py
        for pet in pets:
            print(pet)
        ```
    1. Does anything change if we change `pet` to `foo`?
    No, we are just iterating through the list and printing the current value.
## Model B | Insertion and Deletion
An athlete keeps track of how many minutes it takes for them to run a mile.

```py
minute_miles = [8.4, 9.2, 8.1, 6.5, 6.1, 5.9, 7.4, 8.3, 6.2]
```

1. Explain what this code of line would do: `minute_miles.append(7.3)`
Add 7.3 to the end of the list
1. Write a line of code that would add `6.7` to the list.
minute_miles.append(6.7)
1. What does `minute_miles.insert(2, 8.8)` do?
Add 8.8 to the list in the second index (3rd spot)
1. Write a line of code that would place `6.0` at the beginning of the list.
minute_miles.insert(0, 6.0)
1. Explain what this line of code would do: `del minute_miles[2]`
it deletes the value at the second index.
1. Write a line of code that would delete the last record in the list.
del minute_miles[8]
1. Explain what this line of code would do: `minute_miles.remove(8.1)`
it deletes 8.1 from the list and moves the values accoriding
1. Write a line of code that would delete `8.3` from the list.
minute_miles.remove(8.3)
1. What would happen if the same time appears in the list twice, and `remove()` was used? Does it remove both instances?
It would only the first instance. 
1. What happens if you try to remove `3.3`?
Error because item does not exist in the list.