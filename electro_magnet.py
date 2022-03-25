class Electro_magnet:

    def __init__(self):
        self._state = False

    def switchOn(self):
        self.state = True

    def switchOff(self):
        self.state = False

    
num1 = Electro_magnet 

num1.switchOn(num1)

print(num1.state)

num1.switchOff(num1)