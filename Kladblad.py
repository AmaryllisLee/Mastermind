lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']


def gekleurde_pincode_input2():
    'Gebruiker maakt een 4 pincode uit  op basis van inputs '
    while True:
        kleur = input('Geeft aan een code van vier letters van A t/m F:  ')
        list_kleur =  list(kleur)

        if  len(list_kleur) == 4:

            return list_kleur
            break
        else:
            print('{} is not correct, Try another one'.format(list_kleur))
            continue
'''
Eigen Heuristiek
lif antw == '2':
            uitslag = eigen_strategie()
            if uitslag == 'win':
                print('Computer heeft gewonnen')
            elif uitslag == 'lose':
                print('Computer heeft verloren')

            else:
                print('Error')
'''

'''
Codemaker oude versie
def codemaker():
    'Computer moet de secret code raden'

    #Simple strategy
    #Voor deze algoritme gaan we eerst een gok vergelijken met de secret code.
    #Daarna wordt het gok vergeleken met alle mogelijk pincode


    secret_code = gekleurde_pincode_input()  # secret pincode van de speler
    lijst_alle_combinatie = lst_combinatie_genereren()

    i=0
    while i <=10:
        if i == 0:
            gok = ['A','A','B','C']
            z_w_feedback = pincodes_vergelijken(secret_code,gok)
        else:
             gok,z_w_feedback = gok_checken(secret_code,lijst_alle_combinatie)

        if z_w_feedback == (4, 0):
                return ('win')
        else:
            lijst_alle_combinatie = lijst_schrappen(gok, z_w_feedback, lijst_alle_combinatie)
            i += 1
            continue
    return ('lose')

'''