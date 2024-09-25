import customtkinter as ctk
from tkinter import messagebox
from tkcalendar import Calendar
import random

class Agendamento:
    def __init__(self, nome, data):
        self.nome = nome
        self.data = data
        self.codigo = random.randint(1000, 9999)
