# Python Introduction (or Review)
You can access the `Python shell` by running `python3` in your terminal!  
I also recommend making a `sandbox.py` to test and check your answers.

1. How do you initialize a variable in Python?
Just create make a label and set it equal to some value. Ex. num = 1
1. How does Python distinguish between different variable types?
It doens't, all labels can hold all types of variables
1. Does Python check variable types **statically** or **dynamically**?
Dynamically
1. What happens if you run a Python script and there is a bug?
You get a terminal error at the program won't run
1. Convert the following snippet into one line:
    ```py
    if (a and not b):
      return False
    else:
      return True
    ```
  return (not a or b)

1. Explain the difference between `range(1,10)` and `range(1,10,2)`.
range(1,0) gives the integers from 1,10 with a step of 1 but range(1,10,2) gives this range of integers but with a step of 2 instead of 1.

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

def addxy (x, y):
    return x+y

1. `larger(x,y)` returns the larger number

def largerxy (x,y):
    if (x>y):
        return x
    elif (y>x):
        return y
    else:
        return False

1. `xor(a,b)` returns whether _exactly_ one input is True

def xor (a,b):
    return (a!=b)

1. `hello(n)` prints `"hello"` _n_ times

def hellon(n):
    print("hello"*n)

1. `fraction(n)` prints the float representations of `1/2, 1/3, 1/4 ... 1/n`

def fraction(n):
    print (1/n)

1. `factorial(n)` returns the factorial of _n_ (written as `n!`)

def factorial(n):
    factorial = 0
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        factorial =1
        while (n>1):
            factorial=factorial*n
            n-=1
        return factorial

1. `stars(n)` prints a right triangle of stars with height and base _n_  
    ex: `stars(3)` should print:
    ```
    *
    **
    ***
    ```

def stars(n):
    for i in range(n+1):
        print ("*"*i)

