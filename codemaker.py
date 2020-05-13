from Backend import gekleurde_pincode_input,lst_combinatie_genereren, pincodes_vergelijken, lijst_schrappen, generate_lijst_letters



def codemaker(aPosities, aLetters):
    'AI has to break code'

    lijst_letters = generate_lijst_letters(aLetters)
    # user chooses 4 pin code that consist of lijst_letters
    code = gekleurde_pincode_input(aPosities,aLetters)

    # Generate list of all possible combination
    possible_comibinations = lst_combinatie_genereren(aPosities,aLetters)


    print(code)
    # Compare the first element of list possible_combination(guess) with code.
    # If guess is not equal with code, the key pegs will be generated.
    for i in range(10):
        guess = possible_comibinations[0]
        key_pegs = pincodes_vergelijken(code, guess) # Bepaalt de feedback van de code en de gok

        if key_pegs == (aPosities,0):
            print('{}, {} in  {} tries, Computer win !!'.format(guess, key_pegs, i))
            break
        else:
                #Based on the generated key pegs, the list of possible_commbination will be modified.
                lijst_schrappen(guess, key_pegs, possible_comibinations)
                print('{} tries, {}, {}, {}  '.format(i,guess, key_pegs, len(possible_comibinations)))









