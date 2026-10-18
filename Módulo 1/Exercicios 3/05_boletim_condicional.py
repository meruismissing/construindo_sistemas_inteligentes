nota1 = float(input("Digite a primeira nota: "))

nota2 = float(input("Digite a segunda nota: "))

if nota1 < 0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print("Nota inválida!")

else:
  media = (nota1 + nota2) / 2
  print("Sua média é:", media)

if media >= 7:
  print("Aprovado!")
elif media >= 5:
  print("Recuperação!")
else:
  print("Reprovado!")
