class Person:
    def __init__(self, name, age, grade, is_programmer):
        self.name = name
        self.age = age
        self.grade = grade
        self.is_programmer = is_programmer
        self.is_human = is_programmer

    def person_eat(self):
        print(self.name + " eats " + "Mango")

    def walk(self):
        if self.is_human:
            print(self.name + "walks with 2 legs")
        else:
            print("Could not identify species")

    # def hasCar(self):
    #     hascar = True
    #     car = "audi"
    #     if hascar:
    #         print("Car info" + )
