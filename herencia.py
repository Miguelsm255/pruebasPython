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
        

class VElectricos():

    def __init__(self):
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

    hcaballito = ''

    def caballito(self):
        self.hcaballito = 'Estoy haciendo el caballito'
    
        #AQUÍ HAY QUE INSERTAR LA FUNCION 'ESTADO' CON 'CABALLITO' 
        #TODO: Crear funcion 'estado' con 'caballito'


class biciElectrica(Vehiculos,VElectricos):
    pass


miMoto = Moto('Honda', 'CBR')
miMoto.estado()

miFurgoneta = Furgoneta('Renault', 'Kangoo')
miFurgoneta.arrancar()
miFurgoneta.carga(True)

miBici = biciElectrica()