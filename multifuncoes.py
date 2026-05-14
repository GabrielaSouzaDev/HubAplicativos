# Autor: Gabriela Souza
# Projeto - Ferramentas Essenciais

import customtkinter as ctk
import requests

# configuração visual
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

# janela principal
app = ctk.CTk()
app.geometry('800x600')
app.title('MULTIFUNÇÕES')
app.iconbitmap('tools.ico')

# frame esquerda/menu
frame_menu = ctk.CTkFrame(app,
                          width=200,
                          height=600,
                          fg_color= '#FFE880')
frame_menu.pack(side='left',fill='y')


# frame direita/conteúdo
frame_conteudo = ctk.CTkFrame(app,
                              fg_color='#964B00')
frame_conteudo.pack(side='right', fill='both', expand='True')

# botões
ctk.CTkButton(frame_menu,
              fg_color='#FFFFFF',
              text_color=('#0F0F0F'),
              hover_color=('#964B00'),
              corner_radius=12,
              text='Juros Simples').pack(pady=10, padx=10)


# loop
app.mainloop()