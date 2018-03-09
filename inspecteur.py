from random import shuffle,randrange
import parser as p
from time import sleep
import parser as p

permanents, deux, avant, apres = {'rose'}, {'rouge','gris','bleu'}, {'violet','marron'}, {'noir','blanc'}
couleurs = avant | permanents | apres | deux
passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

class personnage:
    def __init__(self,couleur):
        self.couleur, self.suspect, self.position, self.pouvoir = couleur, True, 0, True
    def __repr__(self):
        susp = "-suspect" if self.suspect else "-clean"
        return self.couleur + "-" + str(self.position) + susp


class iaInspecteur:
    def __init__(self,question):
        self.question = ""

    def choosePersonnage(self):
        print("a")
        return

    def activatePouvoir(self):
        print("b")
        return

    def bloqueChemin(self):
        print("c")
        return

    def movePersonnage(self):
        print("d")
        return

    def swapPersonnage(self):
        print("e")
        return

    def shadow(self):
        print("f")
        return

    def prepareAnswer(self):
        actions = {"tuile": self.choosePersonnage,
                    "pouvoir": self.activatePouvoir,
                    "bloquer": self.bloqueChemin,
                    "sortie": self.bloqueChemin,
                    "positions": self.movePersonnage,
                    "echanger": self.swapPersonnage,
                    "obscurcir": self.shadow,
        }
        try:
            actions[self.question]()
        except:
            pass




def writeRep(reponse):
    rf = open('./0/reponses.txt','w')
    rf.write(str(reponse))
    rf.close()

def lancer():
    fini = False
    parser = p.parser()
    old_question = ""
    while not fini:
        qf = open('./0/questions.txt','r')
        question = qf.read()
        q = parser.parseQuestion(question)
        qf.close()
        if question != old_question :
            ia_main(q)
            old_question = question
        infof = open('./0/infos.txt','r')
        lines = infof.readlines()
        parser.parseInfo(lines)
        infof.close()
        if len(lines) > 0:
            fini = "Score final" in lines[-1]
    print("partie finie")