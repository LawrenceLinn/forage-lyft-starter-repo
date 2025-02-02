from .engine import Engine


class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int) -> None:
        self.last_service_mileage = last_service_mileage
        self.current_mileage = current_mileage

    def need_service(self) -> bool:
        return self.current_mileage - self.last_service_mileage > 60000
