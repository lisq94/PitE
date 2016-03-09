import sys
import logging

from InputReader import InputReader
from InputValidator import InputValidator
from Solver import Solver
from Error import Error

class Application:

    class __Application:
        def __init__(self):
            self.matrix = None

    instance = None
    params = []

    def __init__(self):
        if not Application.instance:
            Application.instance = Application.__Application()
        else:
            Application.instance.matrix = None

    def __getMatrix__(self):
        return self.params

    def pobierzDane(self):
        try:
            self.params = InputReader().getParams()
        except Error as e:
            print(e.message)
            sys.exit()

    def walidacjaDanych(self):
        try:
            InputValidator(self.params).validate()
        except ValueError as e:
            print(e.value)
            sys.exit()

    def print(self):
        print(self.params)

    def rozwiaz(self):
        solver = Solver(self.params)
        solver.wynik()

    def log(self):
        logging.basicConfig(filename='Application_solver.log', level=logging.INFO, format='%(asctime)s %(message)s')


