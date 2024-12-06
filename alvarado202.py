#vanessa abigail alvardo elizalde #
#realizar un listado de estudiante tomando en cuenta  la siguentes cosas##
#DNI, Apellidos, Nombre, Nota,Calificación#
#con interfas grafica #
import tkinter as tk  
from tkinter import messagebox, simpledialog

alumnos = []

### calificación
def calcular_calificacion(nota):###si no  en caso contrario
    ##SS,AP,NT,SB ##
    if nota < 5:
        return "SS"
    elif 5 <= nota < 7:
        return "AP"
    elif 7 <= nota < 9:
        return "NT"
    return "SB"

###mostrar alumnos
def mostrar_alumnos():
    if not alumnos:
        messagebox.showinfo("alumnos", "no hay alumnos registrados.")
        return
    resultado = "\n".join([f"{a['DNI']} {a['Apellidos']}, {a['Nombre']} - {a['Nota']:.1f} ({a['Calificación']})" for a in alumnos])
    messagebox.showinfo("lista de Alumnos", resultado)


def introducir_alumno():# nuevo alumno a la lista 
    dni = simpledialog.askstring("Nuevo Alumno", "Introduce el DNI:")
    if any(a["DNI"] == dni for a in alumnos):
        messagebox.showerror("Error", "Ya existe un alumno con ese DNI.")
        return
    apellidos = simpledialog.askstring("Nuevo Alumno", "Introduce los apellidos:")
    nombre = simpledialog.askstring("Nuevo Alumno", "Introduce el nombre:")
    try:
        nota = float(simpledialog.askstring("Nuevo Alumno", "Introduce la nota:"))
    except ValueError:
        messagebox.showerror("Error", "La nota debe ser un número.")
        return

    calificacion = calcular_calificacion(nota)
    alumnos.append({"DNI": dni, "Apellidos": apellidos, "Nombre": nombre, "Nota": nota, "Calificación": calificacion})
    messagebox.showinfo("Éxito", "Alumno añadido.")

# Función para eliminar un alumno
def eliminar_alumno():
    dni = simpledialog.askstring("Eliminar Alumno", "Introduce el DNI del alumno a eliminar:")
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            alumnos.remove(alumno)
            messagebox.showinfo("Éxito", "Alumno eliminado.")
            return
    messagebox.showerror("Error", "No se encontró un alumno con ese DNI.")

# Función para consultar un alumno
def consultar_alumno():
    dni = simpledialog.askstring("Consultar Alumno", "Introduce el DNI:")
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            resultado = f"Nota: {alumno['Nota']:.1f}, Calificación: {alumno['Calificación']}"
            messagebox.showinfo("Consulta de Alumno", resultado)
            return
    messagebox.showerror("Error", "No se encontró un alumno con ese DNI.")

# aqui vamos vamos a utilizar for    para ver < nota
def mostrar_suspensos():
    suspensos = [a for a in alumnos if a["Nota"] < 5]
    if not suspensos:
        messagebox.showinfo("Suspensos", "No hay alumnos suspensos.")
        return
    resultado = "\n".join([f"{a['DNI']} {a['Apellidos']}, {a['Nombre']} - {a['Nota']:.1f} ({a['Calificación']})" for a in suspensos])
    messagebox.showinfo("Suspensos", resultado)

#aqui vamos a ver quienes aprobados
def mostrar_aprobados():
    aprobados = [a for a in alumnos if a["Nota"] >= 5]
    if not aprobados:
        messagebox.showinfo("Aprobados", "No hay alumnos aprobados.")
        return
    resultado = "\n".join([f"{a['DNI']} {a['Apellidos']}, {a['Nombre']} - {a['Nota']:.1f} ({a['Calificación']})" for a in aprobados])
    messagebox.showinfo("Aprobados", resultado)

# vamos a modificar la nota
def modificar_nota():
    dni = simpledialog.askstring("Modificar Nota", "Introduce el DNI:")
    for alumno in alumnos:
        if alumno["DNI"] == dni:
            try:
                nueva_nota = float(simpledialog.askstring("Modificar Nota", "Introduce la nueva nota:"))
                alumno["Nota"] = nueva_nota
                alumno["Calificación"] = calcular_calificacion(nueva_nota)
                messagebox.showinfo("Éxito", "Nota actualizada.")
                return
            except ValueError:
                messagebox.showerror("Error", "La nota debe ser un número.")
                return
    messagebox.showerror("Error", "No se encontró un alumno con ese DNI.")

# Ventana principal
def main():
    ventana = tk.Tk()
    ventana.title("Gestión de Alumnos")
    
    ventana.geometry("700x500")#("800x200")# aqui estamos dando  medidas de preferencia 
    ventana.resizable(False, False)






    

    # MENU ####
    botones = [ ####opciones disponibles #
        ("Mostrar Alumnos", mostrar_alumnos),
        ("Añadir Alumno", introducir_alumno),
        ("Eliminar Alumno", eliminar_alumno),
        ("Consultar Alumno", consultar_alumno),
        ("Mostrar Suspensos", mostrar_suspensos),
        ("Mostrar Aprobados", mostrar_aprobados),
        ("Modificar Nota", modificar_nota),
    ]

    for texto, comando in botones:
        boton = tk.Button(ventana, text=texto, width=30, height=2, command=comando)
        boton.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
