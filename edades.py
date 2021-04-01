#  Práctica  de  edades  


edad = int(input("introduce tu edad: "))

if edad < 12 and edad > 0: 
    print ("Eres un niño")
elif edad >= 12 and edad < 18:
    print ("Eres un adolescente")
elif edad >=18:
    print ("Eres mayor de edad")
elif edad <=0:
    print ("¿Cómo vas a tener edad negativa?")