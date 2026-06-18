import customtkinter as ctk


def limpar_conteudo(frame):
    for widget in frame.winfo_children():
        widget.destroy()


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


def tela_calculadora_imc(frame):
    limpar_conteudo(frame)
    ctk.CTkLabel(frame,
                 text='Calculadora de IMC',
                 font=('Arial', 22, 'bold')).pack(pady=25)

    form_frame = ctk.CTkFrame(frame, fg_color='transparent')
    form_frame.pack(pady=10)

    peso_var = ctk.StringVar()
    altura_var = ctk.StringVar()
    resultado_label = ctk.CTkLabel(frame, text='', font=('Arial', 14, 'bold'))

    ctk.CTkLabel(form_frame, text='Peso (kg):', anchor='e').grid(row=0, column=0, pady=8, padx=(0, 10), sticky='e')
    ctk.CTkEntry(form_frame, textvariable=peso_var, width=200).grid(row=0, column=1, pady=8)

    ctk.CTkLabel(form_frame, text='Altura (m):', anchor='e').grid(row=1, column=0, pady=8, padx=(0, 10), sticky='e')
    ctk.CTkEntry(form_frame, textvariable=altura_var, width=200).grid(row=1, column=1, pady=8)

    def calcular_imc():
        try:
            peso = float(peso_var.get().replace(',', '.'))
            altura = float(altura_var.get().replace(',', '.'))
            if peso <= 0 or altura <= 0:
                raise ValueError
            imc = peso / (altura ** 2)
            categoria = 'Magreza' if imc < 18.5 else 'Normal' if imc < 25 else 'Sobrepeso' if imc < 30 else 'Obesidade'
            resultado_label.configure(text=f'IMC: {imc:.1f} — {categoria}')
        except ValueError:
            resultado_label.configure(text='Informe peso e altura válidos.', text_color='#c94f4f')

    ctk.CTkButton(frame,
                  text='Calcular IMC',
                  command=calcular_imc,
                  width=160,
                  corner_radius=10).pack(pady=16)
    resultado_label.pack(pady=10)
