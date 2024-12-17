import customtkinter as ctk

class ValidarCodigoWindow(ctk.CTkToplevel):
    def __init__(self, master, title, message):
        super().__init__(master)
        self.title(title)
        self.geometry("300x150")
        self.resizable(False, False)

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (300 // 2)
        y = (screen_height // 2) - (150 // 2)

        self.geometry(f"300x150+{x}+{y}")

        self.label = ctk.CTkLabel(self, text=message)
        self.label.pack(pady=(20, 5))

        self.entry = ctk.CTkEntry(self, placeholder_text="Digite o código", width=200)
        self.entry.pack(pady=(5, 10))

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(pady=(5, 10))

        self.ok_button = ctk.CTkButton(self.button_frame, text="OK", command=self.on_ok, width=95)
        self.ok_button.pack(side="left", padx=5)

        self.cancel_button = ctk.CTkButton(self.button_frame, text="Cancelar", command=self.on_cancel, width=95)
        self.cancel_button.pack(side="right", padx=5)

        self.result = None

    def on_ok(self):
        self.result = self.entry.get()
        self.destroy()

    def on_cancel(self):
        self.result = None
        self.destroy()

    def get_result(self):
        return self.result
