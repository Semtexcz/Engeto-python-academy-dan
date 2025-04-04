
import argparse

# Vytvoření parseru
parser = argparse.ArgumentParser(
    description="Ukázka klíčových funkcí knihovny argparse."
)

# Povinný poziční argument
parser.add_argument(
    "soubor",                    # Název argumentu
    type=str,                    # Typ argumentu (řetězec)
    help="Cesta k vstupnímu souboru"  # Popis argumentu
)

# Volitelný argument s výchozí hodnotou
parser.add_argument(
    "--vystup",                  # Volitelný argument
    type=str,                    # Typ argumentu (řetězec)
    default="output.txt",        # Výchozí hodnota
    help="Cesta k výstupnímu souboru (výchozí: output.txt)"
)

# Argument s omezením na konkrétní hodnoty
parser.add_argument(
    "--format",
    choices=["text", "json", "csv"],  # Omezení na povolené hodnoty
    default="text",              # Výchozí hodnota
    help="Formát výstupu: text, json nebo csv (výchozí: text)"
)

# Přepínač (True, pokud je uveden)
parser.add_argument(
    "-v", "--verbose",
    action="store_true",         # Přepínač
    help="Zapne detailní výstup"
)

# Argument, který přijímá více hodnot
parser.add_argument(
    "--filtry",
    nargs="+",                   # Přijímá jednu nebo více hodnot
    type=str,                    # Typ každé hodnoty (řetězec)
    help="Seznam filtrů pro zpracování dat (např. filter1 filter2)"
)

# Číselný argument s výchozím rozsahem
parser.add_argument(
    "--iterace",
    type=int,                    # Typ argumentu (integer)
    default=1,                   # Výchozí hodnota
    help="Počet iterací zpracování (výchozí: 1)"
)

# Parsování argumentů
args = parser.parse_args()

# --- Použití argumentů ---
print(f"Vstupní soubor: {args.soubor}")
print(f"Výstupní soubor: {args.vystup}")
print(f"Formát výstupu: {args.format}")

if args.verbose:
    print("Detailní výstup je zapnut.")

if args.filtry:
    print(f"Aktivní filtry: {', '.join(args.filtry)}")
else:
    print("Žádné filtry nebyly zadány.")

print(f"Počet iterací: {args.iterace}")
