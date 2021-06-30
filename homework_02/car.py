import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))
from homework_02.base import Vehicle
from homework_02.engine import Engine



class Car(Vehicle):

    def __init__(self, weight, fuel=0, fuel_consumption=1):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = None

    def set_engine(self, engine: Engine):
        self.engine = engine
