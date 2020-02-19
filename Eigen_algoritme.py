from Backend import gekleurde_pincode_input
import random
'''
Voor deze heuristiek gaat de computer op base van de zw en wit pinnetjes de pincode ontrafelen

Voor deze strategie zijn er een bepaalde voorwaarde :
1.De pinnetjes worden gegeven :
    a.zwart (z) = juiste leteer, juiste positie
    b.wit (w)   = juiste letter, onjuiste positie
    c.none(n)   = onjuiste kleur, onjuiste positie
2. De pinnetje worden op de elke  positie van de gok weergegeven.
vb ABCD en ADEF geeft (z,w,n,n)
'''

def shuffle_w(previous_gok, g,score):
    'In a score where contains only zwart and w pinnetjes, the w will be shuffled'
    w_lst = []
    w_index =[]
    for i in range(0,len(score)):
        if score[i] == 'w':
            w_lst.append(previous_gok[i])
            w_index.append(i)
        else:
            continue

    random.shuffle(w_lst)

    for i in range(0,len(w_index)):
        g[w_index[i]]= w_lst[i]
    return g



    return w_index
def zw_w_score_bepalen(p1, p2):
    'Zwart, wit pinnejtes bepalen van twee codes'
    zw_w_score = []
    p1list = []
    p2list = []

    #Haal aantal zwart op en zet rest van p1 en p2 in aparte lijsten
    for i in range(0, len(p1)):
        if p2[i] == p1[i]:
            zw_w_score.append('z')
        elif p2[i] in p1:
                zw_w_score.append(('w'))
        else:
            zw_w_score.append('n')
    return zw_w_score


def eigen_strategie():
    sc = gekleurde_pincode_input()
    i=0
    while i<= 10:
        if i ==0:
            g = ['A','A','B','B']
            score = zw_w_score_bepalen(sc, g)
        else:
            g = gokken_bepalen(g, score)
            score = zw_w_score_bepalen(sc, g)

        if score == ['z','z','z','z']:
            return 'win'
            break
        else:
            i+=1
            continue
    return 'lose'

            



def gokken_bepalen(previous_gok,score):
    'Aan de hand van de zwart/wit pinnejtes wordt de volgende gok bepaalt'
    a=0
    g = []
    ll= ['A','B', 'C','D','E','F']
    ll2 =[]
    while a<10:
        if score ==['n','n','n','n']:
            del ll['A']
            del ll['B']
            for i in ll:
                if g <4:
                    g.append(i * 2)
            return g
         # insert elements of previous_gok that is de same colour and position as sc
        if 'z' in score:#insert all element in previous_gok met score zw in g
            for i in range(0,len(score)):
                if score[i] == 'z':
                        g.insert(i, previous_gok[i])
                        score[i]= 'x'
                else:
                    g.insert(i,'x')
            a+=1
        elif 'w' in score:
                if 'n' in score:# if teh score contains a mixture of n en w. We would like to change n to w
                    for i in range(0,len(score)):
                        if score =='x':
                            continue
                        elif score[i]=='w':
                            g.insert(score.index('w'), previous_gok[i])
                        else:# score[i] =='n':
                            g.insert(i, random.choice(ll))

                else:
                    g = shuffle_w(previous_gok, g, score)

                return g
                break






