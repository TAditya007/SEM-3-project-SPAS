class ParkingSystem:
    def __init__(self, vehicles=None, slots=None):
        self.vehicles = vehicles if vehicles else []
        self.slots = slots if slots else []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def add_slot(self, slot):
        self.slots.append(slot)