import tkinter as tk

janela = tk.Tk()
janela.title("Calculadora Simples")
janela.geometry("400x200")

lblPrimeiro = tk.Label(janela, text= "Primeiro Número:", font=("Arial, 10"))
n1 = tk.Entry(janela, width=20)

lblSegundo = tk.Label(janela, text= "Segundo Número:", font=("Arial, 10"))
n2 = tk.Entry(janela, width=20)

lblPrimeiro.pack(pady=10)
n1.pack(padx=15)

lblSegundo.pack(pady=10)
n2.pack(padx=15)


botoes = tk.Frame(janela)
botoes.pack(pady=10)

btnSoma = tk.Button(janela, text="+", command=lambda: calcular("+"))
btnSub = tk.Button(janela, text="-", command=lambda: calcular("-"))
btnMult = tk.Button(janela, text="*", command=lambda: calcular("*"))
btnDiv = tk.Button(janela, text="/", command=lambda: calcular("/"))

btnSoma.grid(row=0, column=0, padx=5)
btnSub.grid(row=0, column=1, padx=5)
btnMult.grid(row=0, column=2, padx=5)
btndiv.grid(row=0, column=3, padx=5)

def calcular(operacao):
    if operacao == "+":

janela.mainloop()