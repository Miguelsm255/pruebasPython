# for i in range(1,100,2):
#     print(i, end=' ')

# #---------------------------------------------------------------------------------

# contraseña = input('Introduce una contraseña: ')

# validez = True

# for i in contraseña:

#     if i == ' ':
#         validez = False


# if len(contraseña) < 8:
#     validez = False


# if validez:
#     print(contraseña, 'es una contraseña válida')
# else:
#     print(contraseña, 'no es una contraseña válida')

# #-------------------------------------------------------------------------------------

# email = input('Introduce tu correo electrónico: ')

# arrobas = 0
# puntos = 0
# validez = True

# for i in range(len(email)):
    
#     if email[i] == '@':
#         arrobas =+1
    
#     if email[i] == '.':
#         puntos =+1
    
#     if email[i] == ' ':
#         validez = False

# if arrobas == 1 and puntos > 0 and validez:
#     print('Dirección de email válida')
# else:
#     print('Dirección de email no váida')

#--------------------------------------------------------------------------------------


# num_introducido = int(input('Introduce un número: '))
# num_anterior = num_introducido - 1

# while num_introducido > num_anterior:

#     num_anterior = num_introducido
#     num_introducido = int(input('Introduce otro número mayor que el anterior: '))

#-------------------------------------------------------------------------------------------

# num_introducido = int(input('Introduce un número positivo: '))
# suma = 0

# while num_introducido > 0:

#     suma = suma + num_introducido
#     num_introducido = int(input('Introduce otro número positivo: '))

# print('la suma de los numeros intoducidos es', suma)
