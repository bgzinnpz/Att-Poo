class Personagem:
  def __init__ (self, nome:str, vida:int):
    self.nome = nome
    self.vida = vida
  def Tomar_dano(self, valor:int):
    self.vida -= valor
  class Mago(personagem):
    def __init__(self, nome: str
