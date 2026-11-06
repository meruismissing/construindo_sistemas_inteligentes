# Leia uma palavra e, depois, uma única letra. Percorra a palavra diretamente com for e conte quantas vezes a letra aparece.

# Considere que o usuário informará exatamente um caractere na segunda entrada. Diferencie maiúsculas e minúsculas: a e A são valores distintos.

# Teste com banana e a (resultado 3), com uma letra ausente e com uma palavra vazia.

palavra = input("Digite uma palavra: ")
letra = input("Digite uma letra: ")

contador = 0

for caractere in palavra:
    if caractere == letra:
        contador += 1


if contador > 1:
    print(f"A letra {letra} aparece {contador} vezes no texto.")
else:
    print(f"A letra {letra} aparece {contador} vez no texto.")