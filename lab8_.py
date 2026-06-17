class Carteira:
    def __init__(self, moeda, saldo):
        self._moeda = moeda
        self._saldo = saldo
        
    def conversor_yuan(self, valor_yuan):
       if self.moeda ==  "USD"
            return valor_yuan * 0.14
     elif self.moeda == "BRL":
        return valor_yuan * 0.85
     elif self.moeda == "CNY":
        return valor_yuan
     else:
        print("Erro")

def __add__(self, valor_yuan):
    valor_convertido = self.converter_yuan(valor_yuan)
    return self.saldo + valor_convertido

def __sub__(self, valor_yuan):
    valor_convertido = self.converter_yuan(valor_yuan)
    return self.saldo - valor_convertido
        
  carteira_usd = Carteira("USD", 10.0)
# 50 CNY = 7.0 USD (usando taxa 1 CNY = 0.14 USD) 
print('Soma de carteira USD + 50 yuan = ', carteira_usd + 50.0) # 17.0

