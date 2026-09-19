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

##Pääohjelma
h = Elevator(1, 10)

h.go_to_floor(5)
h.go_to_floor(1)
h.go_to_floor(11)