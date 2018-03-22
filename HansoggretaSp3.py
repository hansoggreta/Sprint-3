#!/usr/bin/env python
# -*- coding: latin-1 -*-
import os
import sys
import turtle

from turtle import Turtle, Screen

import time


class HansogGretaSp3(object):
     def getName(self): pass
     def getDescription(self): pass
     def Visbending(self): pass
     def Tapalifi(self): pass
     def StartingProblem(self): pass
     def problem1(self): pass
     def problem2(self): pass
     def problem3(self): pass
     def problem4(self): pass

class Lif(HansogGretaSp3):
    def __init__(self, herb, hjalp): #Hér vil ég að við tökum líka inn lífin og tilraunirnar sem við eigum eftir...
        self.herb = herb
        self.hjalp = hjalp
        #self.lif = lif
        #self.tilraun = tilraun

        if self.hjalp == True:
            self.Visbending()
        '''if self.hjalp == True and self.lif <= 1:
            with open('NeitaVísbendingu.txt',encoding = "utf-8") as spurning:
                data = spurning.read()
                print(data)'''

        '''if self.tilraun == 0:
            self.TapaLifi'''

    def Visbending(self):
        #Birtir visbendingu sé þess óskað
        if self.herb == 1:
            print('Þetta er vísbending')
        if self.herb == 2:
            with open('visbending2.txt',encoding = "utf-8") as spurning:
                data = spurning.read()
                print(data)

        if self.herb == 3:
            pass
        if self.herb == 4:
            pass

    def TapaLifi(self):
        #Tekur burtu líf og ef lífin klárast þá gerist eitthvað skemmtilegt...
        '''self.lif = self.lif-1
        return self.lif'''



class Herbergi(HansogGretaSp3):
    def __init__(self, name, herb):
        self.name= name
        self.herb= herb
        self.tilraunir = 10
        self.StartingProblem()

    def StartingProblem(self): #Method sem býr til þraut, g.r.f. að hluturinn self.herb haldist hér úr smið, t.d. ef self.herb == 1 þá helst það hér
        description= self.getDescription()
        print(description)
        if self.herb == 1:
            self.problem1()
        elif self.herb == 2:
            self.problem2()
        elif self.herb == 3:
            self.problem3()
        elif self.herb == 4:
            self.problem4()

    def problem1(self):
        self.tilraunir = 10
        print('-------')
        print('ÞRAUT 1')
        print('-------')
        print('Búðu til fjögur fjögurra stafa orð úr stöfunum í orðinu: Piparkaka')
        print('Þú færð 10 tilraunir. Ef þú vilt fá vísbendingu skaltu skrifa "hjalp"')
        o = ['kaka', 'prik', 'rapp', 'apar']
        fundin = []
        NotaVisbendingu = False

        while self.tilraunir > 0:
            s1 = input('Orðið mitt:')
            hjalp = 'hjalp'
            if s1 == hjalp and NotaVisbendingu == False:
                print('Þú missir eina tilraun ef þú vilt sjá vísbendinguna')
                svar = input('Ertu viss um að þú viljir halda áfram? (j/n):')
                if svar == 'j':
                    hjalp = True
                    print('vísbending')
                    self.tilraunir = self.tilraunir - 1
                    NotaVisbendingu = True

            elif s1 == hjalp and NotaVisbendingu == True:
                print('Þú ert búinn að fá að sjá vísbendinguna')
            else:
                s1 = str(s1)
                s1 = s1.lower()
                if s1 in fundin:
                    print('Þú hefur þegar fundið þetta orð. Reyndu aftur')
                elif s1 in o:
                    print('Rétt hjá þér!')
                    fundin.append(s1)
                    del o[o.index(s1)]
                    if len(o) != 0:
                        print('Giskaðu á næsta orð.')
                    else:
                        print('Þú hefur fundið öll orðin!')
                        return
                else:
                    self.tilraunir -= 1
                    if self.tilraunir != 0:
                        print('Rangt svar. Reyndu aftur! Tilraunir eftir:'  + repr(self.tilraunir))
                    else:
                        print('Þú ert búin/n með allar tilraunirnar þínar og missir eitt líf.')
        return

    def problem2(self):
        time.sleep(1)
        tilraun = 3
        print('-------')
        print('ÞRAUT 2')
        print('-------')
        with open('thraut2.txt',encoding = "latin-1") as spurning:
            data = spurning.read()
        print(data)
        self.s1 = 0
        hjalp = "hjalp"
        NotaVisbendingu = False
        while(self.s1 != 2 and tilraun > 0):
            self.s1 = input('Fjöldi umferða:')
            if self.s1 == hjalp and NotaVisbendingu == False:
                print("Test hjalp")
                print('Þú missir eina tilraun ef þú vilt sjá vísbendinguna')
                svar = input('Ertu viss um að þú viljir halda áfram? (j/n):')
                if svar == 'j':
                    NotaVisbendingu = True
                    Lif(self.herb, NotaVisbendingu)
                    tilraun = tilraun - 1

            elif self.s1 == hjalp and NotaVisbendingu == True:
                print('Þú ert búinn að fá vísbendinguna.')

            elif self.s1.isdigit() == True:
                self.s1 = int(self.s1)
                tilraun = tilraun - 1

                if tilraun > 0 and self.s1 != 2:
                    print('Rangt svar. Þú mátt reyna aftur. Þú átt eftir ' + repr(tilraun) + ' tilraunir')

                elif tilraun == 0 and self.s1 != 2:
                    print('Rangt svar. Þú ert búinn með allar tilraunirnar þínar. Þú ert búinn að missa eitt líf')
                    tilraun = 3
                    #lif = lif - 1 - Hér tapar maður lífi
            else:
                print('Þú verður að setja inn tölustaf. Ef þú vilt fá vísbendingu skaltu skrifa "hjalp"')

        print('Rétt hjá þér! Áfram í næsta herbergi.')
        return

    def problem3(self):
        time.sleep(1)
        tilraun = 5
        print('-------')
        print('ÞRAUT 3')
        print('-------')
        with open('thraut3.txt', encoding = 'latin-1') as spurning:
            data = spurning.read()
        print(data)

        print('Ýttu á einhvern takk á lyklaborðinu og þá mun birtast mynd af glugganum í kofanum.')

        a = 0
        while (a != 1 and tilraun > 0):
            a = input()
            print('Þú verður að ýta á einhvern takka til að glugginn birtist')
            break

        print("TEST") #gefur okkur villu í prófun (ef valið er utan 1)

        screen = turtle.Screen()
        screen.setup(600,600)
        screen.bgpic("gluggi.gif") #Finna út hvernig ég birti gluggann

        print("Test 1")

        s1 = 0
        hjalp = "hjalp"
        NotaVisbendingu = False
        while(s1 != 30 and tilraun > 0):
            s1 = input('Fjöldi ferninga:')
            if s1 == hjalp and NotaVisbendingu == False:
                print("Test hjalp")
                print('Þú missir eina tilraun ef þú vilt sjá vísbendinguna')
                svar = input('Ertu viss um að þú viljir halda áfram? (j/n):')
                if svar == 'j':
                    NotaVisbendingu = True
                    Lif(self.herb, NotaVisbendingu)
                    tilraun = tilraun - 1

            elif s1 == hjalp and NotaVisbendingu == True:
                print('Þú ert búinn að fá vísbendinguna.')

            elif s1.isdigit() == True:
                s1 = int(s1)
                tilraun = tilraun - 1

                if tilraun > 0 and s1 != 30:
                    print('Rangt svar. Þú mátt reyna aftur. Þú átt eftir ' + repr(tilraun) + ' tilraunir')

                elif tilraun == 0 and s1 != 30:
                    print('Rangt svar. Þú ert búinn með allar tilraunirnar þínar. Þú ert búinn að missa eitt líf')
                    tilraun = 5
                    #lif = lif - 1 - Hér tapar maður lífi

            else:
                print('Þú verður að setja inn tölustaf. Ef þú vilt fá vísbendingu skaltu skrifa "hjalp"')


        print('Rétt hjá þér! Áfram í næsta herbergi.')
        return

    def problem4(self):
        print('-------')
        print('ÞRAUT 4')
        print('-------')
        print('Hvað er 4+4?')
        s1 = input('Mitt svar:')
        s1 = int(s1)
        while(s1 != 8):
            print('Rangt svar. Reyndu aftur!')
            print('Hvað er 4+4?')
            s1 = input('Mitt svar:')
            s1 = int(s1)
        print('Rétt hjá þér!')
        return

    def getName(self):
        return self.name

    def getDescription(self):
        #time.sleep(1)
        print('Þú ert komin/n í herbergið:', self.name, '. Gangi þér vel að leysa þrautina.')
        if self.herb == 1:
            #time.sleep(1)
            return 'Lýsing: Herbergið þar sem vonda nornin horfir á sjónvarpið.'
        elif self.herb == 2:
            #time.sleep(1)
            return 'Lýsing: Herbergið þar sem vonda nornin sefur.'
        elif self.herb == 3:
            #time.sleep(1)
            return 'Lýsing: Herbergið þar sem vonda nornin tannburstar sig.'
        elif self.herb == 4:
            #time.sleep(1)
            print('Vonandi nær nornin ekki að elda Hans!')
            return 'Lýsing: Herbergið þar sem vonda nornin vill elda Hans.'

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
    with open('upphaf.txt',encoding = "latin-1") as texti:
        data = texti.read()
    print(data)
    VeljaPersonu = False
    while(VeljaPersonu == False):
        print("Hvort viltu leika Hans eða Grétu? Skrifaðu 1 fyrir Grétu eða 2 fyrir Hans.")
        val = input('Mitt val:' )
        if val.isdigit() == True:
            val = int(val)
            if val == 1:
                print("Þú hefur valið Grétu")
                s = Persona(1, 'Gréta', 'Lítil stelpa með ljóst hár')
                VeljaPersonu = True
            elif val == 2:
                print("Þú hefur valið Hans")
                name = 'Hans'
                s = Persona(0, 'Hans', 'Lítill strákur með dökkt hár')
                VeljaPersonu = True
            else:
                print("Þú þarft að skrifa 1 fyrir Grétu eða 2 fyrir Hans.")
        else:
            print('Þú verður að skrifa tölustaf')


    while(win == False):
    #    herb = input('Hvaða herbergi viltu fara í? Veldu 1 fyrir stofu, 2 fyrir svefnherbergi og 3 fyrir baðherbergi.')
    #    herb = int(herb)
        #time.sleep(1)

        herb = 1
        h1 = Herbergi('Stofa', herb)
        #input nýtt herbergi
        herb=2
        h2=Herbergi('Svefnherbergi', herb)

        herb=3
        h3=Herbergi('Baðherbergi', herb)

        herb=4
        h4=Herbergi('Eldhús', herb)

        win = True

    print('-----------------------')
    print('Þú hefur unnið leikinn!')
    print('-----------------------')
if __name__ == "__main__":
    main()
