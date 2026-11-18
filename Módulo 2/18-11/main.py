import tkinter as tk

janela = tk.Tk()

janela.title("Minha primeira aplicação")
janela.geometry("400x300")

janela.mainloop()

rotulo = tk.Label(
    janela,
    text="Eu me chamo mel!",
    font=("Arial", 14),
    fg="blue"
)

rotulo.pack(pady=20)