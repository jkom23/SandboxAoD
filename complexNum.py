class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, otherNum):
        real = self.a + otherNum.a
        imaginary = self.b + otherNum.b
        complexSum = ComplexNumber(real,imaginary)
        return complexSum

    def subtraction (self, otherNum):
        real = self.a - otherNum.a
        imaginary = self.b - otherNum.b
        complexDiff = ComplexNumber(real,imaginary)
        return complexDiff

    def multiplication (self, otherNum):
        real = ((self.a)*(otherNum.a))-((self.b)*(otherNum.b))
        imaginary = ((self.b)*(otherNum.a))+((self.a)*(otherNum.b))
        complexProd = ComplexNumber(real,imaginary)
        return complexProd

    def division (self, otherNum):
        real = (((self.a)*(otherNum.a))+((self.b)*(otherNum.b)))/(((otherNum.a)*(otherNum.a))+((otherNum.b)*(otherNum.b)))
        imaginary = (((self.b)*(otherNum.a))-((self.a)*(otherNum.b)))/(((otherNum.a)*(otherNum.a))+((otherNum.b)*(otherNum.b)))
        complexQuot = ComplexNumber(real,imaginary)
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