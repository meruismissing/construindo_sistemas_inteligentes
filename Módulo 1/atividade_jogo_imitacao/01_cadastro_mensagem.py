codinome = input("Qual o seu nome ou apelido? ")
mensagem = input("Digite a identificação da mensagem, como texto: ")
qtd_simbolos = int(input("Quantidade de grupos de símbolos: "))
if qtd_simbolos <= 0:
    print("Esta quantidade de símbolos é inválida.")
    exit()
tempo = float(input("Qual o tempo estimado para analisar cada grupo, em minutos? "))
if tempo <= 0:
    print("Este tempo é inválido.")
    exit()

total = qtd_simbolos / tempo
if total <= 60:
    print("Análise dentro do prazo.")
elif total > 60:
    print("Reorganizar o trabalho.")
print(f"""
=== FICHA ===
Codinome: {codinome}
ID Mensagem: {mensagem}
Quantidade grupos: {qtd_simbolos}
Tempo total: {total:.2f}
""")
# A identificação continua texto pois contém texto no meio ou é para ser lido como um código, não um número em questão.
# É adequado usar float porque pode ser um tempo quebrado, como, por exemplo, um minuto e meio.
