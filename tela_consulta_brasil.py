import customtkinter as ctk
from tela_base import limpar_conteudo


def tela_consulta_brasil(frame):
    limpar_conteudo(frame)
    ctk.CTkLabel(frame,
                 text='Sistema Consulta Brasil',
                 font=('Arial', 22, 'bold')).pack(pady=25)
    ctk.CTkLabel(frame,
                 text='Use esta tela para inserir CEPs, CNPJs ou outros dados que você queira consultar.',
                 font=('Arial', 14),
                 wraplength=520,
                 justify='left').pack(pady=10)
