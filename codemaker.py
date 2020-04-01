from Backend import gekleurde_pincode_input, gekleurde_pincode_genereren, lst_combinatie_genereren, pincodes_vergelijken,lijst_schrappen, gok_checken

'''

'''

lijst_letters = ['A', 'B', 'C', 'D', 'E', 'F']
def codemaker_2():
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
        key_pegs = pincodes_vergelijken(code, guess)

        if key_pegs == (4,0):
            print('{},{},{} tries, You win'.format(guess, key_pegs, c))
            break
        else:
            #Based on the generated key pegs, the list of possible_commbination will be nodify.
            lijst_schrappen(guess, key_pegs, possible_comibinations)
            print(code,guess, key_pegs, len(possible_comibinations))

            c+=1
            continue
            print(code,guess, key_pegs, len(possible_comibinations))

    print('Computer loses')


codemaker_2()