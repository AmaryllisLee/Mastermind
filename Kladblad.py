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

f