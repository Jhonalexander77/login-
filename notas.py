usuarios = {}  # Guardamos usuario: contraseña
notas = {}     # Guardamos estudiante: nota
cursos = {}    # Guardamos estudiante: [lista de cursos]


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

#historia Us2
def registrar_usuario():
    user = input("Escribe tu usuario: ")
    pwd = input("Escribe tu contraseña: ")
    if user and pwd:
        usuarios[user] = pwd
        cursos[user] = []
        print("Usuario registrado correctamente.\n")


def login():
    user = input("Escribe tu usuario: ")
    pwd = input("Escribe tu contraseña: ")
    if usuarios.get(user) == pwd:
        print(f"\nBienvenido, {user}!")
        menu_principal(user)
    else:
        print("Usuario o contraseña incorrectos.\n")

  #historia Us003  
def menu_principal(user):
    while True:
        if user == "profesor":
            print("1. Registrar Notas")
            print("2. Salir")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                registrar_notas()
            elif opcion == "2":
                break
            else:
                print("Opción no válida.\n")
        else:
            print("1. Crear Curso")
            print("2. Ver mis Cursos")
            print("3. Consultar Nota")
            print("4. Salir")
            opcion = input("Elige una opción: ")
            if opcion == "1":
                crear_curso_estudiante(user)
            elif opcion == "2":
                ver_mis_cursos(user)
            elif opcion == "3":
                consultar_notas(user)
            elif opcion == "4":
                break
            else:
                print("Opción no válida.\n")
                
#historia de Us004
def crear_curso_estudiante(user):
    nombre_curso = input("Escribe el nombre de tu curso: ")
    if nombre_curso:
        if nombre_curso in cursos[user]:
            print("Ya tienes este curso registrado.\n")
        else:
            cursos[user].append(nombre_curso)
            print(f"Te has registrado en el curso '{nombre_curso}'.\n")

def ver_mis_cursos(user):
    if cursos[user]:
        print("Tus cursos son:")
        for curso in cursos[user]:
            print(f"- {curso}")
        print()
    else:
        print("Aún no tienes cursos registrados.\n")

def consultar_notas(user):
    nota = notas.get(user)
    if nota is not None:
        print(f"Tu nota es: {nota}\n")
    else:
        print("Aún no tienes una nota registrada.\n")



#historia de Us005
def registrar_notas():
    estudiante = input("Nombre del estudiante: ")
    if estudiante not in usuarios:
        print("El estudiante no existe.\n")
        return
    nota = input("Nota (0-5): ")
    try:
        nota = float(nota)
        notas[estudiante] = nota
        print("Nota registrada correctamente.\n")
    except ValueError:
        print("Debes ingresar un número válido.\n")