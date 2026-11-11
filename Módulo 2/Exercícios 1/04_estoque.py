class Produto:
    def __init__(self, preco, estoque):
        self.preco = preco
        self.estoque = estoque
    def repor(self):
        if quantidade <= 0:
            return False, "Quantidade inválida para reposição."
        self.estoque += quantidade
        return True, f"Reposição bem-sucedida. Estoque atual: {self.estoque}"
    def vender(self, quantidade):
        if quantidade > self.estoque:
            return False, f"Erro: quantidade excede o estoque. Estoque disponível: {self.estoque}"
        self.estoque -= quantidade
        return True, f"Venda realizada com sucesso. Estoque atual: {self.estoque}"
    def valor_em_estoque(self):
        return self.estoque * self.preco


produto1 = Produto(5.0, 4)
print(f"Produto chegou ao estoque. Preço: R$ {produto1.preco}, Estoque inicial: {produto1.estoque}\n")

sucesso, mensagem = produto1.vender(2)
print(f"Você vendeu 2 produtos e retornou: {sucesso} | {mensagem}")
sucesso, mensagem = produto1.vender(3)
print(f"Você tentou vender 3 produtos e retornou: {sucesso} | {mensagem}")
