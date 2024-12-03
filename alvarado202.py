#vanessa abigail alvardo elizalde #
#realizar un listado de estudiante tomando en cuenta  la siguentes cosas##
#DNI, Apellidos, Nombre, Nota,Calificación#
##
alumnos = []
###calificación
def calcular_calificacion(nota):
    if nota < 5:        #si no siguiente#
        return "SS"
    elif 5 <= nota < 7:
        return "AP"
    elif 7 <= nota < 9:
        return "NT"
    return "SB"
def mostrar_alumnos():#mostrar alumnos
    if not alumnos:
        print("no hay alumnos registrados.")
        return
    for alumno in alumnos:
        print(f"{alumno['DNI']} {alumno['Apellidos']}, {alumno['Nombre']} {alumno['Nota']:.1f} {alumno['Calificación']}") 

def introducir_alumno():
    dni = input("DNI: ")
    if any(a["DNI"] == dni for a in alumnos):
        print("ya existe un alumno con ese DNI.")
        return
    apellidos = input("apellidos: ")
    nombre = input("nombre: ")
    nota = float(input("nota: "))
    calificacion = calcular_calificacion(nota)
    alumnos.append({"DNI": dni, "Apellidos": apellidos, "Nombre": nombre, "Nota": nota, "Calificación": calificacion})
    print("Alumno añadido.")

# eliminar 
def eliminar_alumno():
    dni = input("DNI del alumno a eliminar: ")
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            alumnos.remove(alumno)
            print("alumno eliminado.")
            return
    print("No se encontró un alumno con ese DNI.")

# consultar DNI
def consultar_alumno():
    dni = input("DNI: ")
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            print(f"nota: {alumno['Nota']:.1f}, Calificación: {alumno['Calificación']}")
            return
    print("no se encontró un alumno con ese DNI.")

# modificar la nota 
def modificar_nota():
    dni = input("DNI: ")
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            nueva_nota = float(input("Nueva nota: "))
            alumno["nota"] = nueva_nota
            alumno["calificación"] = calcular_calificacion(nueva_nota)
            print("nota actualizada.")
            return
    print("no se encontró un alumno con ese DNI.")


def mostrar_suspensos():
    suspensos = [a for a in alumnos if a["Nota"] < 5]
    if not suspensos:
        print("no hay alumnos suspensos.")
    else:
        for alumno in suspensos:
            print(f"{alumno['DNI']} {alumno['Apellidos']}, {alumno['Nombre']} {alumno['Nota']:.1f} {alumno['Calificación']}")


def mostrar_aprobados():
    aprobados = [a for a in alumnos if a["Nota"] >= 5]
    if not aprobados:
        print("no hay alumnos aprobados.")
    else:
        for alumno in aprobados:
            print(f"{alumno['DNI']} {alumno['Apellidos']}, {alumno['Nombre']} {alumno['Nota']:.1f} {alumno['Calificación']}")

def mostrar_candidatos_mh():
    candidatos = [a for a in alumnos if a["Nota"] == 10]
    if not candidatos:
        print("no hay candidatos a matrícula de honor.")
    else:
        for alumno in candidatos:
            print(f"{alumno['DNI']} {alumno['Apellidos']}, {alumno['Nombre']} {alumno['Nota']:.1f} {alumno['Calificación']}")

# modificar calificación manualmente
def modificar_calificacion():
    dni = input("DNI: ")
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            nueva_calificacion = input("new calificación (SS, AP, NT, SB): ").upper()
            if nueva_calificacion in ["SS", "AP", "NT", "SB"]:
                alumno["calificación"] = nueva_calificacion
                print("calificación modificada.")
            else:
                print("calificación no válida.")
            return
    print("no se encontró un alumno con ese DNI.")

def menu():#menu de opciones 1-9#
    opciones = {
        "1": mostrar_alumnos,
        "2": introducir_alumno,
        "3": eliminar_alumno,
        "4": consultar_alumno,
        "5": modificar_nota,
        "6": mostrar_suspensos,
        "7": mostrar_aprobados,
        "8": mostrar_candidatos_mh,
        "9": modificar_calificacion,
    }
#vamos a utilizar el while true#
    while True:
        print("\n1. mostrar alumnos\n2. Introducir alumno\n3. Eliminar alumno\n4. Consultar alumno")
        print("5. modificar nota\n6. Mostrar suspensos\n7. Mostrar aprobados\n8. Candidatos a MH\n9. Modificar calificación\n0. Salir")
        opcion = input("Opción: ")
        if opcion == "0":
            print("saliendo...")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("opción no válida.")

#fin
if __name__ == "__main__":
    menu()
