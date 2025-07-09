from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import personaDatos as crud

#creacion de ventana
ventana = Tk()
ventana.title("App CRUD Python")
ventana.geometry("1250x700")
ventana.state("normal")
ventana.configure(bg="#f0f0f0")

#variables del sistema
txt_id = StringVar()
txt_dni = StringVar()
txt_nombre = StringVar()
txt_apellido = StringVar()
txt_edad = StringVar()
txt_direccion = StringVar()
txt_correo = StringVar()

#funciones

#creditos
def creditos():
    messagebox.showinfo("Créditos", """Desarrollado por Andres Camilo Lopez V. Este programa es un CRUD básico en Python con Tkinter. Puedes realizar operaciones de creación, lectura, actualización y eliminación de datos.""")

#limpiarCampos
def limpiarCampos():
    txt_id.set("")
    txt_dni.set("")
    txt_nombre.set("")
    txt_apellido.set("")
    txt_edad.set("")
    txt_direccion.set("")
    txt_correo.set("")

#llenarTabla
def llenarTabla():
    try:
        tabla.delete(*tabla.get_children())
        res = crud.findAll()
        personas = res.get("personas")
        for fila in personas:
            row = list(fila)
            row.pop(0)  # Eliminar el ID de la fila
            row = tuple(row)  # Convertir la lista a tupla
            tabla.insert("", "end", text=id, values=row)
    except Exception as ex:
        messagebox.showerror("Error", f"Error al llenar la tabla: {str(ex)}")

#salir del programa
def salir():
    if messagebox.askyesno("Salir", "¿Estás seguro de que quieres salir de la aplicación?"):
        ventana.destroy()

#guardar datos
def guardarDatos():
    try:
        if txt_edad.get().isnumeric():
            per = {
            "dni": txt_dni.get(),
            "nombre": txt_nombre.get(),
            "apellido": txt_apellido.get(),
            "edad": int(txt_edad.get()),
            "direccion": txt_direccion.get(),
            "correo": txt_correo.get()
            }
            res = crud.save(per)
            if res.get("respuesta"):
                messagebox.showinfo("Éxito", res.get("mensaje"))
            else:
                messagebox.showerror("Error", res.get("mensaje"))
        else:
            txt_edad.set("")
            txt_edad.focus()
            messagebox.showerror("Error", "La edad debe ser un número.")
    except ValueError:
        messagebox.showerror("Error", "Por favor, completa todos los campos correctamente.")

#interfaz grafica de usuario
def crearInterfaz():
    global tabla
    fuente = ("Arial", 12, "bold")
    fuente_2 = ("Arial", 12)
    fuente_boton = ("Arial", 12, "bold")
    #creacion de etiquetas
    Label(ventana, text="DNI", bg="#f0f0f0",font=fuente).grid(row=1, column=0, padx=80, pady=10)
    Label(ventana, text="Nombre", bg="#f0f0f0",font=fuente).grid(row=2, column=0, padx=10, pady=10)
    Label(ventana, text="Apellido", bg="#f0f0f0",font=fuente).grid(row=3, column=0, padx=10, pady=10)
    Label(ventana, text="Edad", bg="#f0f0f0",font=fuente).grid(row=4, column=0, padx=10, pady=10)
    Label(ventana, text="Direccion", bg="#f0f0f0",font=fuente).grid(row=5, column=0, padx=10, pady=10)
    Label(ventana, text="Correo", bg="#f0f0f0",font=fuente).grid(row=6, column=0, padx=10, pady=10)

    #creacion de entradas de texto
    e_dni = ttk.Entry(ventana, textvariable=txt_dni, font=fuente_2)
    e_dni.grid(row=1, column=1, padx=10, pady=10)
    e_nombre = ttk.Entry(ventana, textvariable=txt_nombre, font=fuente_2)
    e_nombre.grid(row=2, column=1, padx=10, pady=10)
    e_apellido = ttk.Entry(ventana, textvariable=txt_apellido, font=fuente_2)
    e_apellido.grid(row=3, column=1, padx=10, pady=10)
    e_edad = ttk.Entry(ventana, textvariable=txt_edad, font =fuente_2)
    e_edad.grid(row=4, column=1, padx=10, pady=10)
    e_direccion = ttk.Entry(ventana, textvariable=txt_direccion, font=fuente_2)
    e_direccion.grid(row=5, column=1, padx=10, pady=10)
    e_correo = ttk.Entry(ventana, textvariable=txt_correo, font=fuente_2)
    e_correo.grid(row=6, column=1, padx=10, pady=10)
    
    #creacion de botones
    icon_new = PhotoImage(file="icon/new.png")
    ttk.Button(ventana, text="Guardar", command=guardarDatos, image=icon_new).place(x=10, y=300, width=100, height=30)
    ttk.Button(ventana, text="Actualizar", command=None).place(x=120, y=300, width=100, height=30)
    ttk.Button(ventana, text="Eliminar", command=None).place(x=230, y=300, width=100, height=30)
    ttk.Button(ventana, text="Buscar", command=None).place(x=340, y=300, width=100, height=30)
    
    #tabla Lista de personas
    Label(ventana, text="LISTA DE PERSONAS", bg="#f0f0f0", font=fuente).place(x=700, y=10)
    tabla = ttk.Treeview(ventana)
    tabla.place(x=450, y=40, width=750, height=600)
    tabla["columns"] = ("DNI","EDAD", "NOMBRE", "APELLIDO", "DIRECCION", "CORREO")
    tabla.column("#0", width=0, stretch=NO)
    tabla.column("DNI", anchor=CENTER, width=100)
    tabla.column("EDAD", anchor=CENTER, width=50)
    tabla.column("NOMBRE", anchor=CENTER, width=100)
    tabla.column("APELLIDO", anchor=CENTER, width=100)
    tabla.column("DIRECCION", anchor=CENTER, width=150)
    tabla.column("CORREO", anchor=CENTER, width=160)
    tabla.heading("#0", text="", anchor=CENTER)
    tabla.heading("DNI", text="DNI", anchor=CENTER)
    tabla.heading("NOMBRE", text="NOMBRE", anchor=CENTER)
    tabla.heading("EDAD", text="EDAD", anchor=CENTER)
    tabla.heading("APELLIDO", text="APELLIDO", anchor=CENTER)
    tabla.heading("DIRECCION", text="DIRECCION", anchor=CENTER)
    tabla.heading("CORREO", text="CORREO", anchor=CENTER)
    
    #Menu superior
    menuTop = Menu(ventana, tearoff=0)
    m_archivo = Menu(menuTop)
    m_archivo.add_command(label="Créditos", command=creditos)
    m_archivo.add_command(label="Salir", command=salir)
    menuTop.add_cascade(label="Archivo", menu=m_archivo)
    ventana.config(menu=menuTop)
    
    m_limpiar = Menu(menuTop, tearoff=0)
    m_limpiar.add_command(label="Limpiar campos", command=limpiarCampos)
    menuTop.add_cascade(label="Limpiar", menu=m_limpiar)
    ventana.config(menu=menuTop)
    
    m_crud = Menu(menuTop, tearoff=0)
    m_crud.add_command(label="Guardar", image=icon_new, compound="left")
    m_crud.add_command(label="Consultar")
    m_crud.add_command(label="Actualizar")
    m_crud.add_command(label="Eliminar")
    menuTop.add_cascade(label="CRUD", menu=m_crud)
    

crearInterfaz()

llenarTabla()
#actualzia cambios en la ventana
ventana.mainloop()