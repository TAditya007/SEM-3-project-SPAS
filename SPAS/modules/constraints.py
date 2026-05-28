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


def availability_rule(slot):
    return slot.is_available


def get_constraint_failures(vehicle, slot):
    failures = []

    if not availability_rule(slot):
        failures.append("slot not available")

    if not size_fits(vehicle, slot):
        failures.append("slot size too small")

    if not vip_rule(vehicle, slot):
        failures.append("reserved slot requires VIP vehicle")

    if not electric_rule(vehicle, slot):
        failures.append("electric vehicle requires charging slot")

    return failures


def valid_allocation(vehicle, slot):
    return len(get_constraint_failures(vehicle, slot)) == 0