class HansogGretaSp3(object):
     def getName(self): pass
     def getDescription(self): pass
     def answer(self): pass
     def move(self): pass
     def kill(self): pass
     def clue(self): pass
     def removeElement(self): pass
     def eldhusLokad(self): pass

class Herbergi(HansogGretaSp3):
    def __init__(self, name, herb):
        self.name= name
        self.herb= herb
        if self.herb == 1:
            #self.herb='Herbergi 1'
            self.StartingProblem()
        else:
            #self.herb='Herbergi 2'
            self.StartingProblem()

    def StartingProblem(self): #Method sem býr til þraut, g.r.f. að hluturinn self.herb haldist hér úr smið, t.d. ef self.herb == 1 þá helst það hér
        description= self.getDescription()
        print(description)
        if self.herb == 1:
            self.problem1()
        else:
            self.problem2()

    def problem1():
        description= self.getDescription()
        print(description)
        print('hæ')

    def problem2():
        description= self.getDescription()
        print(description)

    def getName(self):
        return self.name
    def getDescription(self):
        if self.herb == 1:
            print('Þú ert í herberginu:', self.name)
            return 'Herbergið þar sem vonda nornin horfir á sjónvarpið'
        else:
            return 'Herbergið þar sem vonda nornin sefur'
        #else:
        #    return 'Herbergið þar sem vonda nornin fer á klósettið'

class Persona(Herbergi):
    def __init__(self, kyn, name, description):
        self.name= name
        self.description= description
        self.kyn= kyn

    def getName(self):
        return self.name

    def getDescription(self):
        return self.description
    def kyn(self):
        if self.kyn == 1:
            return 'Kvenkyns'
        else:
            return 'Karlkyns'

def main():
    win = False #Verður true þegar allar þrautirnar i leiknum hafa verið leystar
    while(1):
        print("Hvort viltu leika Hans eða Grétu? Skrifaðu 1 fyrir Grétu eða 2 fyrir Hans.")
        val = input('Mitt val:' )
        val = int(val)
        if val == 1:
            print("Þú hefur valið Grétu")
            s = Persona(1, 'Gréta', 'Lítil stelpa með ljóst hár')
            break
        elif val == 2:
            print("Þú hefur valið Hans")
            name = 'Hans'
            s = Persona(0, 'Hans', 'Lítill strákur með dökkt hár')
            break
        else:
            print("Þú þarft að skrifa 1 fyrir Grétu eða 2 fyrir Hans.")
            val = input ('Mitt val: ')
            val = int(val)
    while(win == False):
    #    herb = input('Hvaða herbergi viltu fara í? Veldu 1 fyrir stofu, 2 fyrir svefnherbergi og 3 fyrir baðherbergi.')
    #    herb = int(herb)
        print('Þú ert komin/n í stofuna. Gangi þér vel að leysa þrautina.')
        herb = 1
        h1 = Herbergi('Stofa', herb)
        #input nýtt herbergi
        herb=2
        h2=Herbergi(herb, des)

if __name__ == "__main__":
    main()
