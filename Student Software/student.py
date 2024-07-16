class Student:
    def __init__(self, name, phone):
        self.name = name
        self.phone= phone

    def display(self):
        print(f"Name is {self.name},phone is {self.phone}")
