from .calculator import Calculator
import multiprocessing
from logger.logger import log_function_call


class Server(Calculator):
    def __init__(self, connection):
        self.connection = connection

    def clalc_plus(self, num1, num2):
        return num1 + num2

    def clalc_minus(self, num1, num2):
        return num1 - num2

    def clalc_multiplied(self, num1, num2):
        return num1 * num2

    def clalc_divide(self, num1, num2):
        return num1 / num2

    def calculat_numbers(self, num1, num2, opertion):
        if opertion == '+':
            return self.clalc_plus(num1, num2)
        elif opertion == '-':
            return self.clalc_minus(num1, num2)
        elif opertion == '*':
            return self.clalc_multiplied(num1, num2)
        elif opertion == '/':
            return self.clalc_divide(num1, num2)
        else:
            assert False, 'worng opertion was addded'

    @log_function_call('handle_data')
    def handle_data(self):
        while True:
            data = self.connection.recv()
            if data == "exit":
                break
            rerult = self.calculat_numbers(data[0], data[1], data[2])
            self.connection.send(rerult)
