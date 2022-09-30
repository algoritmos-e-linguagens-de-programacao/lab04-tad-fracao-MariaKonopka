class Fracao:
  numerado = 1
  denominador = 1
   
  def __init__(self, numerador, denominador):
     self.numerador = numerador
     self.denominador = denominador
  
     
  def add(self, fracao):
     num =(self.numerador * fracao.denominador) + (fracao.numerador * self.denominador)
     den = self.denominador * fracao.denominador
     return Fracao(num, den)
     
  def sub(self, fracao):
     num =(self.numerador * fracao.denominador) - (fracao.numerador * self.denominador)
     den = self.denominador * fracao.denominador
     return Fracao(num, den)
  
  def mult(self, fracao):
      num = self.numerador * fracao.numerador
      den = self.denominador * fracao.denominador
      return Fracao(num, den)
  
  def simplify(self):
      a = self.numerador
      b = self.denominador
  
      while (b != 0):
        d = a % b
        a = b
        b = d
  
      num = self.numerador / a
      den = self.denominador / a
  
      return f"{num} / {den}"
      
  def solve(self):
     return self.numerador/self.denominador
  
  def __str__(self):
     return f"{self.numerador} / {self.denominador}"


fracao1 = Fracao(2,3)
fracao2 = Fracao(1, 3)
fracao3 = fracao1.add(fracao2)
fracao4 = fracao1.sub(fracao2)
fracao5 = fracao1.mult(fracao2)
fracao6 = Fracao (4, 2)

print(f"fracao1: {fracao1}")
print(f"fracao2: {fracao2}")

print(f"fracao3: {fracao3}")
print(f"fracao4: {fracao4}")
print(f"fracao5: {fracao5}")

print(f"fracao5: {fracao5}")

print(f"fracao1: {fracao1.solve()}")
print(f"fracao2: {fracao2.solve()}")
print(f"fracao6: {fracao6.simplify()}")