Q. Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a
constructor which takes the parameters x and y (these should all be numbers).
1. Write a method called add which returns the sum of the attributes x and y.
2. Write a class method called multiply, which takes a single number parameter a and returns the
product of a and MULTIPLIER.
3. Write a static method called subtract, which takes two number parameters, b and c, and returns
b - c.
4. Write a method called value which returns a tuple containing the values of x and y. Make this
method into a property, and write a setter and a deleter for manipulating the values of x and y.

Solution:

class Numbers:
    MULTIPLIER = 5

    def __init__(self, x, y):
        self.x = x
        self.y = y

1.    def add(self):
        return self.x+self.y

2.    def multiply(self, a):
        return a*self.MULTIPLIER

3.    @staticmethod
    def subtractor(b, c):
        return b - c

4.    @property
    def value(self):
        tup = (self.x, self.y)
        return tup

    def setter(self):
        self.x = int(input("Set value of x: "))
        self.y = int(input("Set value of y: "))

    def deleter(self):
        self.x = 0
        self.y = 0


num = Numbers(5, 6)
print(num.add())
print(num.multiply(2))
print(num.value)
num.setter()
print(num.value)
num.deleter()
print(num.value)
