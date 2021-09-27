i=2
while (i<20):
    print(i)
    i+=3
  
def addxy (x, y):
    return x+y

def largerxy (x,y):
    if (x>y):
        return x
    elif (y>x):
        return y
    else:
        return False

def xor (a,b):
    return (a!=b)

def hellon(n):
    print("hello"*n)

def fraction(n):
    print (1/n)

def factorial(n):
    fact = 0
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        fact =1
        
