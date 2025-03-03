import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Gonzalez Abeijon
Nombre: Lucas
Rising BTL. Empresa dedicada a la toma de datos para realizar estadísticas y censos nos pide realizar una carga de datos validada e ingresada 
por ventanas emergentes solamente (para evitar hacking y cargas maliciosas) y luego asignarla a cuadros de textos. 

Los datos requeridos son los siguientes:
    Apellido
    Edad, entre 18 y 90 años inclusive.
    Estado civil, ["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"]
    Número de legajo, numérico de 4 cifras, sin ceros a la izquierda.
'''


class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.label0 = customtkinter.CTkLabel(master=self, text="Apellido")
        self.label0.grid(row=0, column=0, padx=20, pady=10)
        self.txt_apellido = customtkinter.CTkEntry(master=self)
        self.txt_apellido.grid(row=0, column=1)

        self.label1 = customtkinter.CTkLabel(master=self, text="Edad")
        self.label1.grid(row=1, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=1, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Estado")
        self.label2.grid(row=2, column=0, padx=20, pady=10)
        self.combobox_tipo = customtkinter.CTkComboBox(
            master=self, values=["Soltero/a", "Casado/a", "Divorciado/a", "Viudo/a"])
        self.combobox_tipo.grid(row=2, column=1, padx=20, pady=10)

        self.label3 = customtkinter.CTkLabel(master=self, text="Legajo")
        self.label3.grid(row=3, column=0, padx=20, pady=10)
        self.txt_legajo = customtkinter.CTkEntry(master=self)
        self.txt_legajo.grid(row=3, column=1)

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador = 0
        apellido = ""
        edad = None
        estado_civil = ""
        legajo = ""
        while contador < 3:
            apellido = prompt("Tp 5", "Ingrese su apellido")
            contador += 1
            while (apellido == "" or apellido.isdigit()):
                apellido = prompt("Tp 5", "Ingrese un apellido real")


            edad = prompt("Tp 5", "Ingrese su edad")
            edad = int(edad)
            contador += 1
            while not (edad >=18 and edad <= 90):
                alert("Tp 5", "Debes ser mayor de 18 años o menor de 90 años")
                edad = prompt("Tp 5", "Ingrese su edad nuevamente")
                edad = int(edad)

            estado_civil = prompt("Tp 5", prompt="Ingrese su Estado Civil")
            self.combobox_tipo.set(estado_civil)
            while not (estado_civil == "Soltero/a" or estado_civil == "Divorciado/a" or estado_civil == "Casado/a" or estado_civil == "Viudo/a"):
                estado_civil = prompt("Tp 5", "Ingrese un Estado Civil real")
                self.combobox_tipo.set(estado_civil)
            while (estado_civil == None or estado_civil.isdigit()):
                estado_civil = prompt("Tp 5", "Intenta otra vez")
                self.combobox_tipo.set(estado_civil)
            contador += 1
            
            legajo = int(prompt("Tp 5", "Ingrese su numero de legajo"))
            while legajo >= 10000:
                legajo = int(prompt("Tp 5", "Ingresaste mas de 4 digitos"))
            contador += 1
            

            self.txt_apellido.delete(0,10000)
            self.txt_apellido.insert(0,apellido)
            self.txt_edad.delete(0,10000)
            self.txt_edad.insert(0,edad)
            self.txt_legajo.delete(0,10000)
            self.txt_legajo.insert(0,legajo)

            alert(title="Tp 5", message= "Apellido: {0}\n Edad: {1}\n Estado civil: {2}\n Legajo: {3}".format(apellido,edad,estado_civil,legajo))
        
        




if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
