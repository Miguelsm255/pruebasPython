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

    largoChasis = 250
    anchoChasis = 120
    ruedas = 4
    enmarcha = False

    # comportamientos o MÉTODOS

    def arrancar(self,arrancamos):
        self.enmarcha = arrancamos

        if(self.enmarcha):
            return 'El coche está en marcha'

        else:
            return 'El coche está parado'


    def estado(self):

        print('El coche tiene', self.ruedas,'ruedas, un ancho de',self.anchoChasis, 'y un largo de',
            self.largoChasis)
    

    

# Crear Objetos (Instanciar una clase)

miCoche = Coche()

print(miCoche.arrancar(True))
miCoche.estado()

print('-------------A contunuación crearemos el segundo objeto------------')

miCoche2 = Coche()

print(miCoche2.arrancar(False))
miCoche2.estado()


