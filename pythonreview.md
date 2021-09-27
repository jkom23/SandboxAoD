# Python Introduction (or Review)
You can access the `Python shell` by running `python3` in your terminal!  
I also recommend making a `sandbox.py` to test and check your answers.

1. How do you initialize a variable in Python?
Just create make a label equal to some value. Ex. num = 1
1. How does Python distinguish between different variable types?
It doenst, all labels can hold all types of variables
1. Does Python check variable types **statically** or **dynamically**?
Dynamically
1. What happens if you run a Python script and there is a bug?
You get a terminal error
1. Convert the following snippet into one line:
    ```py
    if (a and not b):
      return False
    else:
      return True
    ```
  return (not a or b)
1. Explain the difference between `range(1,10)` and `range(1,10,2)`.
range(1,0) gives the integers from 1,10 with a step of 1 but range(1,10,2) gives this range of integers but with a step of 2 instead of 1
1. Convert the following for-loop into a while-loop:
    ```py
    for i in range(2, 20, 3):
      print(i)
    ```
i=2
while (i<20):
  print(i)
  i+=3
  

    ### Write the following functions.
1. `add(x,y)` returns the sum of `x` and `y`
1. `larger(x,y)` returns the larger number
1. `xor(a,b)` returns whether _exactly_ one input is True
1. `hello(n)` prints `"hello"` _n_ times
1. `fraction(n)` prints the float representations of `1/2, 1/3, 1/4 ... 1/n`
1. `factorial(n)` returns the factorial of _n_ (written as `n!`)
1. `stars(n)` prints a right triangle of stars with height and base _n_  
    ex: `stars(3)` should print:
    ```
    *
    **
    ***
    ```
