import tkinter as tk

janela = tk.Tk()

janela.title("Calculadora simples")
janela.geometry("600x400")

rotulo = tk.Label(
    janela,
    text="Insira o primeiro número",
    font=("Arial", 14),
    fg="magenta"
)

num_um = tk.Entry(
    janela,
    width=20
)

num_doi = tk.Label(
    janela,
    text="Insira o segundo número",
    font=("Arial", 10),
    fg="magenta"
)

num_dois = tk.Entry(
    janela,
    width=20
)

rotulo.pack(pady=20)

num_um.pack(pady=10)
num_doi.pack(pady=10)
num_dois.pack(pady=10)

def mostrar_soma():
    print(f"Número um: {num_um.get()
}")
    print(f"Número dois: {num_dois.get()
}")
    resultado = 0
    resultado += num_um.get() + num_dois.get()
    print(f"Resultado: {resultado}")

botao = tk.Button(
    janela,
    text="Clique aqui",
    command=mostrar_soma
)

botao.pack(pady=10)
janela.mainloop()