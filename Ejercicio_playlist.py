

playlist = {}  # Objeto vacío
playlist['canciones'] = []  # Array de canciones dentro de la playlist


#FUNCIÓN PRINCIPAL
def app():
    # Comprobar si ha escrito el nombre de la playlist
    repetir_pregunta = True

    while repetir_pregunta:

        nombre_playlist = input('¿Cómo quieres llamar la playlist?\r\n')

        if nombre_playlist:
            # Ha escrito un nombre válido
            playlist['nombre'] = nombre_playlist
            repetir_pregunta = False
            agregar_canciones()


# FUNCIÓN AGREGAR CANCIONES
def agregar_canciones():
    # Comprobar si se quieren seguir agregando canciones
    agregar_nueva_cancion = True

    while agregar_nueva_cancion:
        # Preguntar qué canción quiere agregar
        pregunta = f'\r\nAgrega canciones para la playlist {playlist["nombre"]}\r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones\r\n'

        cancion = input(pregunta)

        # Comprobar qué ha puesto en 'cancion'
        if cancion == 'X':
            # Si cancion es 'X' parar
            agregar_nueva_cancion = False
            mostrar_resumen()

        elif cancion:
            # Guardar nombre de cancion
            playlist['canciones'].append(cancion)
            print(playlist)


# FUNCIÓN MOSTRAR RESUMEN DE LA PLAYLIST
def mostrar_resumen():

    # Mostrar mensaje
    print(f'\r\nPlaylist:\r\n{playlist["nombre"]}\r\n')
    print('Canciones:')

    # Mostrar las canciones
    for cancion in playlist['canciones']:
        print (cancion)



app()