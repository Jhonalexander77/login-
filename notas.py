#historia de Us1
def menu_inicio():
    while True:
        print("=== Sistema de Cursos y Notas ===")
        print("1. Registrar Usuario")
        print("2. Iniciar Sesión")
        print("3. Salir")
        opcion = input("Elige una opción: ")
        if opcion == "1":
            registrar_usuario() 
        elif opcion == "2":
            login()
        elif opcion == "3":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.\n")

menu_inicio()