#!/usr/bin/python3
class Robots:
    def __init__(self, name = None):
        self.name = name
    def hi(self):
        if self.name:
            print("Hi my name is", self.name)
        else:
            print("Hi, sadly I have no name :(")
    def set_name(self, name):
        self.name = name
    def set_year(self, year):
        self.year = year
    def get_year(self):
        return self.year
    def get_name(self):
        return self.name
x = Robots()
x.set_name("Teemo")
x.hi()
x.set_year(2023)
y = Robots()
y.set_name(x.get_name())
y.name = "Tamir"
y.hi()
y.set_year(2012)
print("The Robot X Specs :",x.__dict__)
print("The Robot Y Specs :",y.__dict__)
