# Python Classes

## Example
A **UML Class Diagram (Unified Modeling Language)** is a graphical representation of a class. It shows the **signatures** of a class’s code.

Examine the following diagram for a `Point` class.

| Point |
| :-- |
| x: float|
|y: float|
|`slope(Point): float`|
|`distance_to(Point): float`|

And here is an implementation of this class in Python:
```py
    class Point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
    ## we can also have default values for the parameters
        def slope(self, other_point):
            y_diff = (self.y - other_point.y)
            x_diff = (self.x - other_point.x)
            return y_diff / x_diff

        def distance_to(self, other_point):
            y_diff = (self.y - other_point.y)
            x_diff = (self.x - other_point.x)
            return ((y_diff**2)+(x_diff**2))**0.5

    p1 = Point(0, 0)
    p2 = Point(2, 0)
    m = p2.slope(p1) # 0.0
## same as Point.slope(p2, p1) but above structure is more intuitive
    d = p1.distance_to(p2) # 2.0


```
1. What is the syntax for defining a class in Python?
```py
class ClassName:
    def functionName(attribute)
     #code
    #other functions
```
2. What is stored in the variable `p1`?
There is a reference to a point object stored at a specific memory address
3. What does the `slope()` function do, and how is it used?
it inputs two instances of a point and calculates the slope of the line that connects them


## Theory
1. What is a "class"? When and why do we use them?
A class is a blueprint to make new instances of that class
2. What are some examples of classes that you've used before?
Class for employee ID in a company database
ints and strings are also classes with methods (all datatypes are classes)
3. What is a constructor method?
It makes a new instance of that class, the init method
## Practice
1. Create a ComplexNumber class with a constructor method.
2. Write methods for addition, subtraction, multiplication, and division with objects of your ComplexNumber class.
3. Write a __str__ method for your class. What is special about this method? What is the difference between your __str__ method and the default one for your class?

```py
class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, otherNum):
        a_sum = self.a + otherNum.a
        b_sum = self.b + otherNum.b
        complexSum = ComplexNumber(a_sum,b_sum)
        return complexSum
    def subtraction (self, otherNum):
        a_diff = self.a - otherNum.a
        b_diff = self.b - otherNum.b
        complexDiff = ComplexNumber(a_diff,b_diff)
        return complexDiff
    def multiplication (self, otherNum):
        a_factor = ((self.a)*(otherNum.a))-((self.b)*(otherNum.b))
        b_factor = ((self.b)*(otherNum.a))+((self.a)*(otherNum.b))
        complexProd = ComplexNumber(a_factor,b_factor)
        return complexProd
    def division (self, otherNum):
        a_part = (((self.a)*(otherNum.a))+((self.b)*(otherNum.b)))/(((otherNum.a)*(otherNum.a))+((otherNum.b)*(otherNum.b)))
        b_part = (((self.b)*(otherNum.a))-((self.a)*(otherNum.b)))/(((otherNum.a)*(otherNum.a))+((otherNum.b)*(otherNum.b)))
        complexQuot = ComplexNumber(a_part,b_part)
        return complexQuot
    def __str__(self):
        if self.b==0:
            ans=str(self.a)
            return ans
        if self.b>0:
            ans=str(self.a)+"+"+str(self.b)+"i"
            return ans
        else:
            ans=str(self.a)+str(self.b)+"i"
            return ans

num1 = ComplexNumber(2, 4)
num2 = ComplexNumber(-5, 9)

sum=num1.addition(num2)
diff=num1.subtraction(num2)
prod=num1.multiplication(num2)
quot=num1.division(num2)

print(sum)
print(diff)
print(prod)
print(quot)
```
## Application
Design a DataFrame class to store generic tabular data. Consider how your constructor method should work. What other methods should your class have (or in other words, what other operations do you want to be able to perform on a generic data set)? Implement your class.


