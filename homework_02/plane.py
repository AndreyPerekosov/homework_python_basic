import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle


class Plane(Vehicle):

    def __init__(self, weight, fuel=0, fuel_consumption=1, max_cargo=0):
        super().__init__(weight, fuel, fuel_consumption)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, add_cargo):
        if add_cargo + self.cargo <= self.max_cargo:
            self.cargo += add_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        tmp_cargo = self.cargo
        self.cargo = 0
        return tmp_cargo
