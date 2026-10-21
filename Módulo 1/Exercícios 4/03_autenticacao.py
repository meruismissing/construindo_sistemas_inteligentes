usuario_correto = "admin"
senha_correta = "python123"

usuario = input("Digite o seu usuário ")
if usuario != "admin":
    print("Usuário não encontrado!")
    exit()
senha = input("Digite a sua senha ")
if senha != "python123":
    print("Senha incorreta!")
    exit()
elif senha == "python123" and usuario == "admin":
    print("Acesso autorizado!")