

import random
def main():
    print("zgadnij liczbe od 1 do 100.")
    randomNumber = random.randint(1,100)
    found=False
    while not found:
        userGuess = input("twoja liczba?:")
        if userGuess == randomNumber:
            print ("wygrales")
            found = True
        elif userGuess > randomNumber:
             print("mniejsza")
        else:
                print ("wieksza")

    print ("dzieki za gre")
if __name__=="__main__":
    main()