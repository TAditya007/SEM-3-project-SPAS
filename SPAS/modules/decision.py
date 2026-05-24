def calculate_utility(vehicle, slot):
    score = 0

    score += vehicle.priority * 10
    score += max(0, 20 - slot.distance)

    if vehicle.is_vip and slot.is_reserved:
        score += 15

    if vehicle.is_electric and slot.has_charger:
        score += 15

    return score