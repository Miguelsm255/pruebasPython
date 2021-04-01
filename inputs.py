#Inputs del usuario

#nombre = input('¿Cómo te llamas? \r\n Nombre: ')    # \r\n aplica un salto de línea

#print(f'Hola {nombre}')


#Leer datos que son números

edad = int(input('¿Cuántos años tienes? \r\n Edad: '))

if edad >= 18:
    print('Ya puedes votar')
else:
    print('Aún no puedes votar')
