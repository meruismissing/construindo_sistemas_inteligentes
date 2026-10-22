# 07_sistema_frete.py
valor_compra = float(input("Qual o valor da compra? Ex: 15.00 "))
if valor_compra <= 0:
  print("Esse valor é inválido! Não daremos continuidade ao seu pedido.")
  exit()
regiao = input("Qual a região de entrega? (sul/sudeste/centro-oeste/norte/nordeste) ")
if regiao != "sul" and regiao != "sudeste" and regiao != "centro-oeste" and regiao != "norte" and regiao != "nordeste":
  print("Essa região é inválida! Não daremos continuidade ao seu pedido.")
  exit()
print()
print("=== Tabela de Frete ===")
print("| Sul          |   R$15,00  |")
print("| Sudeste      |   R$20,00  |")
print("| Centro-Oeste |   R$25,00  |")
print("| Norte        |   R$35,00  |")
print("| Nordeste     |   R$35,00  |")
print()
frete = 0.0
if valor_compra >= 300.0:
  print("Você recebeu frete grátis!")
  frete += 0.0
  total = valor_compra + frete
  print(f"Valor da compra: {valor_compra}, Frete: {frete}, Total: {total}.")
elif valor_compra < 300 and regiao == "sul":
  frete += 15.00
  total = valor_compra + frete
  print(f"Valor da compra: {valor_compra}, Frete: {frete}, Total: {total}.")
elif valor_compra < 300 and regiao == "sudeste":
  frete += 20.00
  total = valor_compra + frete
  print(f"Valor da compra: {valor_compra}, Frete: {frete}, Total: {total}.")
elif valor_compra < 300 and regiao == "centro-oeste":
  frete += 25.00
  total = valor_compra + frete
  print(f"Valor da compra: {valor_compra}, Frete: {frete}, Total: {total}.")
elif valor_compra < 300 and regiao == "norte" or valor_compra < 300 and regiao == "nordeste":
  frete += 25.00
  total = valor_compra + frete
  print(f"Valor da compra: {valor_compra}, Frete: {frete}, Total: {total}.")

