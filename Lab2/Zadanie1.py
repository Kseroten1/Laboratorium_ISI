class Animal:
    def __init__(self, name: str, age: int, sex: int):
        self.name = name
        self.age = age
        self.sex = sex

    def sound(self):
        print("")


class Dog(Animal):
    def __init__(self, name: str, age: int, sex: int, breed: str):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self): print("bark, bark")


class Cat(Animal):
    def __init__(self, name: str, age: int, sex: int, breed: str):
        super().__init__(name, age, sex)
        self.breed = breed

    def sound(self): print("miau")


class Fox(Animal):
    def __init__(self, name: str, age: int, sex: int):
        super().__init__(name, age, sex)

    def sound(self): print("squik")
