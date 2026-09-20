class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom
    def floor_up(self):
        #Move elevator up 1 floor
        self.current +=1
        print(f"Elevator is at floor {self.current}")
    def floor_down(self):
        #Move elevator down 1 floor
        self.current -= 1
        print(f"Elevator is at floor {self.current}")
    def go_to_floor(self, floor):
        while self.current != floor:
            if self.current > floor:
                self.floor_down()
            else:
                self.floor_up()
        #Move elevator to specific floor
        self.current = floor
        print(f"Elevator is at floor {self.current}")
        pass
    e = Elevator(1,10)
    e.go_to_floor(5)