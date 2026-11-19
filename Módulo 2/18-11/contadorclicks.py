import tkinter as tk

janela = tk.Tk()

janela.title("Clicks")
janela.geometry("600x400")

rotulo = tk.Label(
    janela,
    text="Contador de clicks",
    font=("Arial", 14),
    fg="magenta"
)

rotulo.pack(pady=20)
clicks = 0
def clicar():
    global clicks
    clicks += 1
    rotulo.config(text=f"Qtd. de clicks: {clicks}")

botao = tk.Button(
    janela,
    text="Clique-me",
    command=clicar
)

botao.pack(pady=10)
janela.mainloop()