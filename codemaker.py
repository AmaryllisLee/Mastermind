from Backend import gekleurde_pincode_input, gekleurde_pincode_genereren, lst_combinatie_genereren, pincodes_vergelijken,lijst_schrappen, gok_checken


def input_keypegs(code, guess, tries):
    'This function lets the user compare the two codes and return keypegs'
    controle_keypegs = pincodes_vergelijken(code, guess) # This used to check that the user is not cheating
    amount_tries = 0 # This gives the user 3 chances to guess correctly, else the program will use the controle_keypegs

    print('''
    
    {} try : 
    Your code     : {}
    Computer guess: {}
    
    {} for now
    '''.format(tries, code, guess, controle_keypegs))
    while amount_tries !=3:

        zwart_keypegs = int(input('How many black keypegs? '))
        wit_keypegs = int(input('How many white keypegs? '))
        user_keypegs = (zwart_keypegs, wit_keypegs)
        if user_keypegs != controle_keypegs:
            print('This is not the correct keypegs, Try again')
            continue
        else:
            break

    return user_keypegs


lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
def codemaker_versie2():
    'AI has to break code'

    # user chooses 4 pin code that consist of lijst_letters
    code = gekleurde_pincode_input()

    # Generate list of all possible combination
    possible_comibinations = lst_combinatie_genereren()

    c =0 # c

    # Compare the first element of list possible_combination(guess) with code.
    # If guess is not equal with code, the key pegs will be generated.
    while c <= 10:
        guess = possible_comibinations[0]
        key_pegs = pincodes_vergelijken(code, guess) # user can give keypegs, to make it easier change it to pincode_vergelijken
        #TODO change function pincode_vergelijken to input_keypegs
        if key_pegs == (4,0):
            print('{}, {} in  {} tries, Computer win'.format(guess, key_pegs, c))
            break
        else:
            #Based on the generated key pegs, the list of possible_commbination will be modified.
            lijst_schrappen(guess, key_pegs, possible_comibinations)
            print(code,guess, key_pegs, len(possible_comibinations))

            c+=1
            continue
            print(code,guess, key_pegs, len(possible_comibinations))
    



