import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar
import random

class Agendamento:
    def __init__(self, nome, data, horario, local):
        self.nome = nome
        self.data = data
        self.horario = horario
        self.local = local
        self.codigo = random.randint(1000, 9999)
