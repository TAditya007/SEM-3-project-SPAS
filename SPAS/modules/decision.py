def calculate_utility(vehicle, slot):
    priority_score = vehicle.priority * 10
    distance_score = max(0, 20 - slot.distance)
    vip_bonus = 15 if vehicle.is_vip and slot.is_reserved else 0
    ev_bonus = 15 if vehicle.is_electric and slot.has_charger else 0

    return priority_score + distance_score + vip_bonus + ev_bonus