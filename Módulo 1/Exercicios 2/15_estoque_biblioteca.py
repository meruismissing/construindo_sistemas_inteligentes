print("Uma biblioteca começa o dia com 40 livros disponíveis.")
print()
quantidade_inicial = 40
livros_disponiveis = 40
livros_disponiveis += 12
print(f"Após a biblioteca abrir oficialmente, ela recebe 12 livros novos, contabilizando {livros_disponiveis} livros disponíveis. Enquanto, no começo, eram {quantidade_inicial} livros.") # Antes dos resultados esperados, esta resposta era óbvia, 52.
print()
livros_disponiveis -= 9
print(f"A biblioteca empresta 9 livros, contabilizando {livros_disponiveis} livros disponíveis. Criando uma diferença um pouco maior que os {quantidade_inicial} livros iniciais.") # 52 - 9 se tornaram 43, pois, por exemplo, 50-7 = 43 então 52 - 9 = 43, antes de executar e ver o resultado.
print()
livros_disponiveis += 4
print(f"A biblioteca recebe a devolução de 4 livros, que ficam mais {livros_disponiveis} livros disponíveis, dá para perceber cada mais a diferença entre os {quantidade_inicial} livros do começo.") # Antes de executar, ficam 47 livros. 3 + 4 = 7
print()
livros_disponiveis -= 6
print(f"{quantidade_inicial} foi mudada muitas e muitas vezes durante este dia, até chegar na última hora do dia, onde a biblioteca emprestou mais 6 livros, e terminou o dia com {livros_disponiveis} livros.") # Antes de executar, ficam 41 livros
