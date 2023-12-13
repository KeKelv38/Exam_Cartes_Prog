#ps: rien ne fonctionne, je n'ai pas réussi

class Carte:
    def __init__(self, coutMana, nom, description):
        self.__cout_mana=coutMana
        self.__name=nom
        self.__description=description

    def getMana(self):
        return self.__cout_mana

class Mage:
    def __init__(self, nom, pv, totalMana, manaActuelle):
        self.__name=nom
        self.__pv=pv
        self.__total=totalMana
        self.__manaActuelle=manaActuelle
        self.__main=[]
        self.__defausse=[]
        self.__zoneJeu=[]

    def getManaActuelle(self):
        return self.__manaActuelle
    
    def getPv(self):
        return self.__pv

    def jouerCarte(self):
        

    def recupMana(self, manaActuelle):
        manaActuelle+=10

    def attaquer(self):

class Cristal(Carte):
    def __init__(self, valeur, coutMana):
        self.__valeur=valeur
        self.__cout=coutMana

    def jouerCristal(self, coutMana, mana, totalMana):
        if self.getMana()>= coutMana:
            totalMana+=10
            mana-=coutMana

class Creature(Carte):
    def __init__(self, pv, att, coutMana):
        self.__pv=pv
        self.__att=att
        self.__coutMana=coutMana
        self.__main=[]
        self.__zoneJeu=[]
        self.__defausse=[]
    
    def getPv(self):
        return self.__pv

    def jouerCreature(self):

class Blast(Carte):
    def __init__(self,valeur):
        self.__valeur=valeur

    def lancerBlast(self, cible):
        cible=int(input("Lancer un Blast contre Creature(1) ou Mage(2)"))
        print("La cible est", cible)
        if cible==1:
            Creature.getPv-=valeur
        else
            Mage.getPv-=valeur
        

player1=Mage("Joueur 1", 100, 50, 50)
player2=Mage("Joueur 2", 100, 50, 50)

monstre1=Creature(20, 10, 5)
carteBlast=Blast(15)
carteCristal=Cristal(10, 20)





