# Objeto
# Accediendo a propiedades y comportamientos (pseudocódigo)

# OBJETO

#     Accediendo a propiedades de objetos desde código (pseudocódigo)

#         miCoche.color = 'rojo'
#         miCoche.peso = 1500
#         miCoche.ancho = 2000
#         miCoche.alto = 900

#     Accediendo a comportamiento de objeto desde código (pseudocódigo)

#         miCoche.arranca()
#         miCoche.frena()
#         miCoche.gira()
#         miCoche.acelera()



class Coche():
    
    # propiedades o ESTADO_INICIAL

    def __init__(self):

        self.__largoChasis = 250
        self.__anchoChasis = 120
        self.__ruedas = 4
        self.__enmarcha = False

    # comportamientos o MÉTODOS

    def arrancar(self,arrancamos):
        self.__enmarcha = arrancamos
        chequeo = self.__chequeoInterno()

        if(self.__enmarcha and chequeo):
            return 'El coche está en marcha'

        else:
            return 'El coche no está enmarhca'


    def estado(self):

        print('El coche tiene', self.__ruedas,'ruedas, un ancho de',self.__anchoChasis, 'y un largo de',
            self.__largoChasis)
    

    def __chequeoInterno(self):
    
        print('Realizando chequeo interno...')

        self.gasolina = 'ok'
        self.aceite = 'ok'
        self.puertas = 'cerradas'

        if(self.gasolina == 'ok' and self.aceite == 'ok' and self.puertas == 'cerradas'):
            print('Todo correcto.')
            return True
            
        
        else:
            print('Algo ha ido mal en el chequeo.')
            return False
            
    

    

# Crear Objetos (Instanciar una clase)

Mercedes = Coche()

print(Mercedes.arrancar(True))
Mercedes.estado()

print('\n-------------A contunuación crearemos el segundo objeto------------\n')

Ferrari = Coche()

print(Ferrari.arrancar(False))
Ferrari.estado()


