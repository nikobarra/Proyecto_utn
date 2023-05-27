from tkinter import Button, Entry, IntVar, Label, Radiobutton, Tk

root = Tk()


def hide_lbl(label):
    label.destroy()


def click_btn_1():
    txt_lbl = Label(root, text=f"{entry_1.get()} se guardo correctamente")
    txt_lbl.grid(row=0, column=1)
    root.after(3000, lambda: hide_lbl(txt_lbl))
    entry_1.delete(0, "end")
    entry_2.delete(0, "end")
    entry_3.delete(0, "end")
    entry_4.delete(0, "end")
    entry_5.delete(0, "end")
    entry_6.delete(0, "end")


# Defino los radio button del iva y por default selecciono si
radio_sel = IntVar()
radio_sel.set(value=True)
iva_yes = Radiobutton(root, text="Si", value=True, variable=radio_sel)
iva_yes.grid(row=2, column=3)
iva_no = Radiobutton(root, text="No", value=False, variable=radio_sel)
iva_no.grid(row=2, column=4)

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
label_7 = Label(root, text="incluye iva?:")
label_7.grid(row=2, column=2, sticky="w")


# Defino los campos donde se ingresara el texto
entry_1 = Entry(root, width=100)
entry_1.grid(row=0, column=1)
entry_2 = Entry(root, width=100)
entry_2.grid(row=1, column=1)
entry_3 = Entry(root, width=100)
entry_3.grid(row=2, column=1)
entry_4 = Entry(root, width=100)
entry_4.grid(row=3, column=1)
entry_5 = Entry(root, width=100)
entry_5.grid(row=4, column=1)
entry_6 = Entry(root, width=100)
entry_6.grid(row=5, column=1)

btn_1 = Button(root, text="Agregar", command=click_btn_1)
btn_1.grid(row=7, column=1)

root.mainloop()
