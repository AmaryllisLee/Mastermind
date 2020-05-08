import random
import string
import itertools


'''
voor dit opdracht gaat ik gebruikmaken van letters A-F om de kleuren te definieren en berekingnen te doen
'''

#lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
def generate_lijst_letters (aLetters):
    'Generate a list that contains n letters'
    lijst_letters = list(string.ascii_uppercase)
    return lijst_letters[:aLetters]




def gekleurde_pincode_genereren(aPositie, aLetters):
    lijst_letters = generate_lijst_letters(aLetters)
    pincode = []
    for i in range(aPositie):
        pincode.append(random.choice(lijst_letters)) # Voeg toe een random kleur uit lijst kleur
    return pincode



def gekleurde_pincode_input(aPosities, aLetters):
    lijst_letters = generate_lijst_letters(aLetters)
    'Gebruiker maakt een n pincode uit  op basis van inputs '
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


#TODO Pas aan functie zodat die lijst generen voor alle pincodes met verschillende posities
def lst_combinatie_genereren(n):
    lijst_letters = generate_lijst_letters(n)
    'Alle mogelijke combinatie berkenen en in een set toevoegen'
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
    return lijst_alle_combinatie






'''
Bron :
lst_combinatie_genereren - Marya(student)

'''







