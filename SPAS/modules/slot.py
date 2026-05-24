from dataclasses import dataclass

@dataclass
class Slot:
    slot_id: str
    size: str
    distance: float
    is_available: bool = True
    is_reserved: bool = False
    has_charger: bool = False