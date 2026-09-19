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


cars = []

# Create 10 cars
for i in range(1, 11):
    maximum_speed = random.randint(100, 200)
    car = Car(f"ABC-{i}", maximum_speed)
    cars.append(car)


# Race
while True:

    for car in cars:
        speed_change = random.randint(-10, 15)
        car.kiihdytä(speed_change)
        car.drive(1)

    # Check if one car has reached 10,000 km
    for car in cars:
        if car.td >= 10000:
            break
    else:
        continue

    break


# Print results 
print(f"{'Registration':<15}{'Max speed':<15}{'Speed':<15}{'Distance'}") 

for car in cars: 
    print(f"{car.rn:<15}{car.ms:<15}{car.cs:<15}{car.td:.1f} km")
