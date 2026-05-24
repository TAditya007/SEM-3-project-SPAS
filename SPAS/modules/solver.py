from modules.constraints import valid_allocation
from modules.decision import calculate_utility

class ParkingSolver:
    def __init__(self, vehicles, slots):
        self.vehicles = sorted(vehicles, key=lambda v: v.priority, reverse=True)
        self.slots = slots
        self.assignment = {}

    def solve(self):
        for vehicle in self.vehicles:
            possible_slots = [slot for slot in self.slots if valid_allocation(vehicle, slot)]

            if possible_slots:
                best_slot = max(possible_slots, key=lambda slot: calculate_utility(vehicle, slot))
                self.assignment[vehicle.vehicle_id] = best_slot.slot_id
                best_slot.is_available = False
            else:
                self.assignment[vehicle.vehicle_id] = None

        return self.assignment