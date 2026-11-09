# Leia seis números inteiros e guarde todos em uma lista. Mostre a lista, a soma, a média, o maior e o menor valor.

# Teste com 3, -2, 0, 7, 7, -3: soma 12, média 2.0, maior 7 e menor -3.

lista = []
num_um = int(input("Digite um número: "))
num_dois = int(input("Digite um número: "))
num_tres = int(input("Digite um número: "))
num_quatro = int(input("Digite um número: "))
num_cinco = int(input("Digite um número: "))
num_seis = int(input("Digite um número: "))
lista.append(num_um)
lista.append(num_dois) 
lista.append(num_tres)
lista.append(num_quatro)
lista.append(num_cinco)
lista.append(num_seis)
soma =  num_um + num_dois + num_tres + num_quatro + num_cinco + num_seis
media = soma / 6

menor_valor = min(lista)
maior_valor = max(lista)

print(lista)
print(f"Média: {media:.2f}")
print(f"Menor: {menor_valor}") 
print(f"Maior: {maior_valor}")