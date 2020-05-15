import random
import string

'''
Voor deze tweede spelmodus moet de lst_combiantie_genereren aangepast worden zodat die een lijst kan generen van alle mogelijke pincodes van n posities
in plaats van4 posities.Hier had ik op verschillende manieren geprobeerd maar het was niet gelukt.
Om het programma toch werkend te krijgen had ik gebruik maken van de functie n_length_combo() die ik online had gevonden.
Het enige probleem met deze functie is dat die genereert een lijst met alle unieke combinatie.
Bijvoorbeeld zal er  een lijst van 10 in plaats van 125 ( bij 3 posities en 5 aantal letters).
Daardoor is bij codemaker() beter om pincodes te vormen zonder herhaling vb AAB

'''

def generate_lijst_letters (aLetters):
    'Generate a list that contains n letters'
    lijst_letters = list(string.ascii_uppercase)#maakt een lijst uit de string 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return lijst_letters[:aLetters]# return lijst_letters to bepaalde index aLetters


def gekleurde_pincode_genereren(aPositie, aLetters):
    'Creeert een pincode die bestaat uit aPositie letters'
    lijst_letters = generate_lijst_letters(aLetters)
    pincode = []
    for i in range(aPositie):
        pincode.append(random.choice(lijst_letters)) # Voeg toe een random kleur uit lijst kleur
    return pincode



def gekleurde_pincode_input(aPosities, aLetters):
    'Gebruiker maakt een n pincode uit  op basis van inputs'
    lijst_letters = generate_lijst_letters(aLetters)
    pincode= []
    i=0

    while i < aPosities:
        letter= input('Geeft aan een letter van A t/m {}:  '.format(lijst_letters[-1]))
        if letter in lijst_letters:
            pincode.append(letter)
            i += 1
        else:
            print('Error, je moet een letter van A t/m {} aangeven'.format(lijst_letters[-1]))
    return pincode


def n_length_combo(lst, n):
    'Creeert een lijst van alle unieke combinatie uit een lijst '
    if n == 0:
        return [[]]

    l = []
    for i in range(0, len(lst)):

        m = lst[i]
        remLst = lst[i + 1:]

        for p in n_length_combo(remLst, n - 1):
            l.append([m] + p)

    return l


def lst_combinatie_genereren(aPositie, aLetters):
    'Alle mogelijke combinatie berkenen en in een set toevoegen'
    lijst_letters = generate_lijst_letters(aLetters)

    if aPositie == 4:
        alle_combinatie= []
        for i in lijst_letters:
            for j in lijst_letters:
                for h in lijst_letters:
                    for g in lijst_letters:
                        alle_combinatie.append([i,j,h,g])
        return alle_combinatie
    else:
        lstcombination = n_length_combo(generate_lijst_letters(aLetters), aPositie)
        return lstcombination


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
    return lijst_alle_combinatie



'''
Bron :
lst_combinatie_genereren - hulp van Marya(student in AI - V1B)
n_length_combo()- https://www.geeksforgeeks.org/combinations-in-python-without-using-itertools/
Lijst van de alfabet - https://stackoverflow.com/questions/16060899/alphabet-range-in-python
'''







