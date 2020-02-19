from Spel import codebreker, codemaker
from Eigen_algoritme import eigen_strategie

while True:
    print('''
        MASTERMIND
        Mastermind is een spel waar de ene speler probeert 
        de geheime code van de andere speler te ontrafelen.
        
        De codemaker kiest in het geheim vier code-pionnen.De codebreker heeft 10 kans
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
        uitslag = codebreker()
        if uitslag == 'win':
            print('Gefeliciteerd, je hebt gewonnen')
        elif uitslag == 'lose':
            print('Jammer, je hebt verloren')
        else:
            print('Error')


    elif ans == '2':
        print(
            '''
            Je hebt gekozen voor codemaker. Het computer heeft 2 verschillende strategie 
            om uw code te ontrafelen.
            1.Functie codemaker : Simple strategy
            2.Functie eigen_strategie : Eigen heuristiek
            '''
        )
        antw = input('Kies strategie 1 of 2: ')
        if antw == '1':
            uitslag = codemaker()
            if uitslag == 'win':
                print('Computer heeft gewonnen')
            elif uitslag == 'lose':
                print('Computer heeft verloren')

            else:
                print('Error')

        elif antw == '2':
            uitslag = eigen_strategie()
            if uitslag == 'win':
                print('Computer heeft gewonnen')
            elif uitslag == 'lose':
                print('Computer heeft verloren')

            else:
                print('Error')

    elif ans =='3':
        break
        print('\n Goodbye')
    elif ans !='':
        print('\n Not Valid Choice Try again')

'''
Bron:

Create a menu:  https://stackoverflow.com/questions/19964603/creating-a-menu-in-python
'''
