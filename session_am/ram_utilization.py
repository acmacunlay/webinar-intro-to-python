from dataclasses import dataclass


@dataclass()
class RAMUtilization:
    ram_available: int
    ram_percent: float
