from .engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool) -> None:
        self.warning_light_is_on = warning_light_on

    def need_service(self) -> bool:
        if self.warning_light_is_on:
            return True
        else:
            return False
