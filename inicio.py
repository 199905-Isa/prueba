# Diccionario que almacena los usuarios y contraseñas
usuarios = {
    "usuario1": "contraseña1",
    "usuario2": "contraseña2",
    "usuario3": "contraseña3"
}

def inicio_sesion():
    print("Bienvenido al sistema de inicio de sesión.")

    # Solicitar nombre de usuario
    usuario = input("Ingrese su nombre de usuario: ")

    # Verificar si el usuario existe en el diccionario
    if usuario in usuarios:
        # Solicitar contraseña
        contraseña = input("Ingrese su contraseña: ")

        # Verificar si la contraseña es correcta
        if usuarios[usuario] == contraseña:
            print("Inicio de sesión exitoso. ¡Bienvenido, {}!".format(usuario))
        else:
            print("Contraseña incorrecta. Por favor, inténtelo de nuevo.")
    else:
        print("Usuario no encontrado. Por favor, verifique su nombre de usuario.")


# Llamar a la función de inicio de sesión
inicio_sesion()