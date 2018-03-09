from random import shuffle,randrange
import parser as p
from time import sleep
import operator

import parser as p

permanents, deux, avant, apres = {'rose'}, {'rouge','gris','bleu'}, {'violet','marron'}, {'noir','blanc'}
couleurs = avant | permanents | apres | deux
passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

class iaInspecteur:
    def __init__(self, parser):
        self.personnage = p.personnage
        self.tuiles_dispo = []
        self.parser = parser
        self.nbSuspect = 8
# self.first_turn = {"rose":0,"violet":,"rouge":8,"noir":,"blanc":,"gris":,"bleu":,"marron":,}

    def play(self):
        max_val = -10000
        status_map = self.parser.getAllPersonnage()
        #print(self.tuiles_dispo)
        for perso in self.tuiles_dispo:
            for pos in passages[perso.position]:
                break
                #print(status_map[0])
                #print(pos)
                #print("a\n")


    def min(depth):
        max_val = -10000

        return

    def max(depth):
        return

    def choosePersonnage(self):
        self.tuiles_dispo = self.parser.getTuiles()
        self.play()
        return

    def activatePouvoir(self):
        #print("b")
        return

    def bloqueChemin(self):
        #print("c")
        return

    def movePersonnage(self):
        #print("d")
        return

    def swapPersonnage(self):
        #print("e")
        return

    def shadow(self):
        #print("f")
        return

    def prepareAnswer(self, question):
        question
        #print(question)
        actions = {"tuiles": self.choosePersonnage,
                    "pouvoir": self.activatePouvoir,
                    "bloquer": self.bloqueChemin,
                    "sortie": self.bloqueChemin,
                    "position": self.movePersonnage,
                    "echanger": self.swapPersonnage,
                    "obscurcir": self.shadow,
        }
        try:
            actions[question]()
        except:
            pass




def writeRep(reponse):
    rf = open('./0/reponses.txt','w')
    rf.write(str(reponse))
    rf.close()

def lancer():
    fini = False
    parser = p.parser(0)
    ia = iaInspecteur(parser)
    old_question = ""
    while not fini:
        qf = open('./0/questions.txt','r')
        question = qf.read()
        #print(question)
        q = ia.parser.parseQuestion(question)
        qf.close()
        if question != old_question :
            ia.prepareAnswer(q)
            old_question = question
        infof = open('./0/infos.txt','r')
        lines = infof.readlines()
        ia.parser.parseInfo(lines)
        infof.close()
        if len(lines) > 0:
            fini = "Score final" in lines[-1]

    qf = open('./0/questions.txt', 'r+')
    qf.truncate()
    qf.close()
    print("partie finie")