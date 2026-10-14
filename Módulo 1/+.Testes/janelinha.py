import tkinter as tk
janela = tk.Tk()
janela.title("Eu amo o valval")
janela.geometry("600x240")
texto = tk.Label(janela, text="Eu amo o valval mais do que tudo no mundo.") 
texto.pack(pady=20)

botao = tk.Button(janela, text="Ok")
botao.pack(pady=10)
janela.mainloop()