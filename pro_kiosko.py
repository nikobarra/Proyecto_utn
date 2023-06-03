import sqlite3
from tkinter import (
    W,
    Button,
    DoubleVar,
    Entry,
    IntVar,
    Label,
    LabelFrame,
    StringVar,
    Tk,
    ttk,
)
from tkinter import messagebox
from tkinter.messagebox import askquestion


# creo la base de datos y la conexion
def create_base():
    conn = sqlite3.connect("kiosko.db")
    return conn


# creo las tablas en caso de no existir con sus campos correspondientes
def create_tabla(conn):
    cursor = conn.cursor()
    sql = "CREATE TABLE IF NOT EXISTS productos(id integer PRIMARY KEY AUTOINCREMENT, product text, description text, cost float, price float, provider text, stock integer)"
    cursor.execute(sql)
    conn.commit()


conn = create_base()
create_tabla(conn)
btn2press = False


# Alta de productos y modificacion
def save_data():
    cursor = conn.cursor()
    product = var_prod.get()
    description = var_desc.get()
    cost = var_costo.get()
    price = var_venta.get()
    provider = var_provee.get()
    stock = var_stock.get()
    data = (product, description, cost, price, provider, stock)

    if (btn2press):
        cursor.execute("UPDATE productos SET product = ?, description = ?, cost = ?, price = ?, provider = ?, stock = ? WHERE id = ?", (product, description, cost, price, provider, stock, mi_id))
    else:
        sql = "INSERT INTO productos(product,description, cost, price, provider, stock) VALUES(?, ?, ?, ?, ?, ?)"
        cursor.execute(sql, data)
    conn.commit()
    correct_save()
    carga_tree()


# Valida las entradas para evitar guardar campos vacios
def validate_entry():
    if ((len(var_prod.get()) != 0) and ((len(var_desc.get())) != 0) and ((len(str(var_costo.get()))) != 0) and (len(str(var_venta.get())) != 0) and (len(var_provee.get()) != 0) and (len(str(var_stock.get())) != 0)):
        save_data()
    else:
        messagebox.showwarning('Advertencia',
                               'Por favor, completa todos los campos')


root = Tk()
root.title("Maxikiosco")
root.resizable(0, 0)


# variable para guardar id provisorio sera eliminado
# cuando ingresemos los datos a una bd
# variables donde almaceno temporalmente los valores ingresados
var_prod = StringVar()
var_desc = StringVar()
var_costo = DoubleVar()
var_venta = DoubleVar()
var_provee = StringVar()
var_stock = IntVar()


# funcion para limpiar los campos
def clean_all():
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
    entry_3.delete(0, "end")
    entry_4.delete(0, "end")
    entry_5.delete(0, "end")
    entry_6.delete(0, "end")


# salir del programa
def click_btn_exit():
    response = askquestion(title="salir",
                           message="Esta seguro que desea salir?")
    if response == "yes":
        root.quit()


# funcion que elimina el label generado para mostrar
# que se guardo correctamente el prod!
def hide_lbl(label):
    label.destroy()


def correct_save():
    txt_lbl = Label(root, text=f"{entry_1.get()} se guardo correctamente")
    txt_lbl.grid(row=0, column=1)
    root.after(3000, lambda: hide_lbl(txt_lbl))


def carga_tree():
    tree.grid(column=0, row=7, columnspan=6)
    # bucle para limpiar el tree antes de cargar por
    # si tenia datos y no duplique
    for item in tree.get_children():
        tree.delete(item)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    products = cursor.fetchall()
    for product in products:
        tree.insert(
            "",
            "end",
            values=(product[0],
                    product[1],
                    product[2],
                    product[3],
                    product[4],
                    product[5],
                    product[6]),
        )


def click_btn_1():
    validate_entry()
    clean_all()


def click_btn_2():
    clean_all()
    global btn2press
    global mi_id
    btn2press = True
    item = tree.focus()
    valor = tree.item(item)["values"]
    entry_1.insert(0, valor[1])
    entry_2.insert(0, valor[2])
    entry_3.insert(0, valor[3])
    entry_4.insert(0, valor[4])
    entry_5.insert(0, valor[5])
    entry_6.insert(0, valor[6])
    mi_id = valor[0]
    tree.grid_remove()


# btn_3 elimina el prod seleccionado en el treeview de la bd
def click_btn_3():
    if tree.focus():
        item = tree.focus()
        valor = tree.item(item)["values"]
        cursor = conn.cursor()
        del_value = valor[0]
        data = (del_value,)
        sql = "DELETE FROM productos WHERE id = ?"
        cursor.execute(sql, data)
        conn.commit()
        carga_tree()
    else:
        messagebox.showwarning('Advertencia', 'No hay productos seleccionados')


def click_btn_4():
    carga_tree()


# defino las etiquetas a usar

labels = ["Producto",
          "Descripcion",
          "Costo",
          "Precio de venta",
          "Proveedor",
          "Stock"]
row_count = 0
for etiqueta in labels:
    label_1 = Label(root, text=etiqueta)
    label_1.grid(row=row_count, column=0, sticky="w")
    row_count += 1


# Defino los campos donde se ingresara el texto

entry_1 = Entry(root, textvariable=var_prod, width=100)
entry_1.grid(row=0, column=1)
entry_2 = Entry(root, textvariable=var_desc, width=100)
entry_2.grid(row=1, column=1)
entry_3 = Entry(root, textvariable=var_costo, width=100)
entry_3.grid(row=2, column=1)
entry_4 = Entry(root, textvariable=var_venta, width=100)
entry_4.grid(row=3, column=1)
entry_5 = Entry(root, textvariable=var_provee, width=100)
entry_5.grid(row=4, column=1)
entry_6 = Entry(root, textvariable=var_stock, width=100)
entry_6.grid(row=5, column=1)

# labelframe pra agrupar los botones
btn_group = LabelFrame(root, text="Acciones", padx=10, pady=10)
btn_group.grid(row=6, column=1)

# genero los botones que tendran funcionalidad
btn_1 = Button(btn_group, text="Agregar", command=click_btn_1, cursor="hand2")
btn_1.grid(row=3, column=1, padx=5, pady=5)
btn_2 = Button(btn_group, text="Modificar",
               command=click_btn_2, cursor="hand2")
btn_2.grid(row=3, column=2, padx=5, pady=5)
btn_3 = Button(btn_group, text="Eliminar", command=click_btn_3, cursor="hand2")
btn_3.grid(row=3, column=3, padx=5, pady=5)
btn_4 = Button(btn_group, text="Ver todos",
               command=click_btn_4,
               cursor="hand2")
btn_4.grid(row=3, column=4, padx=5, pady=5)
btn_exit = Button(root, text="Salir",
                  command=click_btn_exit,
                  width=20, cursor="hand2")
btn_exit.grid(row=8, column=1, padx=10, pady=10)

# treeview muestra todos los prod ingresados

tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")
tree.column("#0", width=20, minwidth=20, anchor=W)
tree.column("col1", width=20, minwidth=20, anchor=W)
tree.column("col2", width=80, minwidth=80, anchor=W)
tree.column("col3", width=150, minwidth=80, anchor=W)
tree.column("col4", width=80, minwidth=80, anchor=W)
tree.column("col5", width=80, minwidth=80, anchor=W)
tree.column("col6", width=80, minwidth=80, anchor=W)
tree.column("col7", width=80, minwidth=80, anchor=W)

tree.heading("col1", text="ID")
tree.heading("col2", text="Prod")
tree.heading("col3", text="Desc")
tree.heading("col4", text="Costo")
tree.heading("col5", text="$ Vta")
tree.heading("col6", text="Proveedor")
tree.heading("col7", text="Stock")

# limpio todos los campos para eliminar los valores por default
clean_all()
root.mainloop()
