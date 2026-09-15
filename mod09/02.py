class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0 , travelled_distance = 0):
        self.rn = registration_number
        self.ms = maximum_speed
        self.cs = current_speed
        self.td = travelled_distance

    def kiihdytä(self, speed):
        self.cs += speed


car1 = Car("ABC-123", 147)
car1.kiihdytä(30)
car1.kiihdytä(70)
car1.kiihdytä(50)
print(f"Current speed is {car1.cs} km/h.")

car1.kiihdytä(-200)
print(f"Current speed is {car1.cs} km/h.")
