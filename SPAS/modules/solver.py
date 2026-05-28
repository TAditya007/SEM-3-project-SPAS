from modules.constraints import valid_allocation
from modules.decision import calculate_utility


class ParkingSolver:
    def __init__(self, vehicles, slots):
        self.vehicles = sorted(vehicles, key=lambda v: v.priority, reverse=True)
        self.slots = slots
        self.assignment = {}
        self.trace = []
        self.rejections = {}

    def get_possible_slots(self, vehicle):
        possible_slots = []
        rejected_slots = []

        for slot in self.slots:
            if valid_allocation(vehicle, slot):
                possible_slots.append(slot)
            else:
                rejected_slots.append(slot.slot_id)

        self.rejections[vehicle.vehicle_id] = rejected_slots

        possible_slots.sort(
            key=lambda slot: calculate_utility(vehicle, slot),
            reverse=True
        )
        return possible_slots

    def backtrack(self, index=0):
        if index == len(self.vehicles):
            self.trace.append("All vehicles processed successfully.")
            return True

        vehicle = self.vehicles[index]
        possible_slots = self.get_possible_slots(vehicle)

        self.trace.append(
            f"Evaluating Vehicle {vehicle.vehicle_id} (priority={vehicle.priority}, size={vehicle.size})"
        )

        if not possible_slots:
            self.trace.append(
                f"No valid slot found for Vehicle {vehicle.vehicle_id}. Marking as unassigned."
            )
            self.assignment[vehicle.vehicle_id] = None
            return self.backtrack(index + 1)

        for slot in possible_slots:
            utility = calculate_utility(vehicle, slot)
            self.trace.append(
                f"Trying Slot {slot.slot_id} for Vehicle {vehicle.vehicle_id} with utility={utility}"
            )

            self.assignment[vehicle.vehicle_id] = slot.slot_id
            slot.is_available = False

            if self.backtrack(index + 1):
                return True

            self.trace.append(
                f"Backtracking: Slot {slot.slot_id} removed from Vehicle {vehicle.vehicle_id}"
            )
            self.assignment[vehicle.vehicle_id] = None
            slot.is_available = True

        self.trace.append(
            f"All candidate slots failed for Vehicle {vehicle.vehicle_id}. Marking as unassigned."
        )
        self.assignment[vehicle.vehicle_id] = None
        return self.backtrack(index + 1)

    def solve(self):
        self.assignment = {}
        self.trace = []
        self.rejections = {}
        self.backtrack()
        return self.assignment

    def get_trace(self):
        return self.trace

    def get_rejections(self):
        return self.rejections