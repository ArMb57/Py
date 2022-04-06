class Voiture:
    counter = 0
    def __init__(self, modele, marque, vitesse_max,km, couleur, carburant):
        self.modele = modele
        self.marque = marque
        self.vitesse_max = vitesse_max
        self.km = km
        self.couleur = couleur
        self.carburant = carburant
        
        Voiture.counter += 1
v = Voiture('serie 1', 'BMW', 220, 50000,'rouge', 'essence')
v1 = Voiture('serie 1', 'BMW', 220, 50000,'blanche', 'diesel')
v2 = Voiture('serie 1', 'BMW', 220, 50000,'rouge', 'diesel')
v3 = Voiture('serie 1', 'BMW', 220, 50000,'noire', 'electrique')




class Bateau:
    counter = 0
    def __init__(self, modele, marque, vitesse_max, km, type):
        self.modele = modele
        self.marque = marque
        self.vitesse_max = vitesse_max
        self.km = km
        self.type =type

        Bateau.counter += 1
b = Bateau('switch', 'Bayliner',  30, 3000, 'A moteur')
b1 = Bateau('switch', 'Bayliner', 30, 3000, 'A voile')


class Moto:
    counter = 0
    def __init__(self, modele, marque, vitesse_max,km):
        self.modele = modele
        self.marque = marque
        self.vitesse_max = vitesse_max
        self.km = km

        Moto.counter += 1
m = Moto('Cvo Limited', 'Harley Davidson', 150, 3000)
m1 = Moto('Cvo Limited', 'Harley Davidson', 150, 3000)
m2 = Moto('Cvo Limited', 'Harley Davidson', 150, 3000)
m3 = Moto('Cvo Limited', 'Harley Davidson', 150, 3000)


class Avion:
    counter = 0
    def __init__(self, modele, marque, vitesse_max,km):
        self.modele = modele
        self.marque = marque
        self.vitesse_max = vitesse_max
        self.km = km

        Avion.counter += 1
a = Avion('747', 'Boeing', 988, 1500000)




   
