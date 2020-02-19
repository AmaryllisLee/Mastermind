import random
from itertools import combinations
'''
voor dit opdracht gaat ik gebruikmaken van letters A-F om de kleuren te definieren en berekingnen te doen
A= rood
B= blauw
C = groen
D = geel 
E = Zwart
F = wit
'''


def gekleurde_pincode_genereren():
    lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
    pincode = []
    i=0
    while i<4:
        pincode.append(random.choice(lijst_letters)) # Voeg toe een random kleur uit lijst kleur
        i+=1
    return pincode



def gekleurde_pincode_input():
    'Gebruiker maakt een 4 pincode uit  op basis van inputs '
    lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
    pincode= []
    i=0
    while i<4:
        kleur= input('Geeft aan een letter van A t/m  F:  ')
        if kleur in lijst_letters:
            pincode.append(kleur)
            i+=1
        else:
            print('Error, je moet een letter van A t/m F aangeven')
    return pincode



def lst_combinatie_genereren():
    'Alle mogelijke combinatie berkenen en in een set toevoegen'
    lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
    alle_combinatie= []
    for i in lijst_letters:
        for j in lijst_letters:
            for h in lijst_letters:
                for g in lijst_letters:
                    alle_combinatie.append([i,j,h,g])
    return alle_combinatie



def pincodes_vergelijken(p1, p2):
    'twee pincodes vergelijken'
    zwart = 0
    wit = 0
    p1list=[]
    p2list=[]

    #Haal aantal zwart op en zet rest van p1 en p2 in aparte lijsten
    for i in range(0, len(p1)):
        if p1[i] == p2[i]:
            zwart+=1
        else:
            p1list.append(p1[i])
            p2list.append(p2[i])

    for i in range(0, len(p1list)):
        if p1list[i] in p2list:
            wit +=1
        else:
            continue

    return(zwart, wit)



def lijst_schrappen(gok, z_w_feedback,lijst_alle_combinatie):
    'Verwijder alle combinatie uit lijst waar feedback_comb_gok == z_w_feedback (feedb van secret code en gok)'



    for combinatie in lijst_alle_combinatie:
        feedback_comb_gok = pincodes_vergelijken(gok, combinatie)

        if feedback_comb_gok != z_w_feedback:
            lijst_alle_combinatie.remove(combinatie)
        else:
            continue
    return  lijst_alle_combinatie

def gok_checken(secret_code, lijst_alle_combinatie):
    alle_z_w_feedback_lst = []
    while True:
        gok = random.choice(lijst_alle_combinatie)  # returns een random combinatie uit de lijst
        z_w_feedback = pincodes_vergelijken(secret_code,gok)  # vergelijk pincodes met elkaar -> output aantal zwart en wit

        if z_w_feedback in alle_z_w_feedback_lst:
            continue
        else:
            alle_z_w_feedback_lst.append(z_w_feedback)
            return gok, z_w_feedback
        break




def join_string(s):
    str = ''
    return str.join(s)







# Bron - Marya






