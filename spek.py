import random
import string
from zodziai_listas import zodziai


def atspeti_tinkama_zodi(zodziai):
    """
    Pasirenka atsitiktinį žodį iš pateikto žodžių sąrašo.

    Args:
    zodziai (list): Sąrašas galimų žodžių.

    Returns:
    str: Atsitiktinai pasirinktas žodis didžiosiomis raidėmis.
    """
    zodis = random.choice(zodziai)  # Atsitiktinai pasirenkamas žodis iš sąrašo 'zodziai'.
    return zodis.upper()  # Grąžiname žodį didžiosiomis raidėmis.


def spek():
    """
    Vykdo pagrindinį žodžių spėjimo žaidimą. Leidžia naudotojui spėti žodį
    raidę po raidės, nurodant, kiek spėjimų liko ir kurios raidės buvo bandytos.
    Žaidimas baigiasi, kai žodis atspėjamas arba baigiasi spėjimų skaičius.
    """
    zodis = atspeti_tinkama_zodi(zodziai)
    zodzio_raides = set(zodis)  # Unikalios žodžio raidės.
    abecele = set(string.ascii_uppercase + "ĄČĘĖĮŠŲŪŽ")  # Leidžiamų raidžių rinkinys.
    panaudotos_raides = set()  # Naudotojo jau bandytos raidės.

    spejimai = 8  # Pradinis spėjimų skaičius.

    # Vartotojo spėjimų ciklas
    while len(zodzio_raides) > 0 and spejimai > 0:
        print('Jūs turite', spejimai, 'spėjimus ir Jūs bandėte šias raides:', panaudotos_raides)

        # Dabartinė žodžio būsena su atspėtomis raidėmis ir '_'
        zodziai_list = [raide if raide in panaudotos_raides else '_' for raide in zodis]
        print('Dabartinis žodis: ', ''.join(zodziai_list))

        vartotojo_raide = input('Spėkite žodžio raidę: ').upper()  # Įvestą raidę paverčia į didžiąją.

        if vartotojo_raide in abecele - panaudotos_raides:
            # Jei raidė yra abėcėlėje ir dar nebuvo bandyta
            panaudotos_raides.add(vartotojo_raide)
            if vartotojo_raide in zodzio_raides:
                zodzio_raides.remove(vartotojo_raide)  # Pašalina atspėtą raidę iš neatspėtų raidžių rinkinio.
            else:
                spejimai -= 1  # Jei raidės nėra žodyje, sumažinamas likusių spėjimų skaičius.
                print('Tokios raidės žodyje nėra')

        elif vartotojo_raide in panaudotos_raides:
            print('Jūs jau bandėte šią raidę. Bandykite dar kartą!')

        else:
            print('Neteisingai pasirinktas simbolis.')

    # Žaidimo pabaigos scenarijai
    if spejimai == 0:
        print('Neatspėjote... Žodis buvo', zodis)
    else:
        print('Atspėjote žodį', zodis, '!!!')


def pagrindinis_meniu():
    """
    Pagrindinė funkcija, valdanti žaidimo ciklą.
    Kviečia žaidimo funkciją `spek()` ir klausia naudotojo, ar jis nori žaisti dar kartą.
    Jei ne, žaidimas baigiasi.
    """
    while True:
        spek()
        atsakymas = input('Ar norite žaisti dar kartą? (t): ')
        if atsakymas != 't':
            print('Ačiū, kad žaidėte! Iki pasimatymo!')
            break


# Paleidžiame žaidimą
pagrindinis_meniu()
