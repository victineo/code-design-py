import numpy
from typing import List
from .interfaces.driver_handler_interface import DriverHandlerInterface

class NumpyHandler(DriverHandlerInterface):
    def __init__(self):
        self.__np = numpy

    def standart_deviation(self, numbers: List[float]) -> float:
        return self.__np.std(numbers)
    
    def variance(self, numbers: List[float]) -> float:
        return self.__np.var(numbers)