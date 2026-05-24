from modules.vehicle import Vehicle
from modules.slot import Slot


TEST_CASES = {
    "case1_normal": {
        "vehicles": [
            Vehicle("V1", "Car", "small", 2, False, False),
            Vehicle("V2", "SUV", "medium", 3, True, False),
            Vehicle("V3", "Truck", "large", 1, False, False),
            Vehicle("V4", "Van", "large", 4, False, False),
            Vehicle("V5", "EV-Car", "small", 5, False, True),
        ],
        "slots": [
            Slot("S1", "small", 10, True, False, False),
            Slot("S2", "medium", 5, True, True, False),
            Slot("S3", "large", 15, True, False, False),
            Slot("S4", "small", 7, True, False, True),
        ],
    },

    "case2_vip_priority": {
        "vehicles": [
            Vehicle("V1", "Car", "small", 2, False, False),
            Vehicle("V2", "SUV", "medium", 5, True, False),
            Vehicle("V3", "Sedan", "medium", 3, False, False),
        ],
        "slots": [
            Slot("S1", "small", 8, True, False, False),
            Slot("S2", "medium", 4, True, True, False),
            Slot("S3", "medium", 12, True, False, False),
        ],
    },

    "case3_ev_charging": {
        "vehicles": [
            Vehicle("V1", "EV-Car", "small", 5, False, True),
            Vehicle("V2", "Car", "small", 2, False, False),
            Vehicle("V3", "EV-SUV", "medium", 4, False, True),
        ],
        "slots": [
            Slot("S1", "small", 6, True, False, True),
            Slot("S2", "small", 10, True, False, False),
            Slot("S3", "medium", 5, True, False, True),
        ],
    },

    "case4_no_slot": {
        "vehicles": [
            Vehicle("V1", "Truck", "large", 3, False, False),
            Vehicle("V2", "Bus", "large", 4, False, False),
            Vehicle("V3", "EV-Car", "small", 5, False, True),
        ],
        "slots": [
            Slot("S1", "small", 9, True, False, False),
            Slot("S2", "small", 7, True, False, True),
        ],
    },

    "case5_mixed_complex": {
        "vehicles": [
            Vehicle("V1", "Car", "small", 1, False, False),
            Vehicle("V2", "EV-Car", "small", 5, False, True),
            Vehicle("V3", "SUV", "medium", 4, True, False),
            Vehicle("V4", "Van", "large", 3, False, False),
            Vehicle("V5", "Truck", "large", 2, False, False),
            Vehicle("V6", "EV-SUV", "medium", 5, False, True),
        ],
        "slots": [
            Slot("S1", "small", 11, True, False, False),
            Slot("S2", "small", 6, True, False, True),
            Slot("S3", "medium", 5, True, True, False),
            Slot("S4", "medium", 7, True, False, True),
            Slot("S5", "large", 14, True, False, False),
        ],
    }
}