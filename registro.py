class Registro:
    __temp = int
    __hum = int
    __pre = int

    def __init__(self, temperatura=0, humedad=0, presion=0):
        self.__temp = temperatura
        self.__hum = humedad
        self.__pre = presion

    def getPresion(self):
        return self.__pre
    
    def getTemperatura (self):
        return self.__temp
    
    def getHumedad (self):
        return self.__hum