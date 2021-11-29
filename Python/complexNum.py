class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self, otherNum):
        real = self.a + otherNum.a
        imaginary = self.b + otherNum.b
        complexSum = ComplexNumber(real,imaginary)
        return complexSum

    def subtract (self, otherNum):
        real = self.a - otherNum.a
        imaginary = self.b - otherNum.b
        complexDiff = ComplexNumber(real,imaginary)
        return complexDiff
        # this also works: return self.add(ComplexNumber(-otherNum.a, -otherNum.b))

    def multiply (self, otherNum):
        real = ((self.a)*(otherNum.a))-((self.b)*(otherNum.b))
        imaginary = ((self.b)*(otherNum.a))+((self.a)*(otherNum.b))
        complexProd = ComplexNumber(real,imaginary)
        return complexProd

    def divide (self, otherNum):
        real = (((self.a)*(otherNum.a))+((self.b)*(otherNum.b)))/(((otherNum.a)*(otherNum.a))+((otherNum.b)*(otherNum.b)))
        imaginary = (((self.b)*(otherNum.a))-((self.a)*(otherNum.b)))/(((otherNum.a)*(otherNum.a))+((otherNum.b)*(otherNum.b)))
        complexQuot = ComplexNumber(real,imaginary)
        return complexQuot
        
    def __str__(self):
        if self.b==0:
            ans=str(self.a)
            return ans
        elif self.b==1:
            ans=str(self.a)+"+"+"i"
            return ans
        elif self.b==-1:
            ans=str(self.a)+"-"+"i"
            return ans
        elif self.b>0:
            ans=str(self.a)+"+"+str(self.b)+"i"
            return ans
        else:
            ans=str(self.a)+str(self.b)+"i"
            return ans
        # also account for formatting when a is 0
num1 = ComplexNumber(2, 4)
num2 = ComplexNumber(-2, -5)

sum=num1.add(num2)
diff=num1.subtract(num2)
prod=num1.multiply(num2)
quot=num1.divide(num2)

print(sum)
print(diff)
print(prod)
print(quot)