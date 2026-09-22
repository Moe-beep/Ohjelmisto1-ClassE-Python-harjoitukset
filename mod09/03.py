class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 60 , travelled_distance = 2000):
        self.rn = registration_number
        self.ms = maximum_speed
        self.cs = current_speed
        self.td = travelled_distance

    def kiihdytä(self, speed):
        self.cs += speed


    def drive(self, time):
        distance = time * self.cs
        self.td += distance


car1 = Car("ABC-123", 147)
car1.drive(1.5)
print(f"Travelled distance of {car1.rn} is {car1.td} and it's speed is {car1.cs} km/h.")