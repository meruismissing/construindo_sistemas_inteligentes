class Contador:
    def __init__(self):
        self.valor = 0
    def incrementar(self):
        self.valor += 1
    def zerar(self):
        self.valor = 0

contador1 = Contador()
contador2 = Contador()

contador1.incrementar()
contador1.incrementar()
contador1.incrementar()

contador2.incrementar()

print("--- Valores iniciais ---")
print(f"Contador 1: {contador1.valor}")
print(f"Contador 2: {contador2.valor}")

contador1.zerar()

print("\n--- Valores finais ---")
print(f"Contador 1: {contador1.valor}")
print(f"Contador 2: {contador2.valor}")