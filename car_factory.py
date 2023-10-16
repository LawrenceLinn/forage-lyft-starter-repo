from abc import ABC, abstractmethod
from datetime import datetime
from car import Car
from engine.engine import Engine
from battery.battery import Battery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery


class CarFactory(ABC):
    def __init__(self) -> None:
        pass

    def create_calliope(
        self,
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_glissade(
        self,
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_palindrome(
        self,
        current_date: datetime,
        last_service_date: datetime,
        warning_light_on: bool,
    ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
    
    def creaete_rorschach(
        self,
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = SternmanEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car

    def create_thovex(
        self,
        current_date: datetime,
        last_service_date: datetime,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        car = Car(engine, battery)
        return car
