import tkinter as tk

janela = tk.Tk()

janela.title("Minha primeira aplicação")
janela.geometry("400x300")

rotulo = tk.Label(
    janela,
    text="Eu me chamo mel!",
    font=("Arial", 14),
    fg="magenta"
)

entrada = tk.Entry(
    janela,
    width=30
)

rotulo.pack(pady=20)

entrada.pack(pady=10)

def exibir_mensagem():
    print(f"Texto: {entrada.get()
}")


botao = tk.Button(
    janela,
    text="Clique aqui",
    command=exibir_mensagem
)

botao.pack(pady=10)
janela.mainloop()