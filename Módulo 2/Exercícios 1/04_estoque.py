class Produto:
    def __init__(self, preco, estoque):
        self.preco = preco
        self.estoque = estoque
    def repor(self, quantidade):
        if quantidade <= 0:
            return False, f"Quantidade inválida para reposição. Estoque atual: {self.estoque}"
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
sucesso, mensagem = produto1.repor(5)
print(f"Você repôs 5 produtos e retornou: {sucesso} | {mensagem}")
sucesso, mensagem = produto1.repor(0)
print(f"Você tentou repôr 0 produtos e retornou: {sucesso} | {mensagem}")
valor_final = produto1.valor_em_estoque()
print(f"Preço inicial: {produto1.preco} Estoque final: {produto1.estoque}")
print(f"O valor final é: {valor_final}")