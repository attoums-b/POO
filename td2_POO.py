
class SuperHero:
    def __init__(self, nomH,maxP):
        self.nomH = nomH
        self.pv = self.pv_par_defaut()
        self.pouvoirs = []
        self.maxP = maxP 

    def pv_par_defaut(self):
        return 100  


    def sommePouvoirs(self):
        return len(self.pouvoirs)


    def estMort(self):
        return self.pv <= 0
         
        


    def ajouterPouvoir(self, pouvoir):
        if len(self.pouvoirs)  < self.maxP:
            self.pouvoirs.append(pouvoir)   
        else:
            print("Vous avez dépassé le nombre de pouvoirs maximal à ajouter")      

    def afficherSuperHero(self):
        print(f"nom du heros: {self.nomH}, points de vie actuel: {self.pv}")
        print("SES POUVOIRS !")
        for power in self.pouvoirs:
            print(power.nom ,":" , power.puissance)


class Pouvoirs:
    def __init__(self, nom, puissance):
        self.nom = nom 
        self.puissance = self.puissance_par_defaut(puissance)
        
 
    def puissance_par_defaut(self, puissance):
        if puissance < 0:
            return 10
        else:
            return puissance

    def afficherPuissance(self):
        print(f"nom du pouvoir: {self.nom}, puissance: {self.puissance}")

class Combat:
        
        def __init__(self,super1,super2):
            self.super1 = super1
            self.super2 = super2
        



        def demarrerCombat(self):
            if not self.super1.estMort() and not self.super2.estMort():
                if self.super1.sommePouvoirs() > self.super2.sommePouvoirs():
                    print(f"{self.super1.nomH} a gagné le combat!")
                    self.super2.pv -= 10
                    print(f"Vies après le combat: ({self.super1.nomH})--> {self.super1.pv}, ({self.super2.nomH})-->{self.super2.pv}")
                elif self.super2.sommePouvoirs() > self.super1.sommePouvoirs():
                    print(f"{self.super2.nomH} a gagné le combat!")
                    self.super1.pv -= 10
                    print(f"Vies après le combat: ({self.super2.nomH})--> {self.super2.pv}, ({self.super1.nomH})-->{self.super1.pv}")
                else:
                    self.super1.pv -=5
                    self.super2.pv -= 5
                    print("aucun des deux supers n'est déclaré vainqueur: EGALITE!") 
                    print(f"Vies après le combat: ({self.super1.nomH})--> {self.super1.pv}, ({self.super2.nomH})-->{self.super2.pv}")   



            else:
                print("l'un ou les deux supers sont morts! impossible d'éffectuer le combat !")








def main():
    batman = SuperHero("Batman",3)
    superman = SuperHero("Superman",5)

    p1 = Pouvoirs("rayons lazers", 500)
    p2 = Pouvoirs("bague éclair", -430)
    p3 = Pouvoirs("sort de chèvre", 788)
  
   

    batman.ajouterPouvoir(p2)
    batman.ajouterPouvoir(p3)
    superman.ajouterPouvoir(p1)

    print(type(batman.afficherSuperHero()))
  
    print(batman.sommePouvoirs())
    print(superman.estMort())
    combat = Combat(batman,superman)
    combat.demarrerCombat()




main()    
    
