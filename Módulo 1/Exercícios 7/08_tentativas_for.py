
codigo = "ROBO123"
tentativas = 3

for tentativa in range(0, tentativas, 1):
    print(f"=== TENTATIVA NÚMERO {tentativas} ===")
    tentar = input("Qual é o código? ")
    if tentar == "ROBO123":
        print("Código correto!")
        break
    else:
        tentativas -= 1
        print("Senha incorreta.")
        if tentativas == 0: 
            print("Você está sem tentativas.")