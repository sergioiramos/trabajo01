from tkinter import *

def suma():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 + num2
    label_resultado.config(text="El resultado de la suma es: " + str(resultado))

def resta():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 - num2
    label_resultado.config(text="El resultado de la resta es: " + str(resultado))

def multiplicacion():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    resultado = num1 * num2
    label_resultado.config(text="El resultado de la multiplicación es: " + str(resultado))

def division():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    if num2 != 0:
        resultado = num1 / num2
        label_resultado.config(text="El resultado de la división es: " + str(resultado))
    else:
        label_resultado.config(text="Error: No se puede dividir entre cero.")

# Crear la ventana
ventana = Tk()
ventana.title("Calculadora Básica")

# Etiquetas
label_num1 = Label(ventana, text="Primer número:")
label_num1.pack()

entry_num1 = Entry(ventana)
entry_num1.pack()

label_num2 = Label(ventana, text="Segundo número:")
label_num2.pack()

entry_num2 = Entry(ventana)
entry_num2.pack()

label_resultado = Label(ventana, text="")
label_resultado.pack()

# Botones
boton_suma = Button(ventana, text="Suma", command=suma)
boton_suma.pack()

boton_resta = Button(ventana, text="Resta", command=resta)
boton_resta.pack()

boton_multiplicacion = Button(ventana, text="Multiplicación", command=multiplicacion)
boton_multiplicacion.pack()

boton_division = Button(ventana, text="División", command=division)
boton_division.pack()

# Ejecutar la ventana
ventana.mainloop()

#prueba de git