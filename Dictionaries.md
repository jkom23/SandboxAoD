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
1. What does `story['author']` return?
1. How does Python know that `"Hao Jingfang"` is related to `author`? Where is that relationship defined?
1. In the line `story['author']`, what does the value in the square brackets represent?
1. Write a line of code to print the title of the story.
1. How would you describe the **keys** and **values** of this dictionary?

## Mutation
1. Run this code: `story["words"] = 6359`, and then print `story`. What changes?
1. Run this code: `story["title"] = "Folding Beijing"`. What changes?
1. Describe what the assignment operator (`=`) does in the context of dictionaries.
1. Write a line of code to add the key `"translator"` and value `"Ken Liu"` to `story`.
1. Run this code: `del story['published']`. What happens?
1. Write a line of code to change the value of a key `"B48"` to `15` in a dictionary named `classrooms`.
1. Write a line of code to delete the entry with key `"B48"` in a dictionary named `classrooms`.

## Iteration
1. What gets printed in the following snippet of code?
    ```py
    for x in story:
      print(story)
    ```
1. What is a better name for the variable than `x`?
1. How do we iterate through a dictionary's values?
1. Explain what is happening in the following snippet of code. Some useful terms are **tuple** and **unpacking**.
    ```py
    for (k,v) in story:
        print(k)
        print(v)
    ```

## Application
1. Write a function `count()` that takes a list of strings as input and outputs a dictionary where each unique string is a key, and its count is the value. For example, `count(["hello", "hello", "world", "hello"])` should return `{"hello": 3, "world": 1}`
