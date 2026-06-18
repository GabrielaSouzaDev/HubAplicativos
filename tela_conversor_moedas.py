import customtkinter as ctk
from tela_base import limpar_conteudo


def tela_conversor_moedas(frame):
    limpar_conteudo(frame)
    ctk.CTkLabel(frame,
                 text='Conversor de Moedas',
                 font=('Arial', 22, 'bold')).pack(pady=25)
    ctk.CTkLabel(frame,
                 text='Converta valores entre diferentes moedas aqui.',
                 font=('Arial', 14),
                 wraplength=520,
                 justify='left').pack(pady=10)
