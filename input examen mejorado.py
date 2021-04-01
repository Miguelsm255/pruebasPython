#DECLARACIÓN DE VARIABLES

nota = int(0)
nombre = str
repetir = True
respuesta = str
respuestabool = True
soluciones = [0,1,0,1,0]
soluciones_posibles = [True, False]
solucion_a_respuesta = int
solucionbool = False
numero_pregunta = int(-1)
preguntas = [
    f'\r\n1ª pregunta: \r\n\r\n¿Existe el lenguaje "Python"?',
    f'\r\n2ª pregunta: \r\n\r\n¿Los números son finitos?',
    f'\r\n3ª pregunta: \r\n\r\n¿Youtube es de Google?',
    f'\r\n4ª pregunta: \r\n\r\n¿Toledo está en Madrid?',
    f'\r\n5ª pregunta: \r\n\r\n¿España es un país?'
]



#DECLARACIÓN DE FUNCIONES

#Evaluador
def evaluar():
    global solucionbool
    global respuestabool
    global nota
    if solucionbool == respuestabool:
        nota += 1
        print('\r\nRespuesta correcta!!')
    else:
        print('\r\nRespuesta incorrecta')

#Transformar si/no en booleano
def transsino():
    global respuestabool
    global respuesta
    global repetir
    if respuesta == ('si'):
        respuestabool = True
        repetir = False
    elif respuesta == ('no'):
        respuestabool = False
        repetir = False
    else:
        print('Respuesta no válida')
        repetir = True  



#INICIO EXAMEN

#Preguntar el nombre
nombre = str(input('¿Cómo te llamas? \r\n'))
print(f'\r\nVale {nombre}, comencemos con el cuestionario')

#Preguntas
for pregunta in preguntas:
    
    numero_pregunta += 1
    solucion_a_respuesta = soluciones[numero_pregunta]
    solucionbool = soluciones_posibles[solucion_a_respuesta]

    print(pregunta)
    while repetir == True:
        respuesta = input('Respuesta: ')
        respuesta = respuesta.lower()
        transsino()
    evaluar()
    repetir = True

#Anunciar resultado
print(f'{nombre}, has sacado un {nota}/{numero_pregunta + 1}')
