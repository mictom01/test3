import random
random.seed()
print('Wymyslilem sobie pewna liczbe od 1 do 100, zgadnij jaka :)')
czyniezgadl = True
odp = True
liczba  = random.randint(1,100)
while czyniezgadl:
    sam = input()
    sam = int(sam)
    if sam == liczba:
        print('Brawo, zgadles moja liczbe!')
    if sam<liczba:
        print('Moja liczba jest wieksza')
    if sam>liczba:
        print('Moja liczba jest mniejsza')
    if sam == liczba:
        odp = input("Chcesz zakonczyc program czy grac dalej? Jezeli chcesz grac dalej napisz TAK, jezeli nie chcesz napisz NIE")
    if odp==("nie") or odp== ("NIE") or odp== ("Nie"):
            print ("Koniec programu!" )
            break
    if odp == ("Tak") or odp == ("tak") or odp == ("TAK"):
            print ("To gramy dalej!")