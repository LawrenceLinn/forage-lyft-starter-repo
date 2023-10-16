from abc import ABC, abstractmethod
from datetime import date
import numpy as np
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery
from tires.carrigan_tires import CarriganTires
from tires.octoprime_tires import OctoprimeTires


class CarFactory(ABC):
    def __init__(self) -> None:
        pass

    def create_calliope(
        self,
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        worn: np.array,
    ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(worn)
        car = Car(engine, battery, tires)
        return car

    def create_glissade(
        self,
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        worn: np.array,
    ) -> Car:
        engine = CapuletEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(worn)
        car = Car(engine, battery, tires)
        return car

    def create_palindrome(
        self,
        current_date: date,
        last_service_date: date,
        warning_light_on: bool,
        worn: np.array,
    ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(worn)
        car = Car(engine, battery, tires)
        return car

    def creaete_rorschach(
        self,
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        worn: np.array,
    ) -> Car:
        engine = SternmanEngine(last_service_mileage, current_mileage)
        battery = SpindlerBattery(last_service_date, current_date)
        tires = OctoprimeTires(worn)
        car = Car(engine, battery, tires)
        return car

    def create_thovex(
        self,
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
        worn: np.array,
    ) -> Car:
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tires = CarriganTires(worn)
        car = Car(engine, battery, tires)
        return car
