def size_fits(vehicle, slot):
    size_order = {"small": 1, "medium": 2, "large": 3}
    return size_order[slot.size] >= size_order[vehicle.size]

def vip_rule(vehicle, slot):
    if slot.is_reserved and not vehicle.is_vip:
        return False
    return True

def electric_rule(vehicle, slot):
    if vehicle.is_electric and not slot.has_charger:
        return False
    return True

def valid_allocation(vehicle, slot):
    return (
        slot.is_available
        and size_fits(vehicle, slot)
        and vip_rule(vehicle, slot)
        and electric_rule(vehicle, slot)
    )