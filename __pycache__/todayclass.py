class Student:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name

    @property
    def roll(self):
        return self.__roll

    @roll.setter
    def roll(self, roll):
        if roll > 0:
            self.__roll = roll
        else:
            self.__roll = None
            print("Enter the correct value")

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name


s1 = Student(28, "Dhinesh")

print(s1.roll)
print(s1.name)

s1.roll = 29
s1.name = "Raghava"

print(s1.roll)
print(s1.name)