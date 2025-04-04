## Úvod

---

1. [Iterační protokol podruhé](#Iterační-protokol-podruhé),
2. [while smyčka](#While-smyčka),
3. [nekonečná smyčka](#Nekonečný-while-loop),
4. [operátor mrože?!](#Walrus-operátor),
5. [Zkrácené přiřazování](#Walrus-operátor),
6. [souhrn smyček](#Souhrn-úvodu-smyček),
7. [velmi použitelné prvky iterací](#Comprehensions),
8. [domácí úkol](#Domácí-úkol).

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.yg9qTK4GbobmIc9KTC39pQHaFy%26pid%3DApi&f=1" width="200" />

## Iterační protokol, podruhé

---

Pro periodické opakování ohlášení existují tzv. *iterační protokoly* (příp.  označovány jako *smyčky*, *cykly*, *loopy*).

Pomocí smyčky *for* umíš zapsat takovou *iteraci*, kdy postupně projdeš **všechny hodnoty**.

Co když budeš potřebovat *iterovat* bez zadané hodnoty, ale za jistých podmínek?

Až bude mít `list` 3 hodnoty, dokud uživatel zadává vstupy, atd.


<br>

Potom bude potřeba, povědět si ještě o druhém typu smyček:
1. smyčka `for`,
2. smyčka `while`.

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.Oir5eME7J-RWJpxHkJjr-QHaGe%26pid%3DApi&f=1" width="200" />



## While smyčka
---

Někdy ale není nutné *iterovat* přes **celý objekt**, jak tomu bylo u smyčky `for`.

Naopak, budeš potřebovat provádět proces *iterování* tak dlouho, *dokud* to bude nutné.

Za takovým účelem můžeš využít druhý typ smyček, `while`.

### Obecně while loop


```python
index = 1

while index < 6:
    print("Ještě nemáš 6, ale ", index, ", pokračuji..", sep="")
    index = index + 1

print("Hotovo, máš 6!")
```

    Ještě nemáš 6, ale 1, pokračuji..
    Ještě nemáš 6, ale 2, pokračuji..
    Ještě nemáš 6, ale 3, pokračuji..
    Ještě nemáš 6, ale 4, pokračuji..
    Ještě nemáš 6, ale 5, pokračuji..
    Hotovo, máš 6!


1. `while` je **klíčkové slovo** v záhlaví,
2. `index < 6` je **podmínka**. Pokud je vyhodnocená jako `True`, proveď *odsazené ohlášení*,
3. `index < 6` ... `False`, ukonči smyčku a pokračuj **s neodsazeným zápisem** pod smyčkou,
4. `:` řádek s předpisem musí být **zakončený dvojtečkou**,
5. `print("Ještě nemáš...")`, následují *odsazené ohlášení*, které se budou opakovat v každém kroku,
6. `print("Hotovo, " ... )`, pokračuje *neodsazený zápis*, pod smyčkou.

### While s doplňující podmínkou

Cyklus `while` samotný podmínku obsahuje. Určitě je ale možnost, tento podmínkový strom ještě rozšířit:


```python
index = 0

while index <= 20:
    if len(str(index)) != 2:
        break
    else:
        print(index)
        index = index + 1
```

    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20



```python
index = 0

while index < 20 and len(str(index)) == 2:
    print(index)
    index = index + 1
```

Takové rozšíření může být obzvlášť přínosné, pokud podmínku v předpise nelze jednodušše rozšířit:


```python
index = 0
while index <= 20:
    if index == 10:
        index += 5  # modify the loop variable within the `if` block
    else:
        print(index)
        index += 1
```

    0
    1
    2
    3
    4
    5
    6
    7
    8
    9
    15
    16
    17
    18
    19
    20



```python
index = 0

while index <= 20:
    if index % 2 == 0:
        print(f"{index} je sudé")
    elif index % 5 == 0:
        print(f"{index} je dělitelné pěti")
    else:
        print(index)
    index += 1
```

    0 je sudé
    1
    2 je sudé
    3
    4 je sudé
    5 je dělitelné pěti
    6 je sudé
    7
    8 je sudé
    9
    10 je sudé
    11
    12 je sudé
    13
    14 je sudé
    15 je dělitelné pěti
    16 je sudé
    17
    18 je sudé
    19
    20 je sudé


### While/else

Cyklus `while` lze rozšířit o podmínkovou větev `else`(podobně jako *for loop*).

K ní se *interpret* dostane, pokud je podmínka v předpisu vyhodnocená jako `False`.

Současně nesmí narazit na ohlášení `break`:


```python
index = 0

while index < 20:
    if len(str(index)) != 2:
        index = index + 1

    else:
        print(index)
        index = index + 1

else:
    print("-" * 23, "Podmínka -> False".center(23), "-" * 23, sep="\n")

print(">Pokračuji pod smyčkou<")
```

    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    -----------------------
       Podmínka -> False   
    -----------------------
    >Pokračuji pod smyčkou<


Pokud doplníš ohlášení `break`, *interpret* přeskočí nejenom zbytek smyčky *while* ale také větev `else`:


```python
index = 0

while index < 20:
    if len(str(index)) != 2:  # pokud není číselná hodnota ze dvou znaků
        index = index + 1
        
    else:
        print(index)
        index = 1
        break
    
else:
    print("-" * 23, "Podminka -> False".center(23), "-" * 23, sep="\n")

print(">Pokračuji pod smyčkou<")
```

    10
    >Pokračuji pod smyčkou<


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Mq5UWTetElegP54AipJwxwAAAA%26pid%3DApi&f=1&ipt=d9ac04bc74246bbd95df83420771cf32edadc4aa0cde264c6c4a192b11c9c723&ipo=images" width="250" />

## Nekonečný while loop

---

Jednou z aplikací smyčky `while` je zápis tzv. *nekonečného cyklu*.

Obecně řečeno, že v případě **nekonečných smyček** můžeš potkat dva typy:
1. **řízené** nekonečné smyčky,
2. **neřízené** nekonečné smyčky.

### Neřízené nekonečné smyčky

Ty mohou nastat v důsledku **špatného zápisu** `while` cyklu:


```python
index = 1

while index < 20:
    print(index)
    # neinkrementuji hodnotu v proměnné 'index'
    # .. hodnota je v každém kroce 1 a smyčka nekončí.
    # .. Ctrl + C -> 
```

<br>

*poznámka*. výše ukázaná varianta představuje tzv. *nežádoucí nekonečnou smyčku*, kde vznikla chyba **v odsazené části zápisu**.

Chyba ovšem může nastat i při **špatném ohlášení** v zadání smyčky *while*:


```python
index = 1

while index > 0:  # vyhodnocené ohlášení má stále hodnotu `True`
    print(index)
    index = index + 1
```

*poznámka*. výše ukázaná varianta představuje tzv. *nežádoucí nekonečnou smyčku*, kde vznikla chyba **ve špatně zapsané podmínce**.

### Řízené nekonečné smyčky

Nekonečný cyklus s `while` je možné formulovat jako *řádnou/žádoucí nekonečnou smyčku*:


```python
while True:
    uziv_vstup = input("Zapiš libovolný text [nebo 'q' pro ukončení]: ")

    if uziv_vstup == "q":
        break
    print(uziv_vstup.capitalize())

print("Ukončuji ukázku!")
```

    Zapiš libovolný text [nebo 'q' pro ukončení]: ahoj
    Ahoj
    Zapiš libovolný text [nebo 'q' pro ukončení]: matouš
    Matouš
    Zapiš libovolný text [nebo 'q' pro ukončení]: 1
    1
    Zapiš libovolný text [nebo 'q' pro ukončení]: @
    @
    Zapiš libovolný text [nebo 'q' pro ukončení]: q
    Ukončuji ukázku!



```python
switch = True

while switch:
    uziv_vstup = input("Zapiš libovolný text [nebo 'q' pro ukončení]: ")

    if uziv_vstup == "q":
        switch = False
    print(uziv_vstup.capitalize())

print("Ukončuji ukázku!")
```

    Zapiš libovolný text [nebo 'q' pro ukončení]: ahoj
    Ahoj
    Zapiš libovolný text [nebo 'q' pro ukončení]: p
    P
    Zapiš libovolný text [nebo 'q' pro ukončení]: x
    X
    Zapiš libovolný text [nebo 'q' pro ukončení]: q
    Q
    Ukončuji ukázku!


#### Task 
Napište program, který bude 5krát žádat uživatele o zadání čísla. 
- Pokud je zadané číslo sudé, cyklus číslo přeskočí. 
- Pokud uživatel zadá číslo větší než 100, cyklus se předčasně ukončí. 
- Pokud cyklus proběhne bez přerušení, vypíše zprávu "done".

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.ZtuU0gV1oC0QdH6B74_D9QHaHa%26pid%3DApi&f=1" width="200" />



## Walrus operátor

---

*Přiřazovací operátor* nebo jinak *walrus operátor* je formulace, která je v Pythonu poměrně nová (3.8+).

Jde o zápis, který ti umožní **dva procesy**, při použití **jednoho operátoru**:
1. nejprve **hodnotu přiřadí** proměnné,
2. přímo ji použije.

### Vytvoření hodnoty a uložení


```python
jmeno = "Matous"
```


```python
print(jmeno)
```

    Matous



```python
print(jmeno := "Matous")
```

    Matous


V předchozí ukázce jde čistě **o vysvětlivku**.

**Proměnné** jinak nadále a přehledně zapis po jedné a pod sebe. :)

Praktické ukázky skutečného využití najdeš níže.

### Kombinace s podmínkou


```python
jmeno = input("Zapiš jméno: ".upper())

if jmeno == "Matouš":
    print("Toto je ", jmeno, sep="")
else:
    print("Tak ", jmeno, ", toho neznám.", sep="")
```

    ZAPIŠ JMÉNO: Marek
    Tak Marek, toho neznám.


Obzvlášť v kombinaci se **zabudovanými funkce** a *uživatelskými funkcemi* je nápomocný.

Zásadní je **doplnění kulatých závorek**, kterými *interpretu* zdůrazníš pořadí:


```python
TEXT = "Zapiš jméno: ".upper()

if (jmeno := input(TEXT)) == "Matouš":
    print("Toto je ", jmeno, sep="")
else:
    print("Tak ", jmeno, ", toho neznám.", sep="")
```

    Toto je Matouš


Pokud zapomeneš kulaté závorky, ohlášení **nemusí logicky pracovat**:


```python
TEXT = "Zapiš jméno: ".upper()

if jmeno := input(TEXT) == "Matouš":
    print("Toto je ", jmeno, sep="")
else:
    print("Tak ", jmeno, ", toho neznám.", sep="")
```

    Toto je True


Copak se stane:
1. *Interpret* nejprve uloží vstup do funkce `input()`,
2. následně vloženou hodnotu porovná,
3. výsledek (`True`/ `False`) uloží do proměnné `jmeno`.

### Kombinace s cyklem while


```python
TEXT = "Zapiš libovolný text [nebo 'q' pro ukončení]: "

while (vstup := input(TEXT)) != "q":
    print(vstup)
else:
    print(vstup, "Konec smyčky!", sep="\n")
```

    Zapiš libovolný text [nebo 'q' pro ukončení]: Ahoj
    Ahoj
    Zapiš libovolný text [nebo 'q' pro ukončení]: tak
    tak
    Zapiš libovolný text [nebo 'q' pro ukončení]: mame
    mame
    Zapiš libovolný text [nebo 'q' pro ukončení]: druhou
    druhou
    Zapiš libovolný text [nebo 'q' pro ukončení]: hodinu
    hodinu
    Zapiš libovolný text [nebo 'q' pro ukončení]: q
    q
    Konec smyčky!


Analogicky můžeš opsat celý postup také **bez přiřazovacího operátoru**:


```python
vstup = ""
TEXT = "Zapiš libovolný text [nebo 'q' pro ukončení]: "

while vstup != "q":
    vstup = input(TEXT)
    print(vstup)

else:
    print("Konec smyčky!")
```

    Zapiš libovolný text [nebo 'q' pro ukončení]: a
    a
    Zapiš libovolný text [nebo 'q' pro ukončení]: ahoj
    ahoj
    Zapiš libovolný text [nebo 'q' pro ukončení]: b
    b
    Zapiš libovolný text [nebo 'q' pro ukončení]: @
    @
    Zapiš libovolný text [nebo 'q' pro ukončení]: q
    q
    Konec smyčky!


Pokud ti tedy dovede operátor `:=` šikovně pomoct, **určitě jej využij**.
    
Není nutné jej **zneužívat** v situacích, kdy je zápis málo čitelný, nebo špatně pochopitelný.

Opatrně na **verze**.

Pokud vyvíjíš na jiném prostředí, než produkčním, můžeš zjistit, že **má starší verzi Pythonu** a *walrus* nemusí podporovat.

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.dYsikmEP2d5YjzPcygU9cQHaHa%26pid%3DApi&f=1&ipt=b01ae127da2c6fcbd9b3c4aa14f8fb0a4e8c876ca7d20bfdb844e203c95e9850&ipo=images" width="200" />



## Zkrácené přiřazování

---

Jde o **kratší způsob** pro úpravu hodnoty v existující proměnné.

Efektivnější není jen způsob zápisu, ale také způsob zpracování.

Doposud znáš tento zápis:
1. **Vytvoříš hodnotu** v proměnné `x`,
2. **upravíš hodnoty** v proměnné `x`,
3. **použiješ** novou hodnotu `x`.


```python
x = 2
```


```python
x = x + 3
```


```python
print(x)
```

    5


### Augmented assignment

Zkrácená varianta vypadá tak, že původní proměnnou `x` nepoužiješ a aritmetický operátor přesuneš přes rovnítko:


```python
x = 2
```


```python
x += 2
```


```python
print(x)
```

    4


### Rozdíl

Pro tebe, jako uživatele, je tento zápis pouze o něco kratší.

Vypadá odlišně, jinak je stejně zapsaný pomocí 3 řádků.

V čem je tedy lepší?

<br>

Pro mutable objekty je lepší z hlediska využití paměti - provádí operace tzv in-place.

##### Klasický zápis rozdělený na jednotlivé kroky:
1. Vytvoříš **novy seznam** a **uložíš ho** do proměnné,
2. **načteš** původní seznam,
3. **vytvoris nový seznam**, který obsahuje všechny hodnoty z původního a navíc hodnotu 4,
4. **uložíš** nový seznam do proměnné,
5. **vypíšeš ho**.


```python
x = [2, 3]
id(x)
```




    140435008588160




```python
x = x + [4]
id(x)

```




    140435008531968




```python
print(x)
```

    [2, 3, 4]


##### Ve zkráceném zápise:
1. Vytvoříš **novy seznam** a **uložíš ho** do proměnné,
2. **přidáš novou hodnotu** 4,
3. **vypíšeš ji**.


```python
x = [2, 3]
id(x)
```




    140435008727488




```python
x += [4]
id(x)
```




    140435008727488




```python
print(x)
```

    [2, 3, 4]


### Některé zkrácené operátory

| Původní operátor | Zkrácená varianta |
| :-: | :-: |
| `+` | `+=` |
| `-` | `-=` |
| `*` | `*=` |
| `/` | `/=` |
| `**` | `**=` |

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.yn3NMy-f9-hqQwXqFJ2AtwHaDt%26pid%3DApi&f=1&ipt=21b8ba84b48b23ddb2e3e0629a3748562777e0fbfa04fa9346da57b607ca5c08&ipo=images" width="250" />



## Souhrn úvodu smyček

---

Nyní máš za sebou stručný úvod do problematiky **iterátorů**. Jaké pojmy jsou tedy zásadní.

### Iterable
Anglické ozn., které představuje **takový objekt**, který umí vytvořit *iterátor* (pomůcka zab. funkce `iter()`).


```python
iter({2, 3})
```




    <set_iterator at 0x7fb992302640>




```python
iter((2, 3))
```




    <tuple_iterator at 0x7fb992cbd930>




```python
iter([2, 3])
```




    <list_iterator at 0x7fb992cbe470>




```python
iter(5)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[40], line 1
    ----> 1 iter(5)


    TypeError: 'int' object is not iterable



```python
iter(5.5)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[41], line 1
    ----> 1 iter(5.5)


    TypeError: 'float' object is not iterable


### Iterator
Anglické ozn., které představuje tzv. **iterátor**. Tedy objekt, který dovede podávat jednotlivé hodnoty (pomocí funkce `next()`).


```python
l_iter = iter({2, 3})
```


```python
next(l_iter)
```




    2



### Iteration
Anglické ozn., které představuje proces **iterace**. Což je proces, který postupně prochází hodnoty. Krok za krokem.


```python
for i in [5, 6]:
    print(i)
```

    5
    6



```python
i = 5
while i < 6:
    print(i)
    i += 5
```

    5


### For vs. while smyčka

Kdy máš vybrat co, lze popsat jako:
1. Pokud potřebuješ *iterovat* (~procházet) hodnotu od začátku do konce (tedy přes všechny hodnoty), použij `for`,
2. pokud potřebuješ *iterovat*, dokud platí nějaké kritérium, použij `while`.


```python
for i in range(5):
    print(i)
```

    0
    1
    2
    3
    4



```python
i = 0
while i < 5:
    print(i)
    i += 1
```

    0
    1
    2
    3
    4



```python
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    print(num)
```

    10
    20
    30
    40
    50



```python
numbers = [10, 20, 30, 40, 50]

iterator = iter(numbers)
while True:
    try:
        num = next(iterator)
        print(num)
    except StopIteration:  # tohle jeste probereme
        break
```

    10
    20
    30
    40
    50


##### Zadání

Napiš program, který vypíše všechny sudé čísla od 1 do 20 a zároveň vypíše jejich druhou mocninu. Použij cyklus `for`. Poté přepište tento program s použitím cyklu `while`. 

Pro pokročilé: přepis pomocí while a explicitní práci s iteratorem.



<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
for i in range(1, 21):
    if i % 2 == 0:
        print(f"Číslo: {i}, Druhá mocnina: {i ** 2}")

i = 1
while i <= 20:
    if i % 2 == 0:
        print(f"Číslo: {i}, Druhá mocnina: {i ** 2}")
    i += 1


iterator = iter(range(1, 21))
while True:
    i = next(iterator)
    if i % 2 == 0:
        print(f"Číslo: {i}, Druhá mocnina: {i ** 2}")
```
</details>

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.b7SnnLRXG2WiF98q1Dzp1gHaHN%26pid%3DApi&f=1&ipt=adbdd762327457e58a645b8fe9a7537ba63eef6ee1af682f4935eda3bbda36a7&ipo=images" width="200" />



## Comprehensions

---

Jde o proces, kdy můžeš **kratším a kompaktnějším** zápisem zkombinovat:
1. `for` cyklus,
2. jednodušší podmínky (!),
3. okamžitě plnit nové hodnoty daty.

Jde prakticky **o nejpoužívanější prvek** v Pythonu vůbec, který používá naprostá většina solidních programátorů.

### List comprehensions


```python
dvojnasobek = [cislo * 2 for cislo in range(30)]
```


```python
print(dvojnasobek)
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]


Jde tedy o ekvivalent k zápisu, který zatím znáš jako:


```python
dvojnasobek = list()

for cislo in range(30):
    dvojnasobek.append(cislo * 2)
```


```python
print(dvojnasobek)
```

    [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58]


<br>

V kombinaci s větví `if `:


```python
data = [1, 2, 3, "a", 5, 6, "@", "7", 7]

dvojnasobek = [cislo * 2 for cislo in data if isinstance(cislo, int)]
```


```python
print(dvojnasobek)
```

    [2, 4, 6, 10, 12, 14]


Pokud je zápis v závorce delší a **málo přehledný**:


```python
data = [1, 2, 3, "a", 5, 6, "@", "7", 7]

dvojnasobek = [
    cislo * 2
    for cislo in data
    if isinstance(cislo, int)
]
```


```python
dvojnasobek = list()
data = [1, 2, 3, "a", 5, 6, "@", "7", 7]

for cislo in data:
    if isinstance(cislo, int):
        dvojnasobek.append(cislo * 2)
```

**Obecný vzorec** tedy vypadá jako:


```python
# vysledna_promenna = [
#     <hodnota>
#     <for_smycka>
#     <podminka>
# ]
```

### Dict comprehensions

*Comprehensions* můžeš skládat také **ze slovníků**:


```python
obyvatele = {
    "Praha": 1_335_084, 
    "Brno": 382_405, 
    "Ostrava": 284_982,
    "Plzen": 175_219, 
    "Liberec": 104_261
}
```


```python
velka_mesta = {
    klic.upper(): hodnota
    for klic, hodnota in obyvatele.items()
    if hodnota > 200_000
}
```


```python
print(velka_mesta)
```

    {'PRAHA': 1335084, 'BRNO': 382405, 'OSTRAVA': 284982}



```python
velka_mesta = dict()

for klic, hodnota in obyvatele.items():
    if hodnota > 200_000:
        velka_mesta[klic.upper()] = hodnota
```

Podmínka **o dvou větvích**:


```python
lego_ceny = {
    "7104: Desert Skiff": {"cena_$": 6, "rok_vydani": "2000"},
    "7190: Millennium Falcon": {"cena_$": 100, "rok_vydani": "2000"},
    "75044: Droid Tri-Fighter": {"cena_$": 30, "rok_vydani": "2015"}
}
```


```python
ceny_s_inflaci = {
    jmeno: (
        hodnoty["cena_$"] * 2.27
        if hodnoty["rok_vydani"] == "2000"
        else hodnoty["cena_$"] * 2.51
    )
    for jmeno, hodnoty in lego_ceny.items()
}
```


```python
print(ceny_s_inflaci)
```

    {'7104: Desert Skiff': 13.620000000000001, '7190: Millennium Falcon': 227.0, '75044: Droid Tri-Fighter': 75.3}



```python
ceny_s_infl = dict()

for jmeno, hodnoty in lego_ceny.items():
    if hodnoty["rok_vydani"] == "2000":
        ceny_s_infl[jmeno] = hodnoty["cena_$"] * 2.27
    else:
        ceny_s_infl[jmeno] = hodnoty["cena_$"] * 2.51
```


```python
print(ceny_s_infl)
```

    {'7104: Desert Skiff': 13.620000000000001, '7190: Millennium Falcon': 227.0, '75044: Droid Tri-Fighter': 75.3}


### Set comprehensions


```python
ziskane_adresy = {"me@matousholinka.com", "petr@svetr.com", "lukas@gmail.com", "nan_email"}
```


```python
domeny = {
    adresa.split("@")[1]
    for adresa in ziskane_adresy
    if "@" in adresa
}
```


```python
print(domeny)
```

    {'matousholinka.com', 'gmail.com', 'svetr.com'}



```python
domeny = set()

for adresa in ziskane_adresy:
    if "@" in adresa:
        domeny.add(adresa.split("@")[1])
```


```python
print(domeny)
```

    {'matousholinka.com', 'svetr.com', 'gmail.com'}


### Nestovaná komprehence

Nakonec ještě ukázkat nestované *comprehensions*.

Tady je potřeba si zápis prohlédnout a zamyslet se, jestli je dostatečně **pochopitelný a čitelný** (obecně).

Je totiž k ničemu, pokud zapíšeš **nadupanou smyčku**, kterou budeš někomu *koktavě vysvětlovat*, nebo si o nějaký týden později neuvědomíš, co má tebou napsaná smyčka, vůbec dělat:


```python
data = [
    ["jméno", "přijmení", "email", "projekt"],
    ["Lucie", "Nováková", "lucie.novakova@seznam.cz", "projekt_a"],
    ["Petr", "Svetr", "petr.svetr@gmail.com", "projekt_b"]
]
```


```python
hledana_jmena = [
    bunka
    for radek in data
    for bunka in radek
    if "_" in bunka
]
```


```python
print(hledana_jmena)
```

    ['projekt_a', 'projekt_b']



```python
hledana_jmena = list()

for radek in data:
    for bunka in radek:
        if "_" in bunka:
            hledana_jmena.append(bunka)
```


```python
print(hledana_jmena)
```

    ['projekt_a', 'projekt_b']


##### Zadání

Napište program, který vytvoří seznam prvních 20 celých čísel. Poté pomocí for cyklu vytvořte nový seznam, který obsahuje pouze čísla, která jsou dělitelná 3, a zároveň vypočítá jejich druhou mocninu. Poté tento program přepište pomocí list comprehension.


<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
numbers = list(range(1, 21))
squares_of_multiples_of_3 = []
for num in numbers:
    if num % 3 == 0:
        squares_of_multiples_of_3.append(num ** 2)
print(squares_of_multiples_of_3)

numbers = list(range(1, 21))
squares_of_multiples_of_3 = [num ** 2 for num in numbers if num % 3 == 0]
print(squares_of_multiples_of_3)
```
</details>

##### Zadání

Tvým úkolem bude odstraňovat písmena ze zadaného seznamu pomocí funkce `input`:
```python
pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]
```

Jakmile budou všechna písmena odstraněná, vypíše tvůj program:
```python
Seznam je prázdný!
```

Pokud zapíšeš písmeno, které v zadaném seznamu není, dostaneš upozornění:
```python
x není součástí písmen!
```

Průběh může vypadat následovně:
```python
Začátek: ['a', 'a', 'b', 'c', 'd', 'a', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? a
Zbývají písmena ['a', 'b', 'c', 'd', 'a', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? a
Zbývají písmena ['b', 'c', 'd', 'a', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? a
Zbývají písmena ['b', 'c', 'd', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? b
Zbývají písmena ['c', 'd', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? c
Zbývají písmena ['d', 'e', 'g', 'm']
ktere písmeno chceš vyhodit? d
Zbývají písmena ['e', 'g', 'm']
ktere písmeno chceš vyhodit? e
Zbývají písmena ['g', 'm']
ktere písmeno chceš vyhodit? x
x není součástí písmen!
ktere písmeno chceš vyhodit? g
Zbývají písmena ['m']
ktere písmeno chceš vyhodit? m
Seznam je prázdný!
```


```python
help(list.remove)
```

    Help on method_descriptor:
    
    remove(self, value, /)
        Remove first occurrence of value.
        
        Raises ValueError if the value is not present.
    



```python
pismena = ["a", "a", "b", "c", "d", "a", "e", "g", "m"]

while pismena:
    print(", ".join(pismena))
    
    zadani = input("ktere písmeno chceš vyhodit?")
    
    if zadani not in pismena:
        print(zadani + " není součástí písmen!")
    else:
        pismena.remove(zadani)

else:
    print("Konec hry!")
```

---
