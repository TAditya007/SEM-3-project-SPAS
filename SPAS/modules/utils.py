from modules.decision import calculate_utility

def print_assignment(assignment, vehicles, slots):
    slot_map = {slot.slot_id: slot for slot in slots}

    print("\nParking Allocation Result")
    print("-" * 120)

    for vehicle in vehicles:
        slot_id = assignment.get(vehicle.vehicle_id)

        vip_text = "VIP" if vehicle.is_vip else "Regular"
        ev_text = "Electric" if vehicle.is_electric else "Non-Electric"

        if slot_id:
            slot = slot_map[slot_id]
            reserved_text = "Reserved" if slot.is_reserved else "General"
            charger_text = "Charger" if slot.has_charger else "No-Charger"
            utility = calculate_utility(vehicle, slot)

            print(
                f"Vehicle {vehicle.vehicle_id} ({vehicle.vehicle_type}, {vehicle.size}, {vip_text}, {ev_text}, priority={vehicle.priority}) "
                f"-> Slot {slot.slot_id} ({slot.size}, {reserved_text}, {charger_text}, distance={slot.distance}, utility={utility})"
            )
        else:
            print(
                f"Vehicle {vehicle.vehicle_id} ({vehicle.vehicle_type}, {vehicle.size}, {vip_text}, {ev_text}, priority={vehicle.priority}) "
                f"-> No slot available"
            )