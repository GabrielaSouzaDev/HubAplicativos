import customtkinter as ctk
from tela_base import limpar_conteudo


def tela_inicial(frame):
    limpar_conteudo(frame)
    ctk.CTkLabel(frame,
                 text='Bem-vinda ao Hub de Aplicativos',
                 font=('Arial', 24, 'bold')).pack(pady=(30, 10))
    ctk.CTkLabel(frame,
                 text='Escolha uma ferramenta no menu à direita para começar.',
                 font=('Arial', 14)).pack(pady=10)
    ctk.CTkLabel(frame,
                 text='Cada tela carrega seu próprio conteúdo dentro do mesmo painel de conteúdo.',
                 font=('Arial', 12),
                 wraplength=520,
                 justify='left').pack(pady=10)
