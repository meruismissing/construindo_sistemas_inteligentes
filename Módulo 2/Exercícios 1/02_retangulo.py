class Retangulo:
    def __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura
    
    def calcular_area(self):
        return self.largura * self.altura
    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura)
    def __str__(self):
        return f"Retângulo(largura={self.largura}, altura={self.altura})"
retangulo1 = Retangulo(4, 3)
area = retangulo1.calcular_area()
print(f"A área é: {area}")
print(retangulo1)