import customtkinter as ctk
from tela_base import limpar_conteudo


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
            resultado_label.configure(text=f'IMC: {imc:.1f} — {categoria}', text_color=None)
        except ValueError:
            resultado_label.configure(text='Informe peso e altura válidos.', text_color='#c94f4f')

    ctk.CTkButton(frame,
                  text='Calcular IMC',
                  command=calcular_imc,
                  width=160,
                  corner_radius=10).pack(pady=16)
    resultado_label.pack(pady=10)
