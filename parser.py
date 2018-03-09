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
    def __init__(self):
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
            for info in infos:
                for c in couleurs:
                    if c in info:
                        self.tuiles_dispos.append(self.getPersonnage(c))
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
        if "obscursir" in line:
            return "obscursir"

    def parseInfo(self, lines):
        for line in lines:
            if "QUESTION" in line or "REPONSE" in line:
                break
            infos = line.split(" ")
            for info in infos:
                if "Score" in info:
                    elem = re.split(":|/", info)
                    self.score = int(elem[1])
                elif "Ombre" in info:
                    elem = info.replace("Ombre", "")
                    elem = elem.replace(":","")
                    elem = elem.replace(",","")
                    self.shadow = int(elem)
                for c in couleurs:
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

