import tkinter as tk
janela = tk.Tk()
janela.title("Sou louca?")
janela.geometry("600x240")
texto = tk.Label(janela, text="Você me acha louca?") 
texto.pack(pady=20)

botao = tk.Button(janela, text="Sim")
botao.pack(pady=10)
janela.mainloop()