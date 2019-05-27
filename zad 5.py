class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek

    def przedstaw_sie(self):
        print(f"Jestem {self.imie} {self.nazwisko}. Mam {self.wiek} lat.")

    def urodziny(self):
        wiek_przed = self.wiek
        self.wiek += 1
        return wiek_przed


def main():

    Jan = Osoba("Jan", "Nowak", 48)
    Adam = Osoba("Adam", "Mickiewicz", 220)


    Jan.przedstaw_sie()
    Adam.przedstaw_sie()

    wiek_Adama_przed = Adam.urodziny()
    Adam.przedstaw_sie()
    print(f"Wiek Adama sprzed urodzin: {wiek_Adama_przed}")


    Jan.imie = "Stanisław"
    Jan.nazwisko = "Witkiewicz"
    Jan.wiek = 133

    Jan.przedstaw_sie()


if __name__ == "__main__":
    main()