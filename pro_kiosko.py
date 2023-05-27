from tkinter import W, Button, Entry, IntVar, Label, Radiobutton, StringVar, Tk, ttk
from tkinter.messagebox import askquestion

root = Tk()
root.title("Maxikiosco")

# variable para guardar id provisorio sera eliminado cuando ingresemos los datos a una bd
id_prod = 0
# variables donde almaceno temporalmente los valores ingresados
var_prod = StringVar()
var_desc = StringVar()
var_costo = IntVar()
var_venta = IntVar()
var_provee = StringVar()
var_stock = IntVar()


def click_btn_4():
    response = askquestion(title="salir", message="Esta seguro que desea salir?")
    if response == "yes":
        root.quit()


# funcion que elimina el label generado para mostrar que se guardo correctamente el prod!
def hide_lbl(label):
    label.destroy()


# btn_1 agrega al tree view el prod nuevo, cuando este la bd se agregara a la misma verificando previamente que exista o no
def click_btn_1():
    global id_prod
    id_prod += 1
    tree.insert(
        "",
        "end",
        text=str(id_prod),
        values=(
            var_prod.get(),
            var_desc.get(),
            var_costo.get(),
            var_venta.get(),
            var_provee.get(),
            var_stock.get(),
            radio_sel.get(),
        ),
    )
    txt_lbl = Label(root, text=f"{entry_1.get()} se guardo correctamente")
    txt_lbl.grid(row=0, column=1)
    root.after(3000, lambda: hide_lbl(txt_lbl))
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
    entry_3.delete(0, "end")
    entry_4.delete(0, "end")
    entry_5.delete(0, "end")
    entry_6.delete(0, "end")


# btn_3 elimina el prod seleccionado en el treeview
def click_btn_3():
    global id_prod
    item = tree.focus()
    tree.delete(item)
    id_prod -= 1


# Defino los radio button del iva y por default selecciono si
radio_sel = IntVar()
radio_sel.set(value=True)
iva_yes = Radiobutton(root, text="Si", value=True, variable=radio_sel)
iva_yes.grid(row=2, column=3)
iva_no = Radiobutton(root, text="No", value=False, variable=radio_sel)
iva_no.grid(row=2, column=4)

# defino las etiquetas a usar

labels = ["Producto", "Descripcion", "Costo", "Precio de venta", "Proveedor", "Stock"]
row_count = 0
for etiqueta in labels:
    label_1 = Label(root, text=etiqueta)
    label_1.grid(row=row_count, column=0, sticky="w")
    row_count += 1
label_7 = Label(root, text="Incluye iva?: ")
label_7.grid(row=2, column=2, sticky="w")

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

# genero los botones que tendran funcionalidad
btn_1 = Button(root, text="Agregar", command=click_btn_1)
btn_1.grid(row=3, column=3)
btn_2 = Button(root, text="Modificar", command=click_btn_1)
btn_2.grid(row=4, column=3)
btn_3 = Button(root, text="Eliminar", command=click_btn_3)
btn_3.grid(row=5, column=3)
btn_exit = Button(root, text="Salir", command=click_btn_4, width=20)
btn_exit.grid(row=7, column=1)

# treeview muestra todos los prod ingresados, cuando haya bd se cargaran los datos que ya esten en la bd


tree = ttk.Treeview(root)
tree["columns"] = ("col1", "col2", "col3", "col4", "col5", "col6", "col7")
tree.column("#0", width=50, minwidth=50, anchor=W)
tree.column("col1", width=80, minwidth=80, anchor=W)
tree.column("col2", width=80, minwidth=80, anchor=W)
tree.column("col3", width=80, minwidth=80, anchor=W)
tree.column("col4", width=80, minwidth=80, anchor=W)
tree.column("col5", width=80, minwidth=80, anchor=W)
tree.column("col6", width=80, minwidth=80, anchor=W)
tree.column("col7", width=80, minwidth=80, anchor=W)
tree.grid(column=0, row=6, columnspan=4)
root.mainloop()
