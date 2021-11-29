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
    for i in range (2,n,1):
        print(1/i)


def factorial(n):
    factorial = 0
    if n<0:
        print ("the factorial does not exist")
    elif n==0 or n==1:
        return 1
    else:
        factorial =1
        while (n>1):
            factorial=factorial*n
            n-=1
        return factorial

def factortial(n):
    if (n==0 or n==1):
        return 1
    else:
        print(str(n)+" * factortial(" + str(n) +"-1)")
        return n*factortial(n-1)

def factoriality(n):
    total=1
    for i in range(1,n+1):
        total *= i
    return total

def stars(n):
    for i in range(n+1):
        print ("*"*i)

def makeStars(n):
    for i in range (1,n+1):
        for j in range(i):
            print("*", end ='')
        print()

