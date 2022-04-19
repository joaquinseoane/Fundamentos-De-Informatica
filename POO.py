#  Objeto = Un ente computacional, que entiende mensajes. Y tiene atributos, el estado es el conjunto de atributos. 
# Los objetos tienen estado estaticos (arqitectura) y tiene estados dinamicos que contemplan los valores.
# Los objetos puden instanciarse, que es darle una entidad concreta, es diferente a definirlo.
# Polimorfismo = para que exista el polimorfismo tiene que haber alguien que este observando los objetos. 

#DESAFIO I
class Animalesalado():
    def esta_feliz(self):
        return self.energia > 500


class Golondrina:
  def __init__(self, energia):
    self.energia = energia

  def comer_alpiste(self, gramos):
    self.energia += 4 * gramos

  def volar_en_circulos(self):
    self.volar(0)

  def volar(self, kms):
    self.energia -= 10 + kms

  def esta_debil(self):
      return self.energia < 10

  def esta_feliz(self):
      return self.energia > 500


class Dragon:     
  def __init__(self, cantidad_dientes, energia):
    self.energia = energia
    self.cantidad_dientes = cantidad_dientes

  def escupir_fuego(self):
    self.energia -= 2 * self.cantidad_dientes

  def comer_peces(self, unidades):
    self.energia += 100 * unidades

  def volar_en_circulos(self):
    self.energia -= 1

  def volar(self, kms):
    self.energia -= 10 + kms/10

  def esta_debil(self):
      return self.energia < 50


class entrenador:
  """un entrenador tiene un equipo y puede admitir nuevos animal alado a su equipo"""
  def __init__(self, equipo):
    self.equipo =  equipo

  def agregar_animal(self, animal):
    """este metodo toma un objeto anmial alado que tendra todos los atributos de esa clase"""
    self.equipo.append(animal)
  
  def el_equipo(self):
    return self.equipo

  def entrenar_dragon(self, dragon):
    for i in range(20):
      dragon.volar_en_circulos()
    dragon.comer_peces(3)

  def entrenar_equipo(self):
   for drangon in self.equipo
    self.entrenar_dragon

  def entrenamiento_intensivo(self):
    for dragon in self.equipo:
      while dragon.esta_debil == false:
        dragon.volar_en_circulos()





pepita = Golondrina(100)
anastasia = Golondrina(200)
roberta = Dragon(10, 1000)
chimuelo = dragon(200, 2000)



hipo = entrenador([roberta, chimuelo])

print(hipo)
print(hipo, equipo)
