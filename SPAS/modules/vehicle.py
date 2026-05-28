from dataclasses import dataclass


@dataclass
class Vehicle:
    vehicle_id: str
    vehicle_type: str
    size: str
    priority: int
    is_vip: bool = False
    is_electric: bool = False