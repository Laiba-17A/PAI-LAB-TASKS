class Vehicle:
    def __init__(self, seat_cap):
        self.seat_cap = seat_cap

    def fare(self):
        return self.seat_cap * 100


class Bus(Vehicle):
    def fare(self):
        basefare = super().fare() 
        Mcharge = basefare * 0.10
        totalfare = basefare + Mcharge
        return totalfare


bus = Bus(seat_cap=50)
print("Total Bus Fare:", bus.fare())
