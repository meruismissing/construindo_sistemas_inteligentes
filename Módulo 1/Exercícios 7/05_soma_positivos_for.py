soma = 0
positivos = 0

for i in range(6):
    numero = int(input("Digite um número: "))
    
    soma = soma + numero

    if numero > 0:
        positivos = positivos + 1

print("Soma dos números:", soma)
print("Quantidade de positivos:", positivos)