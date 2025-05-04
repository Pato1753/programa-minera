us_y_contra = {}

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
    us_y_contra[usuario] = contra2
    inicio_sesion()


def inicio_sesion():
    print("Inicio de sesion")
    if us_y_contra == False:
        print("No hay usuarios registrados")
        menu_inicial()
    usuario = input("Ingrese su usuario: ")
    contra = input("Ingrese su contraseña: ")
    if usuario not in us_y_contra:
        print("Usuario no resgistrado")
        menu_inicial()
    if contra != us_y_contra[usuario]:
        print("El la contraseña no es correcta")
        inicio_sesion()
    else:
        menu_usuario()
registro()


def menu_usuario():
    print("Bienvenido")
    print("¿Que desea realilizar?")
    print("1. calcular porcentaje de ley de un mineral")
    print("2. Conversion de unidades")
    print("3. Menu minerales")
    print("4. Cerrar sesion")
    try:
        opcion = int(input("Ingrese la accion que quiere realizar (1, 2, 3,...): "))
        if opcion < 0:
            print("Ingrese un valor positivo")
            menu_inicial()
        elif opcion > 6:
            print("Ingrese un valor dentro de rango (1 - 6)")   #Cambiar el rango,este puede variar
            menu_inicial()
    except ValueError:
        print("Ingrese un valor numerico")
        menu_inicial()
    if opcion == 1:
        inicio_sesion()
    elif opcion == 2:
        registro()
    elif opcion == 3:
        pass
    elif opcion == 4:       #Cambiar el rango,este puede variar
        pass
    elif opcion == 5:
        pass
    else:
        print("Sesion cerrada")