from Backend import lst_combinatie_genereren, pincodes_vergelijken, join_string

def f_noname1(i, combinatielijst):
    'lijst geeft met de mogelijkheden van 1 element met alle mog combinatie'
    lst= []
    for j in combinatielijst:
        noname_var = pincodes_vergelijken(i,j)
        if noname_var == (4,0):
            continue
        else:
            lst.append(noname_var)
    return lst

def categoriseren_dict(i,lst):
    dict = {
        (3, 0): 0,
        (2, 2): 0,
        (2, 1): 0,
        (2, 0): 0,
        (1, 4): 0,
        (1, 3): 0,
        (1, 2): 0,
        (1, 1): 0,
        (1, 0): 0,
        (0, 4): 0,
        (0, 3): 0,
        (0, 2): 0,
        (0, 1): 0,
        (0, 0): 0,
    }
    for j in lst[i]:
        if j in dict.keys():
            dict[j] +=1
        else:
            continue
    return dict

def lijst():
    possible_combination_feedbacks = []
    pincode = []
    a = lst_combinatie_genereren()
    for i in a:
        fb = f_noname1(i, a) # geeft een lijst met de feedbacks van i en alle combinatie uit de lijst
        possible_combination_feedbacks.append(fb) # krijgt een nested list van van alle feedb
        pincode.append(i)
    return pincode, possible_combination_feedbacks



def lijst_categoriseren():
    'Elke lijst van feedbacks categoriseren '
    dict_res= {}
    code,possible_combination_feedbacks = lijst()

    for i in code:
        for j in range(0,len(possible_combination_feedbacks)):
            dct = categoriseren_dict(j,possible_combination_feedbacks)
            dict_res[join_string(i)] = dct
    return dict_res
#code, possible_combination_feedbacks = lijst()
#print(code[0], categoriseren_dict(0, possible_combination_feedbacks))

'''
Voor dit algoritme was de bedoeling om dmv van het artikel van  Unversiteit van Groningen ( 'Yet another mastermind by Barteld Kooi') de opvolgende gok(gok 2 3,etc te bepalen0:

Voor elke mogelijke combinatie in alle combinatie
        de feedback van de mogelijke combinatie met alle mogelijke combinatie bepalen 

Deze lijst van feedbacks categoriseren in (0,0) - (3,0). Hier krijgen we een overzicht van de verdeling van de feedbacks van 1 mogelijke combinatie
vb bij het runnen van regel 61 krijg je ['A', 'A', 'A', 'A'] 
{(3, 0): 20, (2, 2): 0, (2, 1): 0, (2, 0): 150, (1, 4): 0, (1, 3): 0, (1, 2): 0, (1, 1): 0, (1, 0): 500, (0, 4): 0, (0, 3): 0, (0, 2): 0, (0, 1): 0, (0, 0): 625}

Met deze verdeling van feedbacks voor alle mogelijke combinatie kunnen we zien voor welke mogeijke combinatie het meest combinatie schrappen uit mijn lijst van alle combinatie. 
Hiermee kunnen we gok n bepalen ( met het gedachte dat gok 1 = AABC]


'''



