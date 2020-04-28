import string


#lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
def generate_lijst_letters (n):
    'Generate a list that contains n letters'
    lijst_letters = list(string.ascii_uppercase)
    return lijst_letters[:n]

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

'''
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
'''

'''
def join_string(lst):
    'Lst to string'
    s = ''
    return s.join(lst)
'''


#Interface ans 2
'''
        if uitslag == 'win':
            print('Computer heeft gewonnen')
        elif uitslag == 'lose':
            print('Computer heeft verloren')

        else:
            print('Error')
    '''

# antw = input('Kies strategie 1 of 2: ')
# if antw == '1':