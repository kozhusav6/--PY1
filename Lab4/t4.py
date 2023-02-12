
class cars:
    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color

    def beep(self):
        print("beep")

    def __str__(self):
        return f"{self.name}: { self.age}: {self.color}"

    def __repr__(self):
        return f"{self.__class__}: {self.name}: { self.age}: {self.color}"


class Passenger(cars):
    def __init__(self, name: str, age: int, color: str, count: int):
        super().__init__(name, age, color)
        self.count = count

    def __str__(self):
        return f"{self.name}: { self.age}: {self.color}: {self.count}"

    def __repr__(self):
        return f"{self.__class__}: {self.name}: { self.age}: {self.color}: {self.count}"


class freight(cars):
    def __init__(self, name: str, age: int, color: str, weight: int):
        super().__init__(name, age, color)
        self.weight = weight

    def beep(self):
        print("boop")

    def __str__(self):
        return f"{self.name}: { self.age}: {self.color}: {self.weight}"

    def __repr__(self):
        return f"{self.__class__}: {self.name}: { self.age}: {self.color}: {self.weight}"


mazda = Passenger("mazda", 2, "grey", 5)
vaz = freight("vaz", 10, "black", 500)
#Проверки
print(mazda)
print(vaz)

mazda.beep()
vaz.beep()
