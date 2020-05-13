from Backend import gekleurde_pincode_input, gekleurde_pincode_genereren, pincodes_vergelijken,generate_lijst_letters



def codebreaker(aPositie,aLetters):
    'Op basis van de input van de user, gaat de gebruiker de geheime code van de AI proberen te raden'

    secret_code = gekleurde_pincode_genereren(aPositie,aLetters) #er word een code genereert
    print(secret_code) # secret code is geprint om te de functie te testen
    i=0

    while i<= 10:
        gok = gekleurde_pincode_input(aPositie,aLetters)

        feedb = pincodes_vergelijken(secret_code, gok)# geeft feedback van de code en de gok

        if  feedb[0]==aPositie and feedb[1] ==0 :
            return('win')
        else:
            print('Wrong guess, try again: {}, {}'.format(gok, feedb))
            i+=1
    return 'lose'





