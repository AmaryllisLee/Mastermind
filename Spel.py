from Backend import gekleurde_pincode_input, gekleurde_pincode_genereren, lst_combinatie_genereren, pincodes_vergelijken,lijst_schrappen, gok_checken


lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']

def codebreker():
    'Op basis van de input van de user, gaat de codemaker de geheime code  proberen te raden'
    secret_code = gekleurde_pincode_genereren() #
    print(secret_code)
    i=0
    while i<= 10:
        gok = gekleurde_pincode_input()
        feedb = pincodes_vergelijken(secret_code, gok)
        if  feedb[0]==4 and feedb[1] ==0 :
            return('win')
        else:
            print('Wrong guess, try again: {}, {}'.format(gok, feedb))
            i+=1
    return 'lose'



def spel_computer_tegen_men():
    'Computer moet de secret code raden'
    '''
    Simple strategy
    Voor deze algoritme gaan we eerst een gok vergelijken met de secret code.
    Daarna wordt het gok vergeleken met alle mogelijk pincode
    '''
    lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
    secret_code = gekleurde_pincode_input()  # secret pincode van de speler
    lijst_alle_combinatie = lst_combinatie_genereren()

    i=0
    while i <=10:
        if i == 0:
            gok = ['A','A','B','C']
            z_w_feedback = pincodes_vergelijken(secret_code,gok)
        else:
             gok,z_w_feedback = gok_checken(secret_code,lijst_alle_combinatie) # TODO ALgoritme vabn Algoritme.py implementeren


        if z_w_feedback == (4, 0):
                return ('win')
        else:
            lijst_alle_combinatie = lijst_schrappen(gok, z_w_feedback, lijst_alle_combinatie)
            i += 1
            continue
    return ('lose')







