from .battery import Battery
from datetime import date


class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        pass
