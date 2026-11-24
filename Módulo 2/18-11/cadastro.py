# Crie um formulário utilizando o gerenciador de layout grid(). O formulário deverá possuir campos para nome, idade e e-mail, além de um botão "Cadastrar".

# Ao clicar no botão, verifique se todos os campos foram preenchidos e apresente as informações cadastradas em um rótulo na própria interface.
import tkinter as tk

janela = tk.Tk()

janela.title("Registro")
janela.geometry("600x400")

rotulo = tk.Label(
    janela,
    text="Cadastre-se.",
    font=("Arial", 14),
    fg="magenta"
)

nom = tk.Label(
    janela,
    text="Insira seu nome.",
    font=("Arial", 10),
    fg="magenta"
)

nome = tk.Entry(
    janela,
    width=20
)

emai = tk.Label(
    janela,
    text="Insira seu e-mail.",
    font=("Arial", 10),
    fg="magenta"
)

email = tk.Entry(
    janela,
    width=20
)

idad = tk.Label(
    janela,
    text="Insira sua idade.",
    font=("Arial", 10),
    fg="magenta"
)

idade = tk.Entry(
    janela,
    width=20
)

rotulo.pack(pady=20)

nom.pack(pady=10)
nome.pack(pady=10)
emai.pack(pady=10)
email.pack(pady=10)
idad.pack(pady=5)
idade.pack(pady=10)

def mostrar_dados():
    if nome.get().strip() == "" or idade.get().strip() == "" or email.get().strip() == "":
        rotulo.config(text="Digite algo válido.", fg="red")
    else:
        print(f"Nome: {nome.get()
}")
        print(f"E-mail: {email.get()
}")
        print(f"Idade: {idade.get()
}")
        rotulo.config(text=f"Olá, {nome.get()}, seu e-mail é {email.get()} e sua idade é {idade.get()}", fg="magenta")
    
botao = tk.Button(
    janela,
    text="Cadastrar",
    command=mostrar_dados
)

botao.pack(pady=10)
janela.mainloop()