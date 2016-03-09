import sys
from Error import Error


class InputValidator:
    _message = ""

    def __init__(self, params):
        self.params=params
        print("Trwa walidacja")

    def validate(self):
        try:
            self.isOznaczony()
        except Error as e:
            print(e.message)
            sys.exit()

    def isOznaczony(self):
        if not self.params[0][0] * self.params[1][1] - self.params[1][0] * self.params[0][1] != 0:
            raise Error("Układ równań nie jest oznaczony!")
