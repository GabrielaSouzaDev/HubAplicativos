import customtkinter as ctk
from tela_base import limpar_conteudo


def tela_youtube_downloader(frame):
    limpar_conteudo(frame)
    ctk.CTkLabel(frame,
                 text='Youtube Downloader',
                 font=('Arial', 22, 'bold')).pack(pady=25)
    
    ctk.CTkLabel(frame,
                 text='Cole o link do YouTube e baixe o vídeo diretamente desta tela.',
                 font=('Arial', 14),
                 wraplength=520,
                 justify='left').pack(pady=10)
