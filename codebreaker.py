from Backend import gekleurde_pincode_input, gekleurde_pincode_genereren, pincodes_vergelijken,generate_lijst_letters

'''
Voor dit opdracht gaat ik gebruik maken van letters A-F in plaats van kleuren.
De reden is voor een goede overzichtelijkheid van de pincodes.
'''


def codebreaker(aPositie,aLetters):
    lijst_letters = generate_lijst_letters(aLetters)
    'Op basis van de input van de user, gaat de codemaker de geheime code  proberen te raden'
    secret_code = gekleurde_pincode_genereren(aPositie,aLetters) #
    print(secret_code) # secret code is geprint om te de functie te testen
    i=0
    while i<= 10:
        gok = gekleurde_pincode_input(aPositie,aLetters)
        feedb = pincodes_vergelijken(secret_code, gok)
        if  feedb[0]==aPositie and feedb[1] ==0 :
            return('win')
        else:
            print('Wrong guess, try again: {}, {}'.format(gok, feedb))
            i+=1
    return 'lose'








'''
Bron :
Shuffle  a list :https://pynative.com/python-random-shuffle/

'''


