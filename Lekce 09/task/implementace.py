import os  # Importuje modul os pro práci se souborovými cestami a adresáři
from vzor import PREVOD  # Importuje slovník PREVOD z modulu vzor pro převod hodnot

def najdi_vsechny_txt(cesta_in: str) -> list:
    # Funkce najde všechny soubory s příponou .txt v zadaném adresáři
    cesty = [
        os.path.join(cesta_in, soubor) for soubor
        in os.listdir(cesta_in)  # Projde všechny soubory v zadaném adresáři
        if soubor.endswith(".txt")  # Zkontroluje, zda soubor končí na .txt
    ] 
    return cesty  # Vrátí seznam cest k nalezeným .txt souborům

def nacitani_txt(cesta: str) -> list:
    # Funkce načte obsah textového souboru a vrátí ho jako seznam řádků
    with open(cesta, mode="r", encoding="utf-8") as f:  # Otevře soubor v režimu pro čtení s kódováním UTF-8
        obsah = f.readlines()  # Načte všechny řádky ze souboru do seznamu
    print("Zpracovavam soubor", cesta)  # Vypíše název zpracovávaného souboru
    return obsah  # Vrátí seznam řádků

def zformatuj_data(obsah: list) -> list:
    # Funkce formátuje data na základě slovníku PREVOD
    zformatovany_obsah = []  # Inicializuje prázdný seznam pro formátovaný obsah
    for radek in obsah:  # Projde každý řádek v obsahu
        radek_list = radek.split(",")  # Rozdělí řádek podle čárek do seznamu hodnot
        radek_list[0] = PREVOD.get(radek_list[0])  # Převede první položku na hodnotu ze slovníku PREVOD
        if radek_list[0] is not None:  # Zkontroluje, zda byla položka úspěšně převedena
            zformatovany_obsah.append(",".join(radek_list))  # Spojí hodnoty zpět do řetězce a přidá do seznamu
        else:
            print('Upozorneni: neda se udelat prevod!')  # Upozorní, pokud nelze provést převod
    return zformatovany_obsah  # Vrátí seznam formátovaných řádků

def uloz_vysledek(cesta_out: str, obsah: list) -> None:
    # Funkce uloží formátovaný obsah do nového souboru
    with open(cesta_out, mode="w", encoding="utf-8") as f:  # Otevře soubor pro zápis s kódováním UTF-8
        f.writelines(obsah)  # Zapíše seznam řádků do souboru
    print("Vysledek byl ulozen do souboru", cesta_out)  # Vypíše, že soubor byl uložen

def main(cesta_in="input", cesta_out="output"):
    # Hlavní funkce, která volá ostatní funkce a provádí celý proces
    cesty = najdi_vsechny_txt(cesta_in)  # Najde všechny .txt soubory v zadaném adresáři
    for (i, cesta) in enumerate(cesty):  # Projde každý nalezený soubor a jeho index
        obsah = nacitani_txt(cesta)  # Načte obsah souboru
        obsah = zformatuj_data(obsah)  # Zformátuje data na základě slovníku PREVOD
        soubor_out = os.path.join(cesta_out, f"output_{i}.txt")  # Vytvoří cestu pro výstupní soubor
        uloz_vysledek(soubor_out, obsah)  # Uloží formátovaný obsah do výstupního souboru

if __name__ == "__main__":
    main(cesta_in="input", cesta_out="output")  # Spustí hlavní funkci při přímém spuštění skriptu
