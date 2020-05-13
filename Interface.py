from codebreaker import codebreaker
from codemaker import codemaker

'''
Voor dit opdracht gaat ik gebruik maken van letters A-F in plaats van kleuren.
De reden is voor een goede overzichtelijkheid van de pincodes.
'''


while True:
    print('''
        MASTERMIND
        Mastermind is een spel waar de ene speler probeert 
        de geheime code van de andere speler te ontrafelen.
        
        De codemaker kiest in het geheim aantal code-pionnen die bestaat  uit gekozen aantal letters.De codebreker heeft 10 kans
        om de verborgen code te ontrafelen.Voor elke kans moet de codemaker een feedback
        geven:
        
        .zwart : de kleuren zijn dezelfde en staan op de juiste positie
        .wit   : de kleuren zijn dezelfde maar staan niet op de juiste positie
        
        Je kan kiezen voor:
     
        1.Codebreker: Je speelt tegen de computer

        2. Codemaker: Computer speelt tegen jou
            
        3.Exit/quit
        ''')

    ans = input('Welke kies je voor? ')

    if ans == '1':
        print('''
        Je hebt gekozen voor codebreaker
        ''')
        aantalLetters = int(input('Aantal letters ? '))
        aantalPosities = int(input('Aantal posities? '))
        uitslag = codebreaker(aantalPosities, aantalLetters)
        if uitslag == 'win':
            print('Gefeliciteerd, je hebt gewonnen')
        elif uitslag == 'lose':
            print('Jammer, je hebt verloren')
        else:
            print('Error')


    elif ans == '2':
        print(
            '''
            Je hebt gekozen voor codemaker. De computer maakt gebruik van de strategie Simple strategy.
            Bron voor Simple startegy: Yet another Mastermind Strategy van de Universiteit Groningen
            
            Je kan kiezen voor hoeveel letter en hoeveel posties die je wil gebruiken.
            '''
        )
        aantalLetters = int(input('Aantal letters? '))
        aantalPosities =int(input('Aantal posities? '))
        codemaker(aantalPosities,aantalLetters)

    elif ans =='3':
        print('\n Thank you for playing')
        break

    elif ans !='':
        print('\n Not Valid Choice Try again')



# Test - Voorbeeld inputs om programma te testen voor Simple Strategie
#1. codemaker : aantal letters = 19, aantal Posities = 7 , code = AEDBFSG
#2. codemaker : aantal letters = 6, aantal Posities = 4 , code = AABD
#3. codemaker : aantal letters = 26, aantal Posities = 3 , code = ZAF


'''
Bron:
Create a menu:  https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
'''
