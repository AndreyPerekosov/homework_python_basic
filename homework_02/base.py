import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):

    def __init__(self, weight=1, fuel=0, fuel_consumption=1):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.fuel > 0:
            self.started = True
        else:
            raise LowFuelError

    def move(self, distance):
        req_fuel = distance * self.fuel_consumption
        if req_fuel <= self.fuel:
            self.fuel -= req_fuel
        else:
            raise NotEnoughFuel
