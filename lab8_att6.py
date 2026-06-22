class Personagem:
  def __init__ (self, nome:str, vida:int):
    self.nome = nome
    self.vida = vida
  def Tomar_dano(self, valor:int):
    self.vida -= valor
  class Mago(personagem):
    def __init__(self, nome: str, vida: int, mana: float):
      super().__init__(nome, vida)
      self.mana + float(mana)
    def __str__(self):
      return f"Mago: {self.nome} | Vida: {self.vida} | Mana: {self.mana}"
    def __add__(self, valor: float):
      self.mana += valor
      return self.mana
    def __sub__(self, valor: float):
      self.mana -= valor
      if self.mana < 0:
        self.mana = 0.0
      return self.mana
    def __mul__(self, fator:float):
      self.mana *= fator 
      return self.mana

    def __truediv__(self, valor:float):
      if valor == 0:
        print("Erro: nao e possivel dividir a man  por zero")
        return self.mana
      else:
        self.mana = self.mana / valor
      class Barbaro(Personagem):
        def __init__(self, nome: str, vida: init, stamina: float, furia:bool):
          
