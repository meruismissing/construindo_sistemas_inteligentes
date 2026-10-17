primeiro_num = int(input("Qual é o primeiro número? "))
segundo_num = int(input("Qual é o segundo número? "))

if primeiro_num > segundo_num:
    print("O primeiro número é maior.")
elif segundo_num > primeiro_num:
    print("O segundo número é maior.")
else: 
    print("Ambos números são iguais.")
