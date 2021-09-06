'''
Triple quotes denotes a block comment!
This homework should feel very familiar 
(hint: you've written the exact same methods before!)
'''

# Practice: What does this method do?
def foo(n):
  temp = n
  sum = 0
  while temp > 0:
    sum += temp % 10
    temp = temp // 10
  return sum


# 1) Return whether a number is positive
def is_positive(n):
  return n>0

# 2) Return the smallest number
def find_smallest(x, y, z):
  if x<y and x<z:
    return x
  elif y<x and y<z:
    return y
  else:
    return z


# 3) Return whether x+y is greater than z
def is_sum_greater(x, y, z):
  return x+y>z

# 4) Print all numbers from 1 to n that
#    are multiples of 3 or 5
def print35(n): 
    s = 1
    while s<=n:
      if s%3==0 or s%5==0:
        print(s)
      s+=1
    

# 5) Write a method named say_hello
#	 - takes a number n as parameter
#	 - prints "Hello" n times

def say_hello(n):
  print("Hello " * n)


# Test your methods!!! I've included some examples.
print(foo(123))                 # prints 6

print(is_sum_greater(1, 5, 3))    # should print True
                   # should print 3, 5, 6, 10
                    # should print "Hello" 3 times

say_hello(9)