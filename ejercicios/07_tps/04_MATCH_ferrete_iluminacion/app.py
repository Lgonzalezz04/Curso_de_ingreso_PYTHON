import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Apellido: Gonzalez Abeijon
Nombre: Lucas
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        # configure window
        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
        
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_calcular_on_click(self):
        marca = self.combobox_marca.get()
        cantidad = int(self.combobox_cantidad.get())
        precio = 800 

        #A. Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%.
        match cantidad:
            case 6 | 7 | 8 | 9 | 10 | 11 | 12:
                precio = (precio * .50) * cantidad


        #B. Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
        match cantidad:
            case 5:
                match marca:
                    case "ArgentinaLuz":
                        precio = (precio * .60) * cantidad
                    case _:
                        precio = (precio * .70) * cantidad

        #C. Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
        match cantidad:
            case 4:
                match marca:
                    case "ArgentinaLuz" | "FelipeLamparas":
                        precio = (precio * .75) * cantidad
                    case _:
                        precio = (precio * .80) * cantidad

        #D. Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
        match cantidad:
            case 3:
                match marca:
                    case "ArgentinaLuz":
                        precio = (precio * .85) * cantidad
                    case "FelipeLamparas":
                        precio = (precio * .90) * cantidad
                    case _:
                        precio = (precio * .95) * cantidad

        #E. Si el importe final con descuento suma más de $4000  se obtien un descuento adicional de 5%.
        if precio  > 4000:
            precio = (precio * .95)
        mensaje = f"El total es: {precio}"
        alert(title="TP 4",message=mensaje)
        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()