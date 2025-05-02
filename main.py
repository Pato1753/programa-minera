usuarios = []
contraseñas = []

def menu_inicial():
    print("BIENVENIDO A LA APLICACION MINAQUINTERO")
    print("¿Que desea realizar?")
    print("1. Iniciar sesion")
    print("2. Registrarce")
    print("3. Cerrar sesion")
    print("")
    try:
        opcion = int(input("Ingrese la accion que quiere realizar (1, 2, 3): "))
        if opcion < 0:
            print("Ingrese un valor positivo")
            menu_inicial()
        elif opcion > 3:
            print("Ingrese un valor dentro de rango (1, 2, 3)")
            menu_inicial()
    except ValueError:
        print("Ingrese un valor numerico")
        menu_inicial()
    if opcion == 1:
        inicio_sesion()
    elif opcion == 2:
        registro()
    else:
        print("Sesion cerrada")

def registro():
    usuario = input("Ingrese su nombre de usuario: ")

    contra1 = input("Ingrese una contraseña: ")
    contra2 = input("Confirme su contraseña: ")
    while contra1 != contra2:
        print("Contraseñas ingresadas no coinciden")
        contra1 = input("Ingrese una contraseña: ")
        contra2 = input("Confirme su contraseña: ")
    usuarios.append(usuario)
    contraseñas.append(contra2)
    inicio_sesion()


def inicio_sesion():
    print("Inicio de sesion")
    
    