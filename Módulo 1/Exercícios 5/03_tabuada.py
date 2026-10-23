tabuada = int(input("De qual tabuada você deseja saber? "))
limite = int(input("Qual o limite da tabuada? ex: de 10 é 100. "))
contador = tabuada
while contador != limite:
    print(contador)
    contador += tabuada
    
print(limite)
print("Fim!")