class Car:
    def __init__(self, registration_number, maximum_speed, current_speed = 0 , travelled_distance = 0):
        self.rn = registration_number
        self.ms = maximum_speed
        self.cs = current_speed
        self.td = travelled_distance

car1 = Car("ABC-123", 147)

print(f"Rigisteration number is {car1.rn:s} and it's maximun speed is {car1.ms} km/h")