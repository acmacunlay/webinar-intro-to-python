import psutil


class ResourceMonitor:
    def __init__(self) -> None:
        pass

    def get_available_ram(self) -> int:
        return psutil.virtual_memory().available

    def get_ram_utilization(self) -> float:
        return psutil.virtual_memory().percent
