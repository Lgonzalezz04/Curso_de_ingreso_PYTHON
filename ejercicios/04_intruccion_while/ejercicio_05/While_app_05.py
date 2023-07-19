import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter


'''
Apellido:Gonzalez Abeijon
Nombre:Lucas
Enunciado:
Al presionar el botón ‘Validar letra’, mediante prompt solicitar al usuario que ingrese una letra. 
Se deberá validar que la letra sea ‘U’, ‘T’ o ‘N’ (en mayusculas) 
En caso no coincidir con ninguna de las letras, volverla a solicitar hasta que la condición se cumpla
'''


class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
        
        self.btn_validar_letra = customtkinter.CTkButton(master=self, text="Ingresar", command=self.btn_validar_letra_on_click)
        self.btn_validar_letra.grid(row=2, pady=20, columnspan=2, sticky="nsew")
        
    
    def btn_validar_letra_on_click(self):
        letra = prompt(title="Ej 5", prompt= "Ingrese U T o N").upper()
        while not (letra == "U" or letra == "T" or letra == "N"):
            letra = prompt(title="Ej 5", prompt="Error, letra incorrecta").upper()
        alert(title="Ej 5", message=f"La letra {letra} es correcta")
            
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()