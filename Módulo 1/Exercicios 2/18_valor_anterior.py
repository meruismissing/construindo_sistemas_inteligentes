saldo = 80
saldo_anterior = saldo # Mantém o mesmo valor porque foi usado o comando antes das atribuições que vêm depois dele. Ou seja, se tivesse tido um saldo_anterior depois, atualizaria, mas continua dessa mesma forma porque é antes e não depois de qualquer atribuição.

saldo = saldo - 25 # 55
saldo = saldo + 10 # 65

print("Saldo anterior:", saldo_anterior)
print("Saldo atual:", saldo)
