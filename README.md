# Generovaná osnova


## Python, obecný úvod

1. **Instalace a spuštění Pythonu**:
   - Instalace Pythonu 3.8+.
   - Spuštění Pythonu v terminálu (kontrola verze, interaktivní interpret).

2. **Pracovní prostředí**:
   - Interpret Pythonu.
   - Editor Pythonu.
   - IDE (Visual Studio Code, PyCharm aj.).
   - Jupyter Notebook.

3. **Základy syntaxe a datové typy**:
   - Výpis na obrazovku pomocí `print()`.
   - Základní operace s čísly (`int`, `float`).
   - Běžné a méně známé aritmetické operace (`+`, `-`, `*`, `/`, `//`, `%`, `**`).

4. **Práce s desetinnými čísly (float)**:
   - Problém s přesností typu `float`.
   - Použití modulu `decimal` pro přesnější operace.

5. **Textové hodnoty (řetězce, `str`)**:
   - Tvorba řetězců pomocí uvozovek (`'...'`, `"..."`, `'''...'''`, `"""..."""`).
   - Escape sekvence (`\'`, `\\`, `\n`, `\t` aj.).
   - Konkatenace řetězců (`+`), opakování (`*`).
   - Indexování, slicing, striding (`[...]`, `[::]`).

6. **Změna datového typu (`type()`, `int()`, `float()`, `str()`)**:
   - Převod mezi řetězci, čísly a dalšími datovými typy.

7. **Práce s proměnnými**:
   - Pojmenování proměnných (pravidla pro názvy, použití `_` a čísel).
   - Přidělování hodnot proměnným (`=`).

8. **Sekvenční datové typy**:
   - Seznamy (`list`) a jejich vlastnosti.
   - N-tice (`tuple`) a jejich vlastnosti.
   - Spojování, opakování, indexování, slicing a striding pro `list` a `tuple`.

9. **Zabudované funkce (built-in functions)**:
   - `type()`, `print()`, `input()`, `help()`, `list()`, `tuple()`.

10. **Jednoduché funkce a interakce s uživatelem**:
   - Použití `input()` pro zadávání vstupů od uživatele.
   - Výpis výsledků pomocí `print()`.
---


## Podmínky a metody

1. **Rozhodování v Pythonu**:
   - Použití `if`, `elif`, `else`.
   - Základní rozhodovací logika pomocí porovnávání hodnot.

2. **Datový typ `bool` (boolean)**:
   - Dvě možné hodnoty: `True` a `False`.
   - Vytváření proměnných s typem `bool`.
   - Použití funkce `bool()` pro testování pravdivosti výrazu.

3. **Funkce `bool()` a jiné datové typy**:
   - Pochopení, co je pravdivé (`True`) a nepravdivé (`False`).
   - Použití `bool()` s hodnotami jako `0`, `1`, prázdný řetězec, seznam, n-tice a `None`.

4. **Srovnávací operace (`<`, `>`, `<=`, `>=`, `==`, `!=`)**:
   - Porovnávání číselných hodnot a řetězců.

5. **Boolean operace (`and`, `or`, `not`)**:
   - Kombinování více logických výroků.
   - Krátké vyhodnocování (`and` přestává testovat, když narazí na `False`, `or` na `True`).

6. **Srovnání identit objektů (`is`, `is not`)**:
   - Porovnávání paměťových identifikátorů objektů.
   - Rozdíl mezi `is` a `==`.

7. **Membership testing (`in`, `not in`)**:
   - Ověření, zda je hodnota součástí sekvence (řetězce, seznamu, n-tice).

8. **Jednoduchý podmínkový zápis (`if`, `else`)**:
   - Odsazení kódu, který se vykoná při splnění podmínky.
   - Použití klíčových slov `if` a `else`.

9. **Rozvinutý podmínkový zápis (`if`, `elif`, `else`)**:
   - Vytváření složitějších rozhodovacích stromů.
   - Kombinace více podmínek pomocí `and` a `or`.

10. **Ternární operátor**:
    - Kratší zápis podmíněného přiřazení proměnné.
    - `x = <hodnota1> if <podmínka> else <hodnota2>`.

11. **Metody pro `str` (řetězce)**:
    - Např. `.isnumeric()`, `.upper()`, `.lower()`, `.title()`.
    - Získání části řetězce pomocí `.split()`.

12. **Metody pro `list` (seznamy)**:
    - `.append()`, `.insert()`, `.split()` (pokud jde o seznamy vytvořené z řetězců).
    - Vkládání a přidávání položek do seznamu.
---


## Slovníky a množiny

1. **Datový typ `dict` (slovník)**:
   - Vytváření slovníků (`{key: value}`).
   - Přístup k hodnotám pomocí klíče (`dict[key]`).
   - Vytváření slovníků pomocí `dict()` nebo `{}`.
   - Přidávání a modifikace klíčů a hodnot (`dict[key] = value`).
   - Vnořené slovníky (slovníky obsahující jiné slovníky).
   - Metody pro práci se slovníky (`get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `clear()`, `copy()`, `setdefault()`, `fromkeys()`).
   - Mělká vs. hluboká kopie slovníku.
   - Testování existence klíče (`in`).

2. **Datový typ `set` (množina)**:
   - Vytváření množin (`{value1, value2}` nebo `set()`).
   - Přidávání a odebírání prvků (`add()`, `remove()`, `discard()`, `pop()`).
   - Množinové operace: sjednocení (`|`), průnik (`&`), rozdíl (`-`), symetrický rozdíl (`^`).
   - Metody množin (`union()`, `intersection()`, `difference()`, `symmetric_difference()`, `issubset()`, `issuperset()`, `isdisjoint()`).
   - Kopírování množin (`copy()`).
   - Testování existence prvků v množině (`in`).

3. **Datový typ `frozenset` (neměnitelná množina)**:
   - Vytváření `frozenset()`.
   - Vlastnosti `frozenset` (neměnitelnost).
   - Použití množinových operací s `frozenset`.

4. **Volitelné argumenty v zabudovaných funkcích**:
   - Použití volitelných argumentů v `print()`, `dict.get()`, atd.
   - Princip práce s volitelnými argumenty v různých funkcích.

5. **Praktické použití slovníků a množin**:
   - Vytváření aplikací na základě slovníků a množin (např. filmový slovník).
   - Manipulace s daty pomocí metod a operátorů.
   - Testování existence klíčů a hodnot.
---


## For cyklus

1. **Iterační protokol (smyčky / cykly)**:
   - Rozumět principu iteračních protokolů (`for` a `while` smyčky).
   - Rozlišit mezi `for` a `while` smyčkami a vědět, kdy který použít.
   - Kombinace smyček s podmínkami.

2. **For loop (`for` smyčka)**:
   - Procházení různých iterovatelných objektů (`list`, `tuple`, `set`, `dict`).
   - Použití `for` smyčky s různými datovými typy (kromě `int`, `float`, `bool`).
   - Kombinace `for` smyčky s podmínkami (`if`).
   - Použití `for/else` pro detekci ukončení smyčky.
   - Použití `break`, `continue`, a `pass` v `for` smyčkách.
   - Použití `for` smyčky pro procházení dvourozměrných seznamů (matice).

3. **Datový typ `range`**:
   - Vytváření sekvencí pomocí `range()`.
   - Použití `range()` s jedním, dvěma a třemi argumenty (start, stop, step).
   - Použití `range()` v `for` smyčkách.
   - Změna `range()` na seznam pomocí `list()`.

4. **Enumerate (číslování)**:
   - Použití `enumerate()` pro získání indexů spolu s hodnotami.
   - Práce s výsledky `enumerate()` při iteraci.
   - Použití indexů v kombinaci s podmínkami.

5. **Zip (spojování iterovatelných objektů)**:
   - Použití `zip()` pro současné procházení více iterovatelných objektů.
   - Převod výsledků `zip()` na seznam nebo slovník.
   - Použití `zip()` s `for` smyčkami.

6. **Použití smyček pro zpracování textových dat**:
   - Vytváření slovníků na základě zpracovaného textu.
   - Automatické generování e-mailů nebo jiných hodnot pomocí `for` smyček.

---


## While cyklus

1. **While smyčka**:
   - Použití `while` smyčky pro iteraci dokud je podmínka `True`.
   - Kombinace `while` s `if` a dalšími podmínkami.
   - Použití `break`, `continue`, a `pass` v `while` smyčkách.
   - Použití `while/else` pro detekci ukončení smyčky.

2. **Nekonečná smyčka (`while True`)**:
   - Použití `while True` pro řízené a neřízené nekonečné smyčky.
   - Použití `break` pro ukončení nekonečné smyčky.
   - Zabezpečení smyčky před nekonečným během.

3. **Walrus operátor (`:=`)**:
   - Vytváření a současné použití proměnných pomocí `:=`.
   - Použití `walrus` operátoru s `while` smyčkami a podmínkami.
   - Výhody `walrus` operátoru při zjednodušování zápisu kódu.

4. **Zkrácené přiřazování (Augmented assignment)**:
   - Použití zkrácených operátorů (`+=`, `-=`, `*=`, `/=`, `**=`) pro úpravu proměnných.
   - Výhody zkráceného přiřazování pro mutable objekty (např. seznamy).

5. **Comprehensions (generátory)**:
   - **List comprehensions** pro generování seznamů.
   - **Dict comprehensions** pro generování slovníků.
   - **Set comprehensions** pro generování množin.
   - Využití *comprehensions* v kombinaci s podmínkami a cykly.
   - Vnořené *comprehensions* a jejich čitelnost.

6. **Praktické použití while smyček a comprehensions**:
   - Vytváření jednoduchých textových her nebo interaktivních úloh.
   - Použití comprehensions k filtrování a zpracování dat.
---


## Knihovny

1. **Obecně ke knihovnám**:
   - Co je to knihovna v Pythonu (soubory `.py` obsahující opakovaně použitelný kód).
   - Dělení knihoven na **moduly** (jednotlivé `.py` soubory) a **balíčky** (složky obsahující více modulů).

2. **Proč používat knihovny**:
   - Opakované využití kódu.
   - Snížení množství psaného kódu.
   - Možnost využívat práci jiných programátorů.

3. **Nahrávání knihoven (importování)**:
   - `import <knihovna>` (standardní způsob).
   - `from <knihovna> import *` (nahrává všechny objekty z knihovny, nebezpečné kvůli možným konfliktům názvů).
   - `from <knihovna> import <objekt>` (nahrání pouze konkrétního objektu, např. funkce nebo proměnné).
   - `from <knihovna> import <objekt> as <alias>` (přidělení aliasu pro objekt).
   - `import <knihovna> as <alias>` (přidělení aliasu pro knihovnu).

4. **Použití knihoven v Pythonu**:
   - Příklady použití vestavěných knihoven: `random`, `os`, `sys`, `collections`.
   - Metody `dir()` a `help()` pro zjišťování obsahu knihoven a jejich dokumentace.

5. **Moduly**:
   - Co je to modul (`.py` soubor).
   - Importování vlastních modulů.
   - Rozdíl mezi moduly a balíčky.

6. **Vlastní moduly**:
   - Jak vytvořit a importovat vlastní modul.
   - Použití `help()` k dokumentaci modulů.

7. **Balíčky**:
   - Co je to balíček (složka obsahující více `.py` souborů).
   - Speciální soubory v balíčku: `__init__.py`, `__pycache__`.
   - Jak vytvořit a importovat vlastní balíček.

8. **Knihovny třetích stran**:
   - Rozdíl mezi standardními a externími knihovnami.
   - Použití `pip` pro instalaci balíčků.
   - Virtuální prostředí (`venv`) a jeho používání.
   - Jak vytvořit `requirements.txt` pro správu závislostí.

9. **Praktické cvičení s knihovnami a moduly**:
   - Práce s externími knihovnami (např. `statistics`, `random`).
   - Vytvoření a import vlastních modulů.
   - Tvorba vlastního balíčku s více moduly.
---


## Uživatelské funkce

1. **Funkce v Pythonu**:
   - Rozdíl mezi **zabudovanými funkcemi** a **uživatelskými funkcemi**.
   - Jak definovat a spustit uživatelskou funkci (`def <nazev_funkce>(parametry):`).

2. **Zabudované funkce (built-in functions)**:
   - Použití funkcí jako `print()`, `len()`, `type()`, `int()`, `str()`, `float()`, `input()`, `abs()`, `round()`, `max()`, `min()`, `sum()`, `sorted()`, `list()`, `dict()`, `set()`, `tuple()`, `bool()`, `isinstance()`, `all()`, `any()`, `map()`, `filter()`, `zip()`, `enumerate()`, `open()`, `reversed()`.
   - Volitelné argumenty (`sep`, `start`).

3. **Uživatelské funkce (user-defined functions)**:
   - Syntaxe pro vytvoření uživatelské funkce.
   - Parametry a argumenty.
   - Použití `return` pro vrácení hodnoty.
   - Význam dokumentace funkcí pomocí *docstring*.
   - Použití `help()` pro získání nápovědy o uživatelské funkci.

4. **Volitelné argumenty a pojmenované argumenty**:
   - Argumenty s přednastavenými hodnotami.
   - Pojmenované argumenty při volání funkcí.

5. **Modulární kód a `__name__ == "__main__"`**:
   - Jak spouštět moduly jako skripty nebo je importovat jako knihovny.

6. **Vícenásobné přiřazení hodnot**:
   - Přiřazování více proměnných najednou.
   - Použití hvězdičky (`*`) pro sbalení hodnot do jednoho objektu.

7. **Správná struktura funkcí**:
   - Vhodné pojmenování funkcí (slovesa).
   - Použití modulů a oddělených funkcí.
   - Správný počet parametrů.
   - Dodržování principu, že funkce má vykonávat jednu konkrétní činnost.

---


## Pokročilá práce s funkcemi

1. **Vstupy uživatelských funkcí**:
   - Rozdíl mezi **parametry** a **argumenty**.
   - Různé vzory vstupů:
     - **Poziční parametry**.
     - **Klíčové argumenty**.
     - **Defaultní parametry**.
     - **Position-only parametry**.
     - **\*args** (sbalení argumentů do n-tice).
     - **\*\*kwargs** (sbalení pojmenovaných argumentů do slovníku).

2. **Funkční rámce (Scope)**:
   - **Globální rámec**.
   - **Lokální rámec**.
   - **Uzavírající rámec** (enclosing scope).
   - **Zabudovaný rámec** (built-in scope).
   - Pravidla pro vyhledávání proměnných (LEGB - Local, Enclosing, Global, Built-in).

3. **Funkce jako objekt**:
   - Funkce jako argumenty.
   - Funkce vracející funkce.
   - Funkce jako objekt s možností přiřazení a předávání.

4. **Rekurze**:
   - Rekurzivní zápis funkcí.
   - Porovnání rekurzivního a nerekurzivního řešení.
   - Použití rekurze pro práci se **stromovými datovými strukturami**.

5. **Praktické příklady**:
   - Vytváření funkcí se sbalenými vstupy `*args` a `**kwargs`.
   - Tvorba dekorátorů (použití uzavírajícího rámce).
   - Zjednodušování datových struktur pomocí rekurze.
---


### Práce s textovými soubory

1. **Základní principy I/O**:
   - Rozdíl mezi RAM a diskem.
   - Význam souborů jako persistentního úložiště.

2. **Struktura a typy souborů**:
   - Header, data, EOF.
   - Binární reprezentace souboru.
   - Textové vs. binární soubory.

3. **Cesty k souborům**:
   - Relativní vs. absolutní cesty.
   - Rozdíl v cestách mezi Linuxem a Windows.
   - Složení cesty: složka, název, přípona.
   - Stromová struktura systému.

4. **Otevírání a čtení souborů**:
   - `open('soubor.txt', mode='r', encoding='utf-8')`.
   - Metody `.read()`, `.readline()`, `.readlines()`.
   - Kurzor a metoda `.seek()`.
   - Ukončení spojení `.close()` nebo automaticky pomocí `with`.

5. **Zápis do souborů**:
   - `mode='w'` (přepis), `mode='a'` (append), `mode='r+'` (čtení + zápis).
   - Metody `.write()`, `.writelines()`.

6. **Kontextový manažer (`with open(...) as`)**:
   - Automatické zavření souboru.

7. **Práce s textovými a binárními soubory**:
   - `mode='rb'`, `mode='wb'`.
   - Rozdíl v reprezentaci: `b'string'`.

8. **Rozdíly v zakončení řádků (`\n`, `\r\n`)**:
   - Dopad při čtení souborů mezi OS.

9. **Kódování znaků**:
   - Rozdíl mezi ASCII a UTF-8.
   - Binární reprezentace znaků v UTF-8.

---

### 🗃️ Modul `pathlib` a `shutil`

10. **Manipulace se soubory a složkami**:
    - Vytváření složek: `.mkdir()`.
    - Mazání složek/souborů: `.rmdir()`, `.unlink()`.
    - Přesouvání a přejmenovávání: `.rename()`.
    - Kopírování: `shutil.copy()`.

11. **Vyhledávání souborů**:
    - `Path.glob()`, `Path.rglob()`.

12. **Získávání informací**:
    - `.exists()`, `.is_file()`, `.is_dir()`.
    - `.stat()` – velikost, datum úpravy.

13. **Práce s cestami**:
    - Spojování: `/`.
    - Absolutní cesty: `.resolve()`.
    - Rodičovské složky: `.parent`, `.parents`.
    - Rozdělení cesty: `.parts`, `.stem`, `.suffix`, `.with_suffix()`.

---

### 🧵 Formátování řetězců

14. **Tři způsoby formátování**:
    - `%`-formatting (nedoporučuje se).
    - `.format()` metoda.
    - f-stringy (`f"Ahoj {jmeno}"`).

15. **Funkce f-string**:
    - Vkládání výrazů, zarovnání, zaokrouhlování, formát čísel.
    - Přístup k datům (např. z dictu: `{data['name']}`).

---


## Výjimky a debuggování v Pythonu

1. **Traceback**:
   - Co je to **traceback** a jak ho číst (cesta k chybě, typ chyby, popis chyby).
   - Význam tracebacku pro identifikaci místa a příčiny chyby.

2. **Druhy chyb**:
   - **Syntaktické chyby** – chyby při psaní kódu.
   - **Běhové chyby** – chyby při spuštění programu (např. TypeError, NameError).
   - **Logické chyby** – kód se spustí, ale nefunguje správně.

3. **Běhové chyby a jejich druhy**:
   - `NameError`
   - `TypeError`
   - `ValueError`
   - `IndexError`
   - `KeyError`
   - `AttributeError`
   - `ZeroDivisionError`
   - `ImportError`
   - `FileNotFoundError`
   - `OverflowError`
   - `MemoryError`
   - `RecursionError`

4. **Odchytávání výjimek (try-except)**:
   - Použití `try-except` pro ošetření výjimek.
   - Použití `try-except-else-finally` pro komplexní odchytávání chyb.
   - Specifikace typu výjimky (`except TypeError:`).
   - Použití `except Exception as error` pro získání informací o chybě.

5. **Testování kódu a kontrola chyb**:
   - Použití knihovny `mypy` pro kontrolu typů.
   - Testování pomocí `pytest` – psaní testů, spouštění testů, využití dekorátorů `@pytest.mark.parametrize`.

6. **Debugování**:
   - Použití funkcí `print()`, `type()`, `dir()`, `vars()`, `locals()`, `globals()` při hledání chyb.
   - Debugování pomocí `pdb` (Python debugger).
   - Debugování v prostředí IDE (např. PyCharm).

7. **Logování chyb**:
   - Použití modulu `logging` pro záznam chyb a událostí.
   - Výhody logování oproti `print()`.
   - Záznamy do souborů, nastavení úrovní (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
   - Použití knihovny `loguru` pro uživatelsky přívětivé logování.

8. **Úprava a refaktoring kódu na základě chyb**:
   - Vylepšování kódu na základě výpisu tracebacku.
   - Přepis kódu tak, aby byl čitelnější a jednodušší na debugování.
---


## Formáty souborů

1. **Pathlib a Shutil**:
   - Vytváření složek (`Path.mkdir()`).
   - Přejmenování složek (`Path.rename()`).
   - Mazání složek (`Path.rmdir()`, `shutil.rmtree()`).
   - Kopírování a přesouvání souborů (`shutil.copy()`, `Path.rename()`).
   - Vyhledávání souborů (`Path.glob()`, `Path.rglob()`).

---

### 📁 Soubory CSV

2. **Práce se soubory CSV**:
   - Čtení CSV pomocí `csv.reader()`.
   - Zápis do CSV pomocí `csv.writer()`.
   - Čtení a zápis pomocí `DictReader` a `DictWriter`.
   - Nastavení delimitérů a dalších parametrů (např. `delimiter=','`, `quotechar='"'`).

---

### 📁 Soubory JSON

3. **Práce se soubory JSON**:
   - Čtení JSON pomocí `json.load()` a `json.loads()`.
   - Zápis do JSON pomocí `json.dump()` a `json.dumps()`.
   - Výhody JSON oproti CSV při práci s komplexními datovými strukturami.
   - Převod mezi Python slovníky a JSON objekty.

---

### 📁 Spouštění skriptu s argumenty

4. **Spouštění skriptů s argumenty**:
   - Použití `sys.argv` pro načítání argumentů z příkazové řádky.
   - Použití `argparse` pro strukturovanější načítání argumentů.
   - Vytváření uživatelských CLI nástrojů.

---

### 📁 Domácí úloha

5. **Praktická cvičení**:
   - Vytvoření skriptu, který načítá CSV soubory, zpracovává data a ukládá je ve formátu JSON.
   - Implementace argumentů příkazové řádky pro nastavení vstupního a výstupního souboru.

---

