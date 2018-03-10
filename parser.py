import re
permanents, deux, avant, apres = {'rose'}, {'rouge','gris','bleu'}, {'violet','marron'}, {'noir','blanc'}
couleurs = avant | permanents | apres | deux

class personnage:
    def __init__(self,couleur):
        self.couleur, self.suspect, self.position, self.pouvoir = couleur, True, 0, True
    def __repr__(self):
        susp = "-suspect" if self.suspect else "-clean"
        return self.couleur + "-" + str(self.position) + susp

class parser:
    def __init__(self, joueur):
        self.joueur = joueur
        self.personnage = {personnage(c) for c in couleurs}
        self.lines = ""
        self.score = 4
        self.shadow = 0
        self.bloque = {0,0}
        self.tuiles_dispo = []

    def parseQuestion(self, line):
        if "Tuiles" in line:
            elem = line.replace("[","")
            elem = elem.replace(",","")
            infos = elem.split(" ")
            self.tuiles_dispo = []
            for info in infos:
                for c in couleurs:
                    if c in info:
                        self.tuiles_dispo.append(self.getPersonnage(c))
            return "tuiles"
        if "pouvoir" in line:
            return "pouvoir"
        if "bloquer" in line:
            return "bloquer"
        if "sortie" in line:
            return "sortie"
        if "position" in line:
            return "position"
        if "échanger" in line:
            return "echanger"
        if "obscurcir" in line:
            return "obscurcir"

    def parseInfo(self, lines):
        for line in lines:
            if "QUESTION" in line or "REPONSE" in line:
                continue
            infos = line.split(" ")
            for info in infos:
                if "Score" in info and "final" not in line:
                    elem = re.split(":|/", info)
                    self.score = int(elem[1])
                elif "Ombre" in info:
                    elem = info.replace("Ombre", "")
                    elem = elem.replace(":","")
                    elem = elem.replace(",","")
                    self.shadow = int(elem)
                for c in couleurs:
                    #print(line)
                    if c in info:
                        details = info.split("-")
                        if len(details) == 3:
                            self.setPosition(c, int(details[1]))



    def isSuspect(self, couleur):
        for p in self.personnage:
            if p.couleur == couleur:
                return p.suspect
    def setPosition(self, couleur, position):
        for p in self.personnage:
            #print(p)
            if p.couleur == couleur:
                p.position = position
    def getPosition(self, couleur):
        for p in self.personnage:
            if p.couleur == couleur:
                return p.position
    def getPersonnage(self, couleur):
        for p in self.personnage:
            if p.couleur == couleur:
                return p
    def getAllPersonnage(self):
        all_perso = {}
        for p in self.personnage:
            all_perso[p.couleur]= p
        return all_perso
    def getTuiles(self):
        return self.tuiles_dispo
    def getPersonnageWithHim(self, perso):
        groupPerso = []
        for p in self.personnage:
            if perso.position == p.position and perso.couleur != p.couleur:
                groupPerso.append(p)
        return groupPerso
