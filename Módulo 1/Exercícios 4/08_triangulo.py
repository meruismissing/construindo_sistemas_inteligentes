a = float(input("Digite o lado A: "))
if a <= 0:
  print("Triângulo inválido!")
  exit()
b = float(input("Digite o lado B: "))
if b <= 0:
  print("Triângulo inválido!")
  exit()
c = float(input("Digite o lado C: "))
if c <= 0:
  print("Triângulo inválido!")
  exit()

if a > 0 and b > 0 and c > 0 and (a + b > c) or (a + c > b) or (b + c > a):
 if a == b and b == c:
    print("Este é um triângulo Equilátero")
 elif a == b or a == c or b == c:
    print("Este é um triângulo Isósceles")
 else:
    print("Este é um triângulo Escaleno")
