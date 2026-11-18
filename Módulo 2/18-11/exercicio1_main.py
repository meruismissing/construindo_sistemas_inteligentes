import tkinter as tk

janela = tk.Tk()

janela.title("Registro")
janela.geometry("600x400")

rotulo = tk.Label(
    janela,
    text="Insira seus dados.",
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

cidad = tk.Label(
    janela,
    text="Insira sua cidade.",
    font=("Arial", 10),
    fg="magenta"
)

cidade = tk.Entry(
    janela,
    width=20
)

rotulo.pack(pady=20)

nom.pack(pady=10)
nome.pack(pady=10)
emai.pack(pady=10)
email.pack(pady=10)
cidad.pack(pady=5)
cidade.pack(pady=10)

def mostrar_dados():
    print(f"Nome: {nome.get()
}")
    print(f"E-mail: {email.get()
}")
    print(f"Cidade: {cidade.get()
}")
    print(f"Olá, {nome.get()}, seu email é {email.get()} e você é de {cidade.get()}")

botao = tk.Button(
    janela,
    text="Clique aqui",
    command=mostrar_dados
)

botao.pack(pady=10)
janela.mainloop()