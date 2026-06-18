import customtkinter as ctk
from tela_base import limpar_conteudo


def tela_bot_telegram(frame):
    limpar_conteudo(frame)
    ctk.CTkLabel(frame,
                 text='Bot Telegram',
                 font=('Arial', 22, 'bold')).pack(pady=25)
    ctk.CTkLabel(frame,
                 text='Aqui você poderá desenvolver e testar sua integração com o Telegram.',
                 font=('Arial', 14),
                 wraplength=520,
                 justify='left').pack(pady=10)
