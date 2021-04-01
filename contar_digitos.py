#  Práctica  contar  los  dígitos  de  un  número

NumeroIntroducido = int(input("Introduce un número: "))
digitos = 1

if NumeroIntroducido > 0:

    divisor = 10

    while NumeroIntroducido > divisor:
        #divisor = divisor * 10
        divisor *= 10
        digitos += 1
        
    if divisor ==10:
        print (f"El número tiene {digitos} dígito")
    else:
        print (f"El número tiene {digitos} dígitos")

if NumeroIntroducido < 0:

    divisor = -10
    
    while NumeroIntroducido < divisor:
        divisor *= 10
        digitos += 1
        
    if divisor == -10:
        print (f"El número tiene {digitos} dígito")
    else:
        print (f"El número tiene {digitos} dígitos")