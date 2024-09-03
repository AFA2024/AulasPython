class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.__ano = ano
        self.__velocidade = velocidade
        
    def acelerar(self):
        self.velocidade += 10
        print(f"{self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h")
        
    def frear(self):
        self.velocidade -= 10
        print(f"{self.modelo} freou. Velocidade atual: {self.velocidade} km/h")
    
    def get_ano(self):
        return self.__ano
    
    def set_ano(self, ano):
        if ano > 1985:
            self.__ano = ano
        else:
            print("Ano Invalido !")

carro1 = Carro("Toyota", "Corolla", 2020, 0)
print(carro1.get_ano())

carro1.set_ano(2025)
print(carro1.get_ano())

carro1.set_ano(1800)
       