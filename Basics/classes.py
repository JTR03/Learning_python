class vehicle():
    def __init__(self,bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class cars(vehicle):
    def __init__(self, engineType):
        super().__init__('Car')
        self.wheel = 4
        self.doors = 5
        self.engineType = engineType

    def drive(self, speed):
        super().drive(speed)
        print("Driving my",self.engineType, "car at",self.speed)

class motor_cycle(vehicle):
    def __init__(self,hassleCar, engineType):
        super().__init__("Motor Cycle")
        if (hassleCar):
            self.wheel = 3
        else:
            self.wheel = 2
        self.doors = 0
        self.engineType = engineType

    def drive(self, speed):
        super().drive(speed)
        print("Riding my", self.engineType, "maotorcycle at", self.speed)


car1 = cars("gas")
car2 = cars("electric")
mc1 = motor_cycle("gas", True)

print(mc1.wheel)
print(car1.engineType)
print(car2.doors)

car1.drive(90)
car2.drive(60)
mc1.drive(120)