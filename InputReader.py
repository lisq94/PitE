from Error import Error
import logging


class InputReader:
    def __init__(self):
        print("Podaj współczynniki pierwszego równania ax + by = c")
        self.first = input("Podaj w formacie a b c: ")
        print("Podaj współczynniki drugiego równania ax + by = c")
        self.second = input("Podaj w formacie a b c: ")

    def getParams(self):
        self.first = self.first.split(" ")
        self.second = self.second.split(" ")
        try:
            if len(self.first) > 3 or len(self.second) > 3:
                raise IndexError
            if len(self.first) < 3 or len(self.second) < 3:
                raise Error("Podano za mało elementów")
            a = [float(self.first[0]), float(self.second[0])]
            b = [float(self.first[1]), float(self.second[1])]
            c = [float(self.first[2]), float(self.second[2])]
            logging.info("Parametry poczatkowe: " + str([a, b, c]))
        except ValueError:
            raise Error("Jeden z argumentów nie jest liczbą!")
        except IndexError:
            raise Error("Podano za dużo elementów")
        return [a, b, c]
