## oop: Objet Oriented programming, IN OOP we use classs and object.
## how to create object
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age= age

    def display(self):
        print(f"Name is {self.name}")
        print(f"Name is {self.age}")

## how to create object
st1 = Student(name='sandip', age=24)
st1.display()

st2 = Student(name='sandeep', age=25)
st2.display()


#another example, WAP a python program to create a class Laptop with properties[id, name, ram] and create 3 object ofit.


class Laptop:
    def __init__(self, id, name, ram):
        self.id= id
        self.name=name
        self.ram=ram

    def display(self):
        print(f"Id is {self.id}, name is {self.name}, and RAM is {self.ram}")

p1 = Laptop(id=1, name='lenovo', ram= '1GB')
p2 = Laptop(id=2, name='mac', ram= '10GB')
p3 = Laptop(id=3, name='HP', ram= '5GB')
p1.display()
p2.display()
p3.display()
        
        