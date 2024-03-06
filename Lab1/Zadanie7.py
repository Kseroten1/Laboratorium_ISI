class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def sound(self):
        print(f"{self.name} is barking")


firstDog = Dog("Bunny", 6, "Black")
secondDog = Dog("Bug", 1, "Brown")
thirdDog = Dog("Rico", 4, "White")

firstDog.sound()
secondDog.sound()
thirdDog.sound()
