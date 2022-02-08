class Multiplier:
    def __init__(self, a):
        self.a = a

    def multiply(self, b=1):
        print(b * (self.a))


x = Multiplier("Hello")
x.multiply(2)

#print(2*"Hello")