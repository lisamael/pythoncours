class Animal (): 
    def __init__(self, name:str, taille:float , poids:int):
        self.name = name
        self.taille = taille
        self.poids = poids
        
    def describe (self) :
        print(f'Mon animal est {self.name},il mesure {self.taille} m, il pèse {self.poids} kg .')     

class Herbivore(Animal):
    def eat (self):
        print(f'Mon animal {self.name} est herbivore')

class Carnivore(Animal):
    def eat (self)-> None:
        print(f'Mon animal {self.name} mange est carnivore')

class Omnivore(Herbivore):
    def __init__(self, name:str, taille:float , poids:int):
        super().__init__(name, taille ,poids)
    def eat(self):
        super().eat()
        print(f"mon animal {self.name} mange aussi la viande")

if __name__ == '__main__':
    Lion= Carnivore('Lion',1.40,80)
    Lion.eat()
    Lion.describe()
    Cochon=Omnivore('Cochon',0.50,5)
    Cochon.eat()
    Cochon.describe()