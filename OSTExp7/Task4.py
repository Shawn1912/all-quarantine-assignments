class Calculation1:  
    def add(self,a,b):  
        print("Addition is       : ",(a+b))
    
class Calculation2:  
    def subtract(self,a,b):  
        print("Subtraction is    : ",(a-b))
    
class Calculation3:  
    def multiply(self,a,b):  
        print("Multiplication is : ",(a*b))
    
class Calculator(Calculation1,Calculation2, Calculation3):  
    def divide(self,a,b):  
        print("Division is       : ",(a/b))
    
d = Calculator()  
d.add(10,20)
d.subtract(10,20)
d.multiply(10,20)
d.divide(10,20)
