from abc import ABC, abstractmethod

class Calculator(ABC):
    @abstractmethod
    def clalc_plus(self):
        pass

    @abstractmethod
    def clalc_minus(self):
        pass

    @abstractmethod
    def clalc_multiplied(self):
        pass

    @abstractmethod
    def clalc_divide(self):
        pass