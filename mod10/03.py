class Elevator:
    def __init__(self, bottom_floor, top_floor, current_floor=0):
        self.bf = bottom_floor
        self.tf = top_floor
        self.cf = current_floor

    def floor_up(self):
        if self.cf == self.tf:
            print("elevator is on top floor, can't go up")
        else:
            self.cf += 1
            print("floor went up 1 floor")

    def floor_down(self):
        if self.cf == self.bf:
            print("elevator is on bottom floor, can't go down")
        else:
            self.cf -= 1
        print("floor went down 1 floor")

    def go_to_floor(self, floor):
        if floor > self.tf:
            print("floor is too high")
        elif floor < self.bf:
            print("floor is too low")

        if floor > self.cf:
            while self.cf < floor:
                if self.cf == self.tf:
                    print("elevator is on top floor, can't go up")
                    break
                self.floor_up()
            print("elevator is on floor " + str(self.cf))

        elif floor < self.cf:
            while self.cf > floor:
                if self.cf == self.bf:
                    print("elevator is on bottom floor, can't go down")
                    break
                self.floor_down()
            print("elevator is on floor " + str(self.cf))

class Building:
    def __init__(self, bottom_floor, top_floor, elevator_count):
        self.bottom_floor = bottom_floor
        self.top_floor = top_floor
        self.elevator = []

        for i in range(elevator_count):
            elevator = Elevator(bottom_floor, top_floor)
            self.elevator.append(elevator)

    def run_elevator(self, elevator, floor):
        self.elevator[elevator - 1].go_to_floor(floor)
        print(f"the elevator{elevator} is in floor {floor}")

    def fire_alarm(self):
        print("FIRE BREAKOUT!!!! AHHHHHHHHHHH!!")
        for i in range(len(self.elevator)):
            self.run_elevator(i+1,1)

##Pääohjelma
b = Building(1, 10, 3)
b.run_elevator(1, 5)
b.fire_alarm()