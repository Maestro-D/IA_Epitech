from random import shuffle,randrange
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

class ia:
    def __init__(self, parser):
        self.parser = parser
        self.persoBM = personnage("rose")
        self.bloque = {}
        self.tuilesDispo = parser.getTuiles()
        self.listePerso = parser.getAllPersonnage()
        self.passageBM = 0

    def ia_main(self, q):
        self.writeRep(randrange(6))
        if q == "tuiles":
            self.choicePerso(self.parser.getTuiles())
        elif q == "pouvoir":
            self.activatePower()
        elif q == "bloquer":
            self.closePath()
        elif q == "sortie":
            self.closeExit()
        elif q == "position":
            self.move()
        elif q == "echanger":
            self.choiceChange()
        elif q == "obscurcir":
            self.makeNight()
        else:
            return
    
    def choicePerso(self, listeTuile):
        persoBM = self.simulate(listeTuile, self.parser.personnage)
        tmp = 0
        for p in listeTuile:
            if p.couleur == persoBM.couleur:
                self.writeRep(tmp)
                return tmp
            tmp += 1
        print("\nSHOULD NOT BE THERE ! in choicePerso line 127\n")
        return tmp

    def activatePower(self):
        self.writeRep(0)

    def closePath(self):
        #print("CLOSE PATH")
        return

    def closeExit(self):
        #print("CLOSE EXIT")
        return

    def move(self):
        #print("MOVE")
        self.writeRep(self.passageBM)
        return

    def choiceChange(self):
        #print("CHANGE")
        return

    def makeNight(self):
        #print("NIGHT SHALL FALL")
        return

    def writeRep(self, reponse):
        rf = open('./1/reponses.txt','w')
        rf.write(str(reponse))
        rf.close()

    def simulate(self, persos, allPerso):
        miniBM = 100
        passageBM = 0
        for _perso in persos:
            ret = self.moveIt(allPerso, _perso)
            mini = ret[0]
            passage = ret[1]
            if mini < miniBM:
                miniBM = mini
                self.passageBM = passage
                persoBM = _perso
        return persoBM

    def moveIt(self, allPerso, perso):
        mini = 100
        tmpPosition = perso.position
        if perso.couleur != 'rose': 
            myPass = passages[perso.position]
        else:
            myPass = pass_ext[perso.position]
        for k in myPass:
            perso.position = k
            cpt = self.cptAlone(allPerso) 
            if cpt < mini:
                mini = cpt
                passBM = k
            perso.position = tmpPosition
        return mini, passBM

    def cptAlone(self, persos):
        carte = [0,0,0,0,0,0,0,0,0,0]
        score = 0
        for _perso in persos:
            carte[_perso.position] = carte[_perso.position] + 1
        for room in carte:
            if room == 1:
                score += 1
        return score        

def lancer():
    fini = False
    parser = p.parser(1)
    fantome = ia(parser)
    old_question = ""
    while not fini:
        qf = open('./1/questions.txt','r')
        question = qf.read()
        #print(question)
        q = parser.parseQuestion(question)
        qf.close()
        if question != old_question :
            fantome.ia_main(q)
            old_question = question
        infof = open('./1/infos.txt','r')
        lines = infof.readlines()
        parser.parseInfo(lines)
        infof.close()
        if len(lines) > 0:
            fini = "Score final" in lines[-1]
    qf = open('./1/questions.txt','r+')
    qf.truncate()
    qf.close()
    infof = open('./1/infos.txt','r+')
    infof.truncate
    infof.close()
    if len(lines) > 0:
            fini = "Score final" in lines[-1]
