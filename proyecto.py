'''
Crear un programa que tenga:

    .Ventana
    .Tamaño fijo
    .No redimensionable
    .Un menu (Inicio, Añadir, Información, Salir)
    .Diferentes pantallas
    .Formulario de añadir productos
    .Guardar datos temporalmente
    .Mostrar datos listados en la pantalla home
    .Opcion de salir

'''

from tkinter import *
from tkinter import ttk

# Definir ventana
ventana = Tk()
#ventana.geometry("500x500")
ventana.minsize(500, 500)
ventana.title("Proyecto Tkinter - Master en Python")
ventana.resizable(0,0)

# Pantalla
def home():
    home_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=210,
        pady=20
    )
    home_label.grid(row=0, column=0)

    # Inserto frame de lista de productos
    product_box.grid(row=2)
    # Listar productos en el frame
    '''
    for product in products:
        if len(product) == 3:
            product.append("added")
            Label(product_box, text=product[0]).grid()
            Label(product_box, text=product[1]).grid()
            Label(product_box, text=product[2]).grid()
            Label(product_box, text="_____________________").grid()
    '''
    # Inserto valores a tabla de ttk
    for product in products:
        if len(product) == 3:
            product.append("added")
            product_box.insert("", 0, text=product[0], values = (product[1]))

    # Ocultar otras pantallas
    add_label.grid_remove()
    add_frame.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def add():
    # Encabezado
    add_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=120,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=6)

    # Campos del formulario
    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5, sticky=W)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5, sticky=W)

    add_price_label.grid(row=2, column=0, padx=5, pady=5, sticky=W)
    add_price_entry.grid(row=2, column=1, padx=5, pady=5, sticky=W)

    add_description_label.grid(row=3, column=0, padx=5, pady=5, sticky=NW)
    add_description_entry.grid(row=3, column=1, padx=5, pady=5, sticky=W)
    add_description_entry.config(
        width=30,
        height=5,
        font=("Consolas", 12),
        padx=15,
        pady=15
    )

    add_separator.grid(row=4)

    boton.grid(row=5, column=1)
    boton.config(
        padx=15,
        pady=4,
        bg="green",
        fg="white"
    )

    # Ocultar otras pantallas
    home_label.grid_remove()
    product_box.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    return True

def info():
    info_label.config(
        fg="white",
        bg="black",
        font=("Arial", 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)
    data_label.grid(row=1, column=0)
    # Ocultar otras pantallas
    home_label.grid_remove()
    product_box.grid_remove()
    add_label.grid_remove()
    add_frame.grid_remove()
    return True

def add_product():
    products.append([
        name_data.get(),
        price_data.get(),
        add_description_entry.get("1.0", "end-1c")
    ])
    name_data.set("")
    price_data.set("")
    add_description_entry.delete("1.0", END)

    print(products)

# Variables importantes
products = []
name_data = StringVar()
price_data = StringVar()

# Definir campos de pantalla (Inicio)
home_label = Label(ventana, text="Inicio")

# Definir lista de productos (no hace falta usar frame si usamos tabla)
#product_box = Frame(ventana, width=250)


# Definir tabla para lista de productos
product_box = ttk.Treeview(height=12, columns=2)
# Separacion
Label(ventana).grid(row=1)
# Definir valores tabla
product_box.grid(row=1, column=0, columnspan=2)
product_box.heading("#0", text="Producto", anchor=W)
product_box.heading("#1", text="Precio", anchor=W)


# Definir campos de pantalla (Añadir)
add_label = Label(ventana, text="Añadir producto")
# Definir campos de pantalla (Información)
data_label = Label(ventana, text="Creado por FNF")
info_label = Label(ventana, text="Información")


# Campos del formulario
add_frame = Frame(ventana)
add_name_label = Label(add_frame, text="Nombre:")
add_name_entry = Entry(add_frame, textvariable=name_data)

add_price_label = Label(add_frame, text="Precio:")
add_price_entry = Entry(add_frame, textvariable=price_data)

add_description_label = Label(add_frame, text="Descripción:")
add_description_entry = Text(add_frame)

add_separator = Label(add_frame)

boton = Button(add_frame, text="Guardar", command=add_product)

# Cargar pantalla inicio
home()
#add()

# Definir menu superior
menu_superior = Menu(ventana)
menu_superior.add_command(label="Inicio", command=home)
menu_superior.add_command(label="Añadir", command=add)
menu_superior.add_command(label="Información", command=info)
menu_superior.add_command(label="Salir", command=ventana.quit)

# Cargar menu superior
ventana.config(menu=menu_superior)

# Cargar ventana
ventana.mainloop()