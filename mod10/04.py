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


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            speed_change = random.randint(-10, 15)
            car.kiihdytä(speed_change)
            car.drive(1)

    def print_status(self):
        print(f"{'Registration':<15}{'Max speed':<15}{'Speed':<15}{'Distance'}")

        for car in self.cars:
            print(f"{car.rn:<15}{car.ms:<15}{car.cs:<15}{car.td:.1f} km")

    def race_finished(self):
        for car in self.cars:
            if car.td >= self.distance:
                return True

        return False


# Create 10 cars
cars = []

for i in range(1, 11):
    maximum_speed = random.randint(100, 200)
    car = Car(f"ABC-{i}", maximum_speed)
    cars.append(car)


# Create the race
race = Race("Grand Demolition Derby", 8000, cars)


# Run the race
hours = 0

while not race.race_finished():
    race.hour_passes()
    hours += 1

    if hours % 10 == 0:
        race.print_status()


# Print final status
print("Final status:")
race.print_status()