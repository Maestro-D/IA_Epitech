from random import shuffle,randrange
from time import sleep

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

def lancer():
    fini = False
    old_question = ""
    while not fini:
        qf = open('./0/questions.txt','r')
        question = qf.read()
        qf.close()
        if question != old_question :
            rf = open('./0/reponses.txt','w')
            rf.write(str(randrange(2)))
            rf.close()
            old_question = question()
        infof = open('./0/infos.txt','r')
        lines = infof.readlines()
        infof.close()
        if len(lines) > 0:
            fini = "Score final" in lines[-1]
    print("partie finie")