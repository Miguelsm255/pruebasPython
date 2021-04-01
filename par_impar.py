#  Práctica  comprobar  si  un  número  es  par  o  impar

numero = int(input("Introduce un número: "))

resto = numero % 2    # % calcula el resto de una división

if resto == 0 :
    print (f"El número {numero} es par")
else:
    print (f"El número {numero} es impar")