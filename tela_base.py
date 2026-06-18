import customtkinter as ctk


def limpar_conteudo(frame):
    for widget in frame.winfo_children():
        widget.destroy()
