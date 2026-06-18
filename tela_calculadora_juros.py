import customtkinter as ctk
from tela_base import limpar_conteudo


def tela_calculadora_juros(frame):
    limpar_conteudo(frame)
    ctk.CTkLabel(frame,
                 text='Calculadora Juros',
                 font=('Arial', 22, 'bold')).pack(pady=25)
    ctk.CTkLabel(frame,
                 text='Calcule juros simples ou compostos sem sair desta tela.',
                 font=('Arial', 14),
                 wraplength=520,
                 justify='left').pack(pady=10)
