import logging

class Solver:
    def __init__(self,params):
        #print(params)
        self.params=params
        self.W = self.params[0][0] * self.params[1][1] - self.params[1][0] * self.params[0][1]
        self.Wx = self.params[2][0] * self.params[1][1] - self.params[1][0] * self.params[2][1]
        self.Wy = self.params[0][0] * self.params[2][1] - self.params[2][0] * self.params[0][1]

    def wynik(self):
        logging.info("X= " + str(self.getX()) + " Y= "+ str(self.getY()))
        print("Wynik : X= " + str(self.getX()) + " Y= "+ str(self.getY()))

    def getX(self):
        return round(self.Wx/self.W,3)

    def getY(self):
        return round(self.Wy/self.W,3)