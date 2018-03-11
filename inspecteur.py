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
        self.current_perso = p.personnage
        self.tuiles_dispo = []
        self.parser = parser
        self.nbSuspect = 8
        self.tuile_choose = 0
        self.eval_salle = 0
        self.new_salle = 0
        self.copy_map = {}


    def play(self):
        alpha = -10000
        depth = 1
        self.copy_map = self.parser.getAllPersonnage()
        for perso in self.tuiles_dispo:
            old_position = perso.position
            index = 0
            for pos in passages[perso.position]:
                perso.position = pos
                self.copy_map[perso.couleur].position = pos
                self.tuiles_dispo.remove(perso)
                beta = self.mini(depth)
                if beta >= alpha:
                    print("eee")
                    alpha = beta
                    self.tuile_choose = index
                    print(self.tuile_choose)
                    self.new_salle = pos
                perso.position = old_position
                self.copy_map[perso.couleur].position = old_position
                self.tuiles_dispo.insert(0, perso)
                index += 1

    def mini(self, depth):
        if depth == 0:
            return self.eval()
        beta = 10000
        for perso in self.tuiles_dispo:
            old_position = perso.position
            for pos in passages[perso.position]:
                perso.position = pos
                self.copy_map[perso.couleur].position = pos
                self.tuiles_dispo.remove(perso)
                alpha = self.maxi(depth - 1)
                if beta < alpha:
                    alpha = beta
                perso.position = old_position
                self.copy_map[perso.couleur].position = old_position
        return beta

    def maxi(self, depth):
        if depth == 0:
            return self.eval()
        alpha = -10000
        for perso in self.tuiles_dispo:
            old_position = perso.position
            for pos in passages[perso.position]:
                perso.position = pos
                self.copy_map[perso.couleur].position = pos
                self.tuiles_dispo.remove(perso)
                beta = self.mini(depth - 1)
                if beta > alpha:
                    alpha = beta
                perso.position = old_position
                self.copy_map[perso.couleur].position = old_position
        return alpha

    def eval(self):
        partition = [{p for p in self.copy_map if p.position == i} for i in range(10)]
        score = 0
        for piece,gens in enumerate(partition):
            if len(gens) == 1 or piece == self.shadow:
                for p in gens:
                    score += 1
        return score

    def choosePersonnage(self):
        self.tuiles_dispo = self.parser.getTuiles()
        if len(self.tuiles_dispo) <= 2:
            self.play()
            writeRep(self.tuile_choose)
            print(self.tuile_choose)
        writeRep("0")
        return

    def activatePouvoir(self):
        if self.current_perso.couleur == "rouge":
            writeRep("1")
        return

    def bloqueChemin(self):
        #print("c")
        return

    def movePersonnage(self):
        writeRep(self.new_salle)
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