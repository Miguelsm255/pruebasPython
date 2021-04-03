class Vehiculos():

    def __init__(self,marca,modelo):

        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelera = False
        self.frena = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelera = True
    
    def frenar(self):
        self.frena = True
    
    def estado(self):
        print ('Marca:', self.marca, '\nModelo:', self.modelo, '\nEn marcha:', self.enmarcha,
            '\nAcelerando:', self.acelera, '\nFrenando:', self.frena)
        

class VElectricos(Vehiculos):

    def __init__(self, marca, modelo):

        super().__init__(marca, modelo)
        self.autonomia = 100
    
    def cargarEnergia(self):
        self.cargando = True


class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado = cargar

        if(self.cargado):
            return 'La furgoneta está cargada'
            
        else:
            return 'La furgoneta no está cargada'


class Moto(Vehiculos):

    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.__hcaballito = False

    def caballito(self):
        self.__hcaballito = True

    def estado(self):
        super().estado()
        print('Caballito:', self.__hcaballito)


class biciElectrica(VElectricos):
    pass


miMoto = Moto('Honda', 'CBR')
miMoto.estado()

miFurgoneta = Furgoneta('Renault', 'Kangoo')
miFurgoneta.arrancar()
miFurgoneta.carga(True)

miBici = biciElectrica('orbea', 'ob1500')