import random

class Car:
    def __init__(self, registration_number, maximum_speed, current_speed=0, travelled_distance=0):
        self.rn = registration_number
        self.ms = maximum_speed
        self.cs = current_speed
        self.td = travelled_distance

    def kiihdytä(self, speed):
        self.cs += speed

        if self.cs > self.ms:
            self.cs = self.ms

        if self.cs < 0:
            self.cs = 0

    def drive(self, time):
        distance = time * self.cs
        self.td += distance

## Sub classes electric car and gasoline car
class Electric_car(Car):
    def __init__(self,registration_number, maximum_speed,current_speed,travelled_distance, electric_capacity):
        super().__init__(registration_number, maximum_speed,current_speed,travelled_distance)
        self.ec = electric_capacity
    def drive(self,time):
        super().drive(time)

    def print(self):
        print(f"The electric car has travelled {self.td}")

class Gasoline_car(Car):
    def __init__(self,registration_number, maximum_speed,current_speed,travelled_distance,tank_volume):
        super().__init__(registration_number, maximum_speed,current_speed,travelled_distance)
        self.tv = tank_volume

    def drive(self,time):
        super().drive(time)

    def print(self):
        print(f"The gasoline car has travelled {self.td}")



## Create electric car and gasloine car
electric1 = Electric_car("ABC-15", 180,50,0,52.5)
gasoline1 = Gasoline_car("ACD-123", 165,25,0,32.3)




electric1.drive(3)
gasoline1.drive(3)
electric1.print()
gasoline1.print()