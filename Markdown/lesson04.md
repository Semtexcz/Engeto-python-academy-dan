# Python akademie

<br>

## Obsah lekce

---

1. [Iterační protokol](#Iterační-protokol),
2. [for loop](#for-loop),
3. [range](#Datový-typ-RANGE),
4. [enumerate](#Enumerate),
5. [zip](#Zip),
6. [domácí úkol](#Domácí-úkol).

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.yg9qTK4GbobmIc9KTC39pQHaFy%26pid%3DApi&f=1" width="300" style="margin-left:auto; margin-right:auto" />

## Iterační protokol a.k.a. cyklus

---

V některých situacích se můžeš setkat s **opakujícím se zápisem**:
```python

# Máš set..
domena = set()

# .. chceš procházet stringy s emaily..
email_1 = "m.vybiralova@firma.cz"
email_2 = "m.vybiralova@email.cz"
email_3 = "m.vybiralova@dobradomena.cz"
email_4 = "marie@vybiralova.cz"
email_5 = "marie.vybiralova@gmail.com"

# ..a do původního setu ukládat pouze jména domén.
domena = set(
    (
        email_1.split("@")[1].split(".")[0],
        email_2.split("@")[1].split(".")[0],
        email_3.split("@")[1].split(".")[0],
        email_4.split("@")[1].split(".")[0],
        email_5.split("@")[1].split(".")[0]
    )
)
```

Ten nutně nemusí znamenat **chybný** nebo **nelogický zápis**, ale pokud chceš provádět podobný postup 10x, 100x, 1000x, už může být nereálný na zapsání.
```python
emaily = list()

# pro každý email v listu emailu
# .. vyber email,
# .. označ pouze doménu,
# .. ulož ji do setu.

```

<br>

Pro periodické opakování ohlášení existují tzv. *iterační protokoly* (příp.  označovány jako smyčky, cykly, loopy).

Ty umožní zápis **zkrátit, automatizovat** a **současně udělat přehlednější**.

<br>

V rámci Pythonu se budeme bavit o **dvou základních typech smyček**:
1. smyčka `for`,
2. smyčka `while`.


<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.XOkl2fR4SKcajGnAi6KoZQHaDt%26pid%3DApi&f=1" width="400" style="margin-left:auto; margin-right:auto" />

## For loop <a class="anchor" id="for-loop"></a>

---

*For cyklus* je v jednoduchosti proces, který ti umožní projít tebou zadaný objekt **od prvního údaje** až **do posledního**.

<br>

### Obecně

---


```python
for pismeno in ['a', 'b', 'c']:
    print(pismeno)
```

1. `for` je **klíčkový výraz** v zahlaví (zápisu) cyklu,
2. `pismeno` je **proměnná vytvořená v cyklu**,jejíž obsah se v každém kroku cyklu přepíše,
3. `in` **klíčový výraz** ukazující zdroj objektů pro dočasnou proměnnou,
4. `"Matous"` je tzv. *iterovatelný objekt*, tedy proměnná, kterou můžeme procházet (třeba `str`, `list`, `set`, `dict`),
5. `:` řádek s předpisem musí být **zakončený dvojtečkou**,
6. `print(pismeno)` následují **odsazené instrukce**, které se budou opakovat v každém kroku.

### Co všechno můžeš iterovat

##### Sety


```python
for jmeno in {"Matouš", "Marek", "Lukáš"}:
    print(jmeno)
```

##### Tuple


```python
for jmeno in ("Matouš", "Marek", "Lukáš"):
    print(jmeno)
```

##### List


```python
for jmeno in ["Matouš", "Marek", "Lukáš"]:
    print(jmeno)
```

##### Dictionaries


```python
for klic, hodnota in {
    "jmeno": "Matous",
    "prijmeni": "Holinka",
    "email": "matous@holinka.com"
}.items():
    print(klic, hodnota, sep="=")
```

##### Integers / float / bool - NE!!!


```python
for x in 12345:
    print(x)
```


```python
for x in 1.2345:
    print(x)
```


```python
for x in True:
    print(x)
```

<br>

Obecný cyklus *for* se dá různě upravovat.

Jednou z možností a častých kombinací je doplnit cyklus **podmínkovým zápisem**.

<br>

### S proměnnou a podmínkou

---
Cyklus lze kombinovat s objekty, které jsou ti již dobře známé. Tedy *proměnné* a *podmínkové zápisy*:


```python
pismena = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
```


```python
for pismeno in pismena:
    if pismeno == "g":  # "a" --> False
        print("*Mam hodnotu ->*", pismeno)
    else:
        print("Nemam 'g', ale", pismeno)
```

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s `for` smyčkou a podmínkovým zápisem:

1. Procházej hodnoty pro zadaný `tuple` se jménem `cisla`,
2. .. pokud je hodnota **dělitelná třemi**, vypiš `"Fizz"`,
3. .. pokud je hodnota **dělitelná pěti**, vypiš `"Buzz"`,
4. .. pokud je hodnota **dělitelná třemi a současně pěti**, vypiš `"FizzBuzz"`,
5. .. pokud nebude platit ani jedna z předchozích podmínek, vypiš hodnotu samotnou.


```python
cisla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
cisla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)

for cislo in cisla:
    if cislo % 3 == 0 and cislo % 5 == 0:
        print("FizzBuzz")
    elif cislo % 3 == 0:
        print("Fizz")
    elif cislo % 5 == 0:
        print("Buzz")
    else:
        print(cislo)
```
</details>

<br>

### For/else

---

Jde o **speciální syntaxi**, kde na ohlášení smyčky doplníš větev `else`, která má svoje využití:


```python
pismena = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
```


```python
for pismeno in pismena:
    if pismeno == "x":
        print("*Mam hodnotu ->*", pismeno)
    else:
        print("Nemam 'x', ale", pismeno)

else:  # je možné napsat klasickou větev s "if"
    print("-" * 29, "Hledane pismeno neni v listu!", "-" * 29, sep="\n")
```

*poznámka*. Pomocný `else` se přidává k cyklu `for`, pokud chceme nějaký proces provést **až po úspěšném skončení celého cyklu**.

<br>

### For loop s doplňujícím ohlášením

---

Cykly můžeš doplnit **ohlášeními**, obzvlášť pokud potřebujeme **přeskočit**/**pokračovat** v  průběhu cyklu.

<br>

| Ohlášení | Použití |
|:-:|:-|
|`break` | **přeskočí** zbytek smyčky (vč. else větve) a pokračuje kódem pod ní |
|`continue` | 	**vrací se** k definici smyčky |
|`pass` | 	tzv. *placeholder*, zabrání potenciální výjimce |

<br>

### Ohlášení BREAK

#### Obyčejný for loop

---


```python
for pismeno in "Matous":
    print(pismeno)
```

<br>

#### For loop a ohlášení break

---


```python
for pismeno in "Matous":
    print(pismeno)
    break
```

<br>

#### For/else bez ohlášení break

---


```python
for pismeno in "Matous":
    print(pismeno)
else:
    print("-" * 29, "Konec smycky!", "-" * 29, sep="\n")
```

<br>

#### For/else s ohlášením break

---


```python
for pismeno in "Matous":
    print(pismeno)
    break
else:
    print("-" * 29, "Konec smycky!", "-" * 29, sep="\n")
```

<br>

#### For loop s ohlášením break bez else

---


```python
for pismeno in "Matous":
    print(pismeno)
    break

print("-" * 29, "Konec smycky!", "-" * 29, sep="\n")
```

<br>

#### For/else s ohlášením break a doplňujícím ohlášením pod cyklem

---


```python
pismena = ["a", "b", "c", "d", "e", "f", "g", "h"]
```


```python
for pismeno in pismena:
    if pismeno == "e":
        print("Mam hodnotu ->", pismeno)
        break
    else:
        print("Nemam 'e', ale", pismeno)

print("Pokracuji s interpretaci naseho zapisu ^.^")
```

<br>

### Ohlášení CONTINUE

#### Obyčejný for loop

---


```python
for pismeno in "Matous":
    print(pismeno)
```

<br>

#### For loop a ohlášení continue

---


```python
for pismeno in "Matous":
    print(pismeno)
    continue
```

<br>

#### For/else a ohlášení continue

---


```python
for pismeno in "Matous":
    print(pismeno)
    continue

else:
    print("-" * 29, "Konec smycky!", "-" * 29, sep="\n")
```

<br>

#### For loop, podmínka a ohlášení continue

---


```python
pismena = ["a", "b", "c", "d", "e", "f", "g", "h"]
```


```python
for pismeno in pismena:
    if pismeno in {"a", "b", "c", "d"}:
        continue

    print("Hodnota je dulezita:", pismeno)
```

<br>

### Ohlášení PASS

Doplňující ohlášení, které slouží jako `placeholder` pro zápis, který ještě není kompletní a současně nezpůsobí výjimku.

<br>

#### For loop, bez ohlášení pass

---


```python
for pismeno in "Matous":
    # budu iterovat skrze promennou: str
```

<br>

#### For loop, s ohlášením pass

---


```python
for pismeno in "Matous":
    # budu iterovat skrze promennou: str
    pass
```

<br>


#### For loop, doplněná budoucí ohlášení

---


```python
for pismeno in "Matous":
    print(pismeno)
#     pass
```

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s nestovanou smyčkou:

1. Procházej hodnoty pro zadaný dvoudimenzionální `list` se jménem `obsah`,
2. .. nejprve procházej **samotné řádky**,
3. .. následně procházej **buňku po buňce** - vyprintuj hodnoty.


```python
obsah = [
    ['jmeno;prijmeni;email;projekt'],
    ['Matous;Holinka;m.holinka@firma.cz;hr'],
    ['Petr;Svetr;p.svetr@firma.cz;devops']
]
```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
obsah = [
    ['jmeno;prijmeni;email;projekt'],
    ['Matous;Holinka;m.holinka@firma.cz;hr'],
    ['Petr;Svetr;p.svetr@firma.cz;devops']
]

for radek in obsah:
    print(radek)

    for bunka in radek[0].split(";"):
        print(bunka)
```
</details>

<br>


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.fNwmtWM7vEaO1gxjCKwMOwHaHa%26pid%3DApi&f=1" width="300" style="margin-left:auto; margin-right:auto" />

## Datový typ RANGE

---


Jde o *built-in* funkci, která nám vytvoří datový typ `range`. Tento typ v podstatě odpovídá tomu, co si představíme pod slovem **interval** nebo **rozsah**:


```python
print(range(11))
```


```python
print(type(range(11)))
```


```python
for cislo in range(0, 11):
    print(cislo)
```

### Vytvoření RANGE

---

| Počet argumentů |	Význam |
|:-:|:-|
| **1** | 	Hodnota stop. Začíná defaultně od 0 (končí o jednu hodnotu dříve než stop)
| **2** | 	Hodnoty start a stop |
| **3** | 	Hodnoty start, stop a step (tedy krok) |


```python
print(range(11))  # 0, 10
```


```python
print(tuple(range(11)))
```


```python
print(tuple(range(5, 11)))
```


```python
print(tuple(range(0, 11, 2)))
```


```python
print(tuple(range(0, 10, -1)))
```


```python
print(tuple(range(10, 0, -1)))
```

*poznámka*. datový typ `range` pracuje pouze **s celými čísly**.


```python
for cislo in range(1, 11):
    print("www.oukro.cz/aukce&page=", cislo, sep="")
```


```python
import time

for _ in range(6):
    print(f"Kontroluji obsah souboru..")

    time.sleep(1)
# print(f"Soubor zkontrolován!")
```

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.xszhziZWTRmKLG00uoNozAHaHM%26pid%3DApi&f=1" width="200" style="margin-left:auto; margin-right:auto" />


## Enumerate

---

Jde opět o  **built-in funkci** a současně datový typ, která nám **vytvoří číslování** pro zadaný *iterovatelný* objekt.


```python
print(["Python", "Java", "JavaScript", "C", "Rust"])
```


```python
print(enumerate(["Python", "Java", "JavaScript", "C", "Rust"]))
```


```python
print(tuple(enumerate(["Python", "Java", "JavaScript", "C", "Rust"])))
```


```python
print(type(enumerate(["Python", "Java", "JavaScript", "C", "Rust"])))
```

### For loop s enumerate

---


```python
for jazyk in ["Python", "Java", "JavaScript", "C", "Rust"]:
    print(jazyk)
```


```python
for jazyk in enumerate(["Python", "Java", "JavaScript", "C", "Rust"]):
    print(jazyk)
```


```python
for jazyk in enumerate(["Python", "Java", "JavaScript", "C", "Rust"]):
    print(jazyk[1])
```


```python
for index, jazyk in enumerate(["Python", "Java", "JavaScript", "C", "Rust"]):
    if index >= 2:
        print(jazyk)
```

<br>


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.QTQy3KN6A9Ih7btyIsF-_gHaGq%26pid%3DApi&f=1" width="200" style="margin-left:auto; margin-right:auto" />

## Zip

---

Tato funkce ti umožní *iterovat* skrze několik *iterovatelných objektů* **současně**:


```python
jmena    = ("Petr", "Marek", "David", "Adam")
prijmeni = ("Svetr", "Pavel", "Dvořák")
```

<br>

Funkce *zip* vrací *tuple*, který obsahuje hodnoty **o stejném indexu** z obou (nebo více) objektů.


```python
print(zip(jmena, prijmeni))        # lazy evaluation: tuple, list
```


```python
print(jmena, prijmeni, sep='\n')
```


```python
print(list(zip(jmena, prijmeni)))
```


```python
for cele_jmeno in zip(jmena, prijmeni):
    print(cele_jmeno)
```


```python
for jmeno, prijmeni in zip(jmena, prijmeni):
    print(jmeno, prijmeni.upper())
```

<br>

Pokud se hodnoty z jednoho z *iterovatelných* objektů vyčerpají, **přeskočí** zbytek hodnot:


```python
for jmeno, prijmeni, vek in zip(
    ("Petr", "Marek"), 
    ("Svetr", "Pavel", "Dvořák"), 
    (22, 32, 42)):  # 2 jména, 3 příjmení
    print(jmeno, prijmeni, vek)
```

➡️ ➡️ **Formulář pro Tvoje hodnocení** [**čtvrté lekce**](https://forms.gle/6N7RTwyuRiT7Co638) ⬅️ ⬅️

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.O9EkosTHP3lmEAvzA3D-2QHaHa%26pid%3DApi&f=1" width="400" style="margin-left:auto; margin-right:auto" />



## Domácí úkol

---

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s `for` smyčkou:

Z výše zadaných jmen vytvoř slovník, kde budou klíče celá jména a hodnoty budou nestované slovníky, obsahující klíče křestní jméno, příjmení a email. Viz. ukázka:


```python
zamestnanci_raw = """
Helena Vybíralová
Wendy Štrumlová
Marie Vybíralová
Stanislav Bechyňka
Zdeňka Urbánková
Lukáš Riečan
Veronika Koudelová
Františka Vorlová
Ilie Seleš
Martin Železný
Petra Niklesová
Bohumil Skok
Jakub Šmíd
Jarmila Procházková
Dagmar Hlavatá
Jiří Nguyen Thanh
Marie Franková
Dana Ulrichová
Jana Hranická
Hana Budošová
Ivan Široký
Květoslava Jiráčková
Pavel Przywara
Josef Umlauf
Tomáš Granzer
Miroslav Kuba
Miloslava Adámková
Marie Karlíková
Jaroslav Hronský
Vlasta Karlíková
Andrea Žatková
Zuzana Lokočová
Ondřej Ptáček
Zdeněk Najman
Tereza Šebešová
Antonie Skokánková
Jan Lion
Václav Vecko
František Vajgl
Adéla Kavková
Amália Vacková
Anna Pažická
Ivo Pustějovský
Antonín Pavela
Jitka Adamová
Libuše Hamroziová
Drahomíra Balzerová
Marek Suchánek
Petr Vavrinec
Jonáš Stuchlý
Jaromír Pecen
Markéta Kyliánková
Marina Pečenková
Ivana Perdochová
Michaela Drápalová
Michael Mentlík
Rudolf Špičák
Žaneta Holá
Blanka Lišková
Eva Svatoňová
Rostislav Hoang
Martina Kalivodová
Milan Hruška
Zdenka Marková
Lenka Schambergerová
Růžena Martinů
Věra Řezanková
Marie Pečenková
Miloš Váchal
Jaroslava Hrubá
Petr Pecen
Pavla Konvicová
Lucie Marešová
Květuše Zdráhalová
Vlastimila Svatošová
Zora Michalčíková
Daniel Švejnoha
Klára Brunclíková
Vladimír Bauer
Michal Slaný
Jiřina Novosadová
Karel Sršeň
Stanislava Lakosilová
Filip Černý
Alena Kubiková
Sára Kotrlová
Alois Rejlek
Božena Novotná
Maryana Nováková
Kateřina Máslová
Ladislav Dvořák
Radek Varga
Petr Dvořák
Ludmila Jaklová
Renáta Foubíková
Nikola Lehká
Dominika Riegerová
Patrik Polák
Soňa Štrbová
David Matoušek
Liubov Hollíková
Monika Poláková
Marie Jaklová
Aleš Svoboda
Roman Kolínský
Karolína Košiková
"""
```

```
{'Adéla Kavková': {'email': 'a.kavková@firma.cz',
                   'krestni_jmeno': 'Adéla',
                   'prijmeni': 'Kavková'},
 'Alena Kubiková': {'email': 'a.kubiková@firma.cz',
                    'krestni_jmeno': 'Alena',
                    'prijmeni': 'Kubiková'},
 'Aleš Svoboda': {'email': 'a.svoboda@firma.cz',
                  'krestni_jmeno': 'Aleš',
                  'prijmeni': 'Svoboda'},
 ...
}
```


```python

```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
zamestnanci = dict()

for cele_jmeno in zamestnanci_raw.splitlines():
    if cele_jmeno:
        zamestnanci[cele_jmeno] = {
            "krestni_jmeno": (kr_jmeno := cele_jmeno.split()[0]),
            "prijmeni": (prijmeni := cele_jmeno.split()[1]),
            "email": kr_jmeno.lower()[0] + "." + prijmeni.lower() + "@firma.cz",
#             "email": f"{kr_jmeno.lower()[0]}.{prijmeni.lower()}@firma.cz"
        }
```
</details>

---
