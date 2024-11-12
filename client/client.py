from logger.logger import log_function_call
import multiprocessing

class Client:
    def __init__(self, connection):
        self.connection = connection
        self.parameterA = ''
        self.parameterB = ''
        self.arithmetic_operation = ''

    @log_function_call('set_parameters_from_user')
    def set_parameters_from_user(self):
        try:
            self.parameterA = int(input('please enter first number: \n'))
            self.parameterB = int(input('please enter second number: \n'))
            self.arithmetic_operation = \
                (input('please enter one of the following arithmetic operation ( -, +, *, /): \n'))
        except ValueError:
            assert False, 'user enter an invlid number'
        except TypeError:
            assert False, 'user enter an invlid arithmetic operation'

    @log_function_call('send_data_to_server')
    def send_data_to_server(self):
        self.connection.send((self.parameterA, self.parameterB, self.arithmetic_operation))

    @log_function_call('recived_data_from_server')
    def recived_data_from_server(self):
        result = self.connection.recv()
        return result

    @log_function_call('print_final_resutl')
    def print_final_resutl(self, result):
        print(f"The result of {self.parameterA}{self.arithmetic_operation}{self.parameterB} = {result}")
