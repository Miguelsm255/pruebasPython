#Crear un diccionario simple

cancion = {
#     key         valor
    "artista" : "Metallica",
    "titulo" : "Enter Sandman",
    "lanzamiento" : 1992,
    "likes" : 3000

}

#Acceder a un valor
print(cancion["artista"])
print(cancion["lanzamiento"])


#Mezclar con un string
artista = cancion.get("artista")  #hay que asignar el valor a una variable
print (f"estoy escuchando {artista}")


#Agregar nuevos valores
cancion ["playlist"] = "heavy metal"
print(cancion)



#Reemplazar valores existentes
cancion ["cancion"] = "Seek & Destroy"
print(cancion)



#Eliminar un valor existente
del cancion["lanzamiento"]
print (cancion)