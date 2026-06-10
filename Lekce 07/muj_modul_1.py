# soubor muj_modul.py
def hlavni_funkce():
    funkce_1()
    funkce_2()
    funkce_3()

def funkce_1():
    print("Spouštění první funkce..")

def funkce_2():
    """Funkce, kterou potřebuješ."""
    print("Spouštění druhé funkce..")

def funkce_3():
    print("Spouštění třetí funkce..")

print(__name__)
if __name__ == "__main__":
    hlavni_funkce()
