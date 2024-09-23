import customtkinter as ctk
from controller import AppController

ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("blue") 

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Inicializa o controller
        self.controller = AppController(self)

if __name__ == "__main__":
    app = App() 
    app.mainloop()
