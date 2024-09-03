class Carro:
    def __init__(self, marca, modelo, ano, velocidade):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        
    def acelerar(self):
        self.velocidade += 10
        print(f"{self.modelo} acelerou. Velocidade atual: {self.velocidade} km/h")
        
    def frear(self):
        self.velocidade -= 10
        print(f"{self.modelo} freou. Velocidade atual: {self.velocidade} km/h")    
        
carro1 = Carro("Toyota", "Corolla", 2020, 0)
carro2 = Carro("Honda", "Civic", 2019, 0)

carro1.acelerar()
carro2.acelerar()
carro1.frear()
