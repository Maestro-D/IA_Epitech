from random import shuffle,randrange
import parser as p

permanents, deux, avant, apres = {'rose'}, {'rouge','gris','bleu'}, {'violet','marron'}, {'noir','blanc'}
couleurs = avant | permanents | apres | deux
passages = [{1,4},{0,2},{1,3},{2,7},{0,5,8},{4,6},{5,7},{3,6,9},{4,9},{7,8}]
pass_ext = [{1,4},{0,2,5,7},{1,3,6},{2,7},{0,5,8,9},{4,6,1,8},{5,7,2,9},{3,6,9,1},{4,9,5},{7,8,4,6}]

class joueur:
    def __init__(self,n):
        self.numero = n
        self.role = "l'inspecteur" if n == 0 else "le fantome"
    def jouer(self,party):
        informer("****\n  Tour de "+self.role)
        p = self.selectionner(party.tuiles_actives)
        avec = self.activer_pouvoir(p,party,avant|deux)
        self.bouger(p,avec,party.bloque)
        self.activer_pouvoir(p,party,apres|deux)
    def selectionner(self,t):
        w = demander("Tuiles disponibles : " + str(t) + " choisir entre 0 et " + str(len(t)-1),self)
        i = int(w) if w.isnumeric() and int(w) in range(len(t)) else 0
        p = t[i]
        informer("REPONSE INTERPRETEE : "+str(p))
        informer(self.role + " joue " + p.couleur)
        del t[i]
        return p
    def activer_pouvoir(self,p,party,activables):
        if p.pouvoir and p.couleur in activables:
            a = demander("Voulez-vous activer le pouvoir (0/1) ?",self) == "1"
            informer("REPONSE INTERPRETEE : "+str(a==1))
            if a :
                informer("Pouvoir de " + p.couleur + " activé")
                p.pouvoir = False
                if p.couleur == "rouge":
                    draw = party.cartes[0]
                    informer(str(draw) + " a été tiré")
                    if draw == "fantome":
                        party.start += -1 if self.numero == 0 else 1
                    elif self.numero == 0:
                        draw.suspect = False
                    del party.cartes[0]
                if p.couleur == "noir":
                    for q in party.personnages:
                        if q.position in {x for x in passages[p.position] if x not in party.bloque or q.position not in party.bloque} :
                            q.position = p.position
                            informer("NOUVEAU PLACEMENT : "+str(q))
                if p.couleur == "blanc":
                    for q in party.personnages:
                        if q.position == p.position and p != q:
                            dispo = {x for x in passages[p.position] if x not in party.bloque or q.position not in party.bloque}
                            w = demander(str(q) + ", positions disponibles : " + str(dispo) + ", choisir la valeur",self)
                            x = int(w) if w.isnumeric() and int(w) in dispo else dispo.pop()
                            informer("REPONSE INTERPRETEE : "+str(x))
                            q.position = x
                            informer("NOUVEAU PLACEMENT : "+str(q))
                if p.couleur == "violet":
                    informer("Rappel des positions :\n" + str(party))
                    co = demander("Avec quelle couleur échanger (pas violet!) ?",self)
                    if co not in couleurs:
                        co = "rose"
                    informer("REPONSE INTERPRETEE : "+co)
                    q = [x for x in party.personnages if x.couleur == co][0]
                    p.position, q.position = q.position, p.position
                    informer("NOUVEAU PLACEMENT : "+str(p))
                    informer("NOUVEAU PLACEMENT : "+str(q))
                if p.couleur == "marron":
                    return [q for q in party.personnages if p.position == q.position]
                if p.couleur == "gris":
                    w = demander("Quelle salle obscurcir ? (0-9)",self)
                    party.shadow = int(w) if w.isnumeric() and int(w) in range(10) else 0
                    informer("REPONSE INTERPRETEE : "+str(party.shadow))
                if p.couleur == "bleu":
                    w = demander("Quelle salle bloquer ? (0-9)",self)
                    x = int(w) if w.isnumeric() and int(w) in range(10) else 0
                    w = demander("Quelle sortie ? Chosir parmi : "+str(passages[x]),self)
                    y = int(w) if w.isnumeric() and int(w) in passages[x] else passages[x].copy().pop()
                    informer("REPONSE INTERPRETEE : "+str({x,y}))       
                    party.bloque = {x,y}
        return [p]
                    
    def bouger(self,p,avec,bloque):
        pass_act = pass_ext if p.couleur == 'rose' else passages
        if p.couleur != 'violet' or p.pouvoir:
            disp = {x for x in pass_act[p.position] if p.position not in bloque or x not in bloque}
            w = demander("positions disponibles : " + str(disp) + ", choisir la valeur",self)
            x = int(w) if w.isnumeric() and int(w) in disp else disp.pop()
            informer("REPONSE INTERPRETEE : "+str(x))
            for q in avec:
                q.position = x
                informer("NOUVEAU PLACEMENT : "+str(q))

def ia_main(q):
    writeRep(randrange(6))

def writeRep(reponse):
    rf = open('./1/reponses.txt','w')
    rf.write(str(reponse))
    rf.close()

def lancer():
    fini = False
    parser = p.parser(1)
    old_question = ""
    while not fini:
        qf = open('./1/questions.txt','r')
        question = qf.read()
        q = parser.parseQuestion(question)
        qf.close()
        if question != old_question :
            ia_main(q)
            old_question = question
        infof = open('./1/infos.txt','r')
        lines = infof.readlines()
        parser.parseInfo(lines)
        infof.close()
        if len(lines) > 0:
            fini = "Score final" in lines[-1]
