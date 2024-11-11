import sys
import os
import customtkinter as ctk

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from controller.app_controller import AppController


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Agendamento")
        
        largura = self.winfo_screenwidth()
        altura = self.winfo_screenheight()


        self.geometry(f"{largura}x{altura}+1+1")

        self.controller = AppController(self)
        self.controller.exibir_tela_login()

if __name__ == "__main__":
    app = App()
    app.mainloop()

    #a
