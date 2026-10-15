class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I study {self.course}.")

    def is_adult(self):
        return self.age >= 18    

student01 = Student("John Doe", 20, "Computer Science")
student02 = Student("Jane Smith", 22, "Mathematics")

student01.introduce()
student02.introduce()
student01.is_adult()
student02.is_adult()

class Robot:
    def __init__(self, name, battery, movement_cost):
        self.name = name
        self.battery = battery
        self.movement_cost = movement_cost

    def move(self):
        if self.battery > 0:
            self.battery -= self.movement_cost
            print(f"{self.name} moved. Battery level: {self.battery}")

        else:
            print(f"{self.name} cannot move. Battery is insufficient.")

    def recharge(self):
        self.battery = 100
        print(f"{self.name} is recharged. Battery level: {self.battery}")

robot01 = Robot("Robo01", 25, 10)
robot01.move()
robot01.move()
robot01.move()
print(robot01.battery)
robot01.recharge()
print(robot01.battery)

class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

counter01 = Counter()
counter02 = Counter()
counter01.increment()
counter01.increment()
counter01.increment()
counter02.increment()
counter02.increment()

# The values of the counters are different because they are separate instances of the Counter class. Each instance maintains its own state, so incrementing one counter does not affect the other.
