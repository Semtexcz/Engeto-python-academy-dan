# Python akademie

---

<br>

## Obsah lekce

---

1. [Obecně ke knihovnám](#Obecně-ke-knihovnám),
2. [ohlášení knihoven](#Obecně-ke-knihovnám),
3. [moduly](#Moduly),
4. [balíčky](#Balíčky),
5. [knihovny třetích stran](#Knihovny-třetích-stran).
<br>

---

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.lcaRsa47BhZ7k0yfLdB6AgHaHa%26pid%3DApi&f=1" width="200" style="margin-left:auto; margin-right:auto" >

## Obecně ke knihovnám

---

<br>

### Co je to knihovna

---

Knihovny v Pythonu jsou prakticky soubory s příponou `.py`.


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.353pM1jJdG9e1a3tIlIbjwHaHa%26pid%3DApi&f=1&ipt=2a6ce2dfa6dd729e25be4d186ce0d0fefce73272938c52b7a2bff4ed74c5b16a&ipo=images" width="100" style="margin-left:auto; margin-right:auto" >

<br>

### Jak vypadá knihovna

---

Obsahují v sobě kód, který ty můžeš **rovnou použít** a nemusíš ho přepisovat od začátku.

Autor knihovny si dal práci, že napsal funkce, proměnné, podmínkové zápisy a smyčky tak, že ty už je psát nemusíš.

<br>

#### Knihovna `random.py`

---


```python
import random
```


```python
# print(help(random))
```

#### **Demo:** Ukázka knihovny `random`

<br>

### Obecné dělení

---

Podle struktury knihovny:
1. **Moduly**, tedy samotný soubor s příponou **.py**,
2. **balíčky**, celý adresář, který může obsahovat několik modulů.

<br>

### Proč psát/používat knihovny

---

Pro tebe je to velká výhoda, protože si tento kód jednoduše nahraješ a můžeš se víc soustředit na to, co ty potřebuješ.

<br>

### Praktická ukázky některých knihoven

Ověř **operační systém** pomocí Pythonu:


```python
import sys
```


```python
if sys.platform == "windows":
    print("Spouštím cmd pro Win..")
else:
    print("Spouštím cmd pro unix-based systémy..")
```

    Spouštím cmd pro unix-based systémy..



```python
print(sys.platform)
```

    linux


<br>

Operace **se soubory, cestami** v rámci tvého OS:


```python
import os            # Obdoba: pathlib
```


```python
print(os.getcwd())   # Aktuální umístení
```

    /home/matous/projects/python-academy-2024/shared/notebooks



```python
print(os.listdir())  # Dostupné soubory
```

    ['lesson04.ipynb', 'lesson01.ipynb', '.ipynb_checkpoints', 'lesson07.ipynb', 'lesson05.ipynb', 'lesson11.ipynb', 'lesson06.ipynb', 'lesson02.ipynb', 'lesson08.ipynb', 'lesson03.ipynb', 'lesson10.ipynb', 'lesson12.ipynb', 'lesson09.ipynb']


<br>

Spočítej **3 nejčastější znaky** v zadaném `str`:


```python
from collections import Counter  # Počítání výskytů
```


```python
pocitadlo = Counter("abcdeabcdabcaba")
print(pocitadlo.most_common(3))
```

    [('a', 5), ('b', 4), ('c', 3)]


<br>

## Ohlášení knihoven

---

Jak můžeš knihovny **používat**?

*Použít* knihovnu znamená **nahrát ji**.


```python
print(collections.namedtuple)  # Bez ohlášení knihovny
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[12], line 1
    ----> 1 print(collections.namedtuple)  # bez ohlášení knihovny


    NameError: name 'collections' is not defined



```python
from collections import namedtuple
```


```python
print(namedtuple)  # s ohlášením knihovny
```

    <function namedtuple at 0x7fc6025f5f70>


Samotný způsob nahrátí (nebo také ohlášení) o nahrávání může mít několik podob:
1. `import <knihovna>`,
2. `from <knihovna> import *`,
3. `from <knihovna> import <objekt>`,
4. `from <knihovna> import <objekt> as <alias>`,
5. `import <knihovna> as <alias>`.

<br>

### Nahrávání s `import`

----
    
Nejjednodušší a nejpoužívanější ohlášení pomocí klíčové výrazu `import`:


```python
import math
```

...dále je potřeba pracovat **se skutečnými knihovnami**:


```python
print(math.pi)
```

    3.141592653589793



```python
print(math.e)
```

    2.718281828459045



```python
print(pi)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    Cell In[19], line 1
    ----> 1 print(pi)


    NameError: name 'pi' is not defined



```python
pii = math.pi
```


```python
print(pii)
```

    3.141592653589793


Nejprve nahraješ knihovnu `math`, případně **jméno souboru** bez přípony.

Následně použiješ potřebný objekt (v ukázce konstantu `pi`).

<br>

Podobně můžeš později pracovat se svými soubory `.py`:
```python
# pomocny_modul_1.py
import pomocny_modul_1

print(pomocny_modul_1.moje_promenna)
```

Ohlášení `import <knihovna>` je příhodné, pokud potřebuješ z jedné knihovny **použít více objektů** a současně mít pěkně přehled, ke které knihovně tyto objekty patří.

<br>

### Nahrávání s `from` a hvězdičkou

----

Tento způsob nahrávání **není moc častý**.

Použiješ jej zejména při práci s *interaktivním interpretem* a jednodušších zápisech či kratších ukázkách.


```python
from sys import *
from math import *
```


```python
print(
    e,            # odkud pochází proměnná 'e'? sys/math?
    version,      # ... a odkud 'version'?
    sep="\n"
)
```

    2.718281828459045
    3.8.10 (default, Mar 25 2024, 10:42:49) 
    [GCC 9.4.0]


##### Rekapitulace

Obecně se **tato varianta nahrávání nedoporučuje**, zejména kvůli svojí špatné přehlednosti a zanesení aktuálního prostředí spoustou nevyužitých objektů.

<br>

### Nahrávání s `from` bez hvězdičky

----

Důvod, proč jej není vhodné používat je proto, že uživatel **nepotřebuje uvádět jména objektů** (nevidíš jakou proměnnou nahrál).

Pokud potřebuješ použít třeba **jen jednu proměnnou** nebo objekt obecně, určitě oceníš právě toto ohlášení. 


```python
from math import e, pi
```


```python
print(e)   # math.e
```

    2.718281828459045



```python
print(pi)  # math.pi
```

    3.141592653589793


Oproti variantě s hvězdičkou je rozdíl, že tento způsob napíšeš, pokud potřebuješ jen velmi málo konkrétních objektů.

Současně musíš uvádět, jaký objekt, **odkud nahráváš**.

Při tomto ohlašování vypadá zápis následovně:

1. `from`, tedy klíčový výraz,
2. `math`, jméno knihovny,
3. `import`, klíčový výraz,
4. `e`, jméno proměnné, funkce, aj.

##### Rekapitulace

Jde o způsobem, kdy potřebuješ třeba **jen jedinný objekt z knihovny**, a ten si explicitně ohlášením nahraješ.

<br>

### Nahrávání s `from` bez hvězdičky a s aliasem

----

Pokud je **jméno nahrávaného objektu** příliš dlouhé (např. `EXTRA_DLOUHE_JMENO_KONSTANTY`), případně náročné pro zápis, potom může být přepisování takového jména nepohodlné.

Pokud na takový objekt narazíš, můžeš vyzkoušet **alias**, který definuješ pomocí klíčového slova `as`:
```python
from <knihovna> import <EXTRA_DLOUHE_JMENO_KONSTANTY> as <alias>

print(<alias>)
```

Alias pro kostantu `pi` není zrovna šikovný, ale jde hlavně o ukázku zápisu a použití:


```python
from string import punctuation
```


```python
print(punctuation)
```

    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~



```python
from string import punctuation as p  # obdoba: p = punctuation

print(p)
```

    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~



```python
from string import punctuation as p
punctuation = '.,;'
print(punctuation)
print(p)
```

    .,;
    !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~


Samozřejmě u jména proměnné jako `pi` není potřeba zapisovat *alias* (jméno je stručné a jasné samo o sobě).

S aliasy ale opět pozor. Pokud se jich v jednom souboru objeví víc (3+), potom se opět čtení zápisu stává **méně přehledný**.

1. Nejprve uvidíš *alias* (v ukázce `p`),
2. po té potřebuješ najít proměnnou (v ukázce `pi`), kterou **alias přebírá**,
3. nakonec dohledat knihovnu (.. `math`), ze které pochází.

##### Rekapitulace

*Alias* je výhodný, pokud potkáš v knihovně objekt s dlouhým jménem.

<br>

### Nahrávání s `import` a s aliasem

----

Stejně tak je možné použít alias pro delší jméno knihovny (např. EXTRA_DLOUHE_JMENO_KNIHOVNY).

Teoreticky potom nastává tato situace:
```python
import <EXTRA_DLOUHE_JMENO_KNIHOVNY>

print(<EXTRA_DLOUHE_JMENO_KNIHOVNY>.objekt)
```


*Alias* pro knihovnu `configparser`:


```python
import configparser as cp  # obdoba: cp = configparser

print(cp)
```

Pokud je jméno knihovny (třeba `math`) **dostatečně stručné a jasné**, nemusíš *alias* používat.

##### Rekapitulace

*Alias* je výhodný, pokud potkáš knihovnu s dlouhým jménem.

### Souhrn

---
* `import <knihovna>`, běžné obecné ohlášení,
* `from <knihovna> import *`, pouze pro debugování, zkoušení,
* `from <knihovna> import <objekt>`, pokud potřebuji jen několik málo vybraných objektů, kratší zápis,
* `from <knihovna> import <objekt> as <alias>`, pokud potřebuji alias pro objekty
* `import <knihovna> as <alias>`.

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s *importováním* knihoven:

1. Nahraj knihovnu `math`,
2. pro zadaný tuple `polomery`, vypočítej plochu kruhů (prozkoumej objekty v knihovně `math`, kde potřebuješ dohledat mocniny a konstantu pí),
3. vypočítané plochy potom ukládej do proměnné `plochy`.


```python
import math

polomery = (1, 2, 3, 4, 5)
```


```python

```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
import math

polomery = [1, 2, 3, 4, 5]
plochy = list()

for polomer in polomery:
    plochy.append(math.pow(polomer, 2) * math.pi)
else:
    print(plochy)
```
</details>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.cjfmUt8xYHoEdmQWxT1fBgHaHa%26pid%3DApi&f=1" width="300" style="margin-left:auto; margin-right:auto">


## Moduly

---

Modulem je tedy jakýkoliv soubor s příponou `.py`, který napíšeš ty, nebo jiní programátoři.


Ty **nejčastější moduly** jsou již součástí instalace Pythonu, takže už v tento moment máš u sebe **nainstalovanou paletu těch nejpoužívanějších** (*zabudovaných* nebo také *built-in*) modulů.

<br>


```python
import os      # modul pro práci s operačním systémem
```


```python
import sys     # modul pro přístup k některým systémovým proměnným
```


```python
import random  # modul pro práci s pseudo-náhodnými procesy
```

Pomocí built-in funkce `dir` si můžeš ověřit, že po importování máš v aktuálním pracovním rámci nahráné moduly k dispozici (`True`), zatím co fiktivní muj_modul ne (`False`).


```python
print(
    "os" in dir() \
    and "sys" in dir() \
    and "random" in dir()
)
```

Pokud si vybereš **jméno modulu**, který **není součástí zabudovaných modulů** [pro tvoji verzi Pythonu](https://docs.python.org/3/library/index.html), dostaneš výjimku:


```python
%%file matousuv_modul.py
"""Toto je můj vlastní modul, Matouš."""
```

    Writing matousuv_modul.py



```python
import matousuv_modul
```


```python
import daviduv_modul
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[44], line 1
    ----> 1 import daviduv_modul


    ModuleNotFoundError: No module named 'daviduv_modul'



```python
print(help(matousuv_modul))
```

    Help on module matousuv_modul:
    
    NAME
        matousuv_modul - Toto je můj vlastní modul, Matouš.
    
    FILE
        /home/matous/projects/python-academy-2024/shared/notebooks/matousuv_modul.py
    
    
    None


<br>

### Vlastní modul

---

V úvodu stojí, že si modul můžeš napsat **přímo ty**.

Můžeš si vytvořit např. modul, který obsahuje `dict` s největšími městy v *České republice*. Ten si uložíš k sobě do složky pod jménem `mesta_cr.py`:


```python
%%file mesta_cr.py
# soubor mesta_cr.py
vsechny_mesta = {
    "Praha": 1_335_084,
    "Brno": 382_405,
    "Ostrava": 284_982,
    "Plzeň": 175_219,
    "Liberec": 104_261,
    "Olomouc": 100_514,
    "České Budějovice": 94_229,
    "Hradec Králové": 92_683,
    "Ústí nad Labem": 91_982,
    "Pardubice": 91_755,

}
```

Následné si vytvoříš **druhý soubor** (ve stejném adresáři) `nad_100_k.py`, který bude obsahovat:


```python
# soubor nad_100_k.py
from mesta_cr import vsechny_mesta

for mesto, obyvatele in vsechny_mesta.items():
    if obyvatele > 100_000:
        print(mesto)
```

<br>

### Nápověda `help`

----

Často se dostaneš do situace, kdy si **nebudeš vědět rady**.

Nezapamatuješ si jméno *metody* v *knihovně*, jméno *proměnné*, atd.

Můžeš samozřejmě navštívit různé dokumentace, knihy nebo články. Ale pokud potřebuješ okamžité offline řešení vyzkoušej funkci `help()`.


```python
import random
```


```python
print(dir(random)[39:])
```

    ['betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']



```python
print(help(random.randint))
```

    Help on method randint in module random:
    
    randint(a, b) method of random.Random instance
        Return random integer in range [a, b], including both end points.
    
    None



```python
print(random.randint(1, 5))
```

    5


<br>

### Funkce `dir`

----

Pokud potřebuješ podrobný výpis, je lepší použít funkci `help`.

Pokud ti stačí jen seznam všech dostupných metod, vyzkoušej metodu `dir`.


```python
print(dir(random))
```

    ['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_ONE', '_Sequence', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_accumulate', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_fabs', '_floor', '_index', '_inst', '_isfinite', '_lgamma', '_log', '_log2', '_os', '_pi', '_random', '_repeat', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'binomialvariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randbytes', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']



```python
random.choices? # funkční jen v Jupyter notebooku
```

    [0;31mSignature:[0m [0mrandom[0m[0;34m.[0m[0mchoices[0m[0;34m([0m[0mpopulation[0m[0;34m,[0m [0mweights[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0;34m*[0m[0;34m,[0m [0mcum_weights[0m[0;34m=[0m[0;32mNone[0m[0;34m,[0m [0mk[0m[0;34m=[0m[0;36m1[0m[0;34m)[0m[0;34m[0m[0;34m[0m[0m
    [0;31mDocstring:[0m
    Return a k sized list of population elements chosen with replacement.
    
    If the relative weights or cumulative weights are not specified,
    the selections are made with equal probability.
    [0;31mFile:[0m      /usr/lib/python3.12/random.py
    [0;31mType:[0m      method

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s *moduly*:

1. Nahraj z knihovny `random` objekt pro výběr 10 náhodných čísel z intervalu **0-1000**,
2. nahraj z knihovny `statistics` objekt pro výpočet průměrné hodnoty z *iterovalného* objektu `mean`,
3. do proměnné `nahodna_cisla` ulož **10 náhodných celých čísel**,
4. do proměnné `prumer` ulož průměrnou hodnotu,
5. výsledek na závěr vypiš ve formátu:`Průměr náhodných čísel je:  <prumer>`.


```python
from statistics import mean
from random import choices
```


```python

```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
from random import choices
from statistics import mean

nahodna_cisla = choices(range(0, 1001), k=10)
prumer = mean(nahodna_cisla)
print("Průměr náhodných čísel je:", prumer, sep='')
```
</details>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Rq-hToMXLKlFsOOyPp_85QHaHa%26pid%3DApi&f=1" width="200" style="margin-left:auto; margin-right:auto">

## Balíčky

---

Pokud je **modul** samotný soubor s příponou **.py**, potom je **balík** v podstatě *sbírka několika modulů* (tedy souborů **.py**). [https://github.com/python/cpython/tree/main/Lib/json](https://github.com/python/cpython/tree/main/Lib/json)


Prohlédni si třeba obsah adresář (tedy balíček) `json`:
```
json/
├── __init__.py
├── __pycache__
├── decoder.py
├── encoder.py
├── scanner.py
└── tool.py
```

Kromě **modulů** (soubory s příponou **.py**) obsahují balíčky tyto **speciální soubory**:
1. `__init__.py`,
2. `__pycache__`.


Proč je tedy dobré mít jak **moduly**, tak **balíčky**? Někdy je totiž příkazů, objektů a podmínek je v jednom souboru tolik, že by se stal jeden soubor nepřehledný, špatně pochopitelný.

Proto se programátoři snaží tyto objekty (proměnné, smyčky, podmínky), které **k sobě logicky patří**, **rozdělit na víc modulů** a sdružit do jednoho balíčku.

<br>

### \_\_init\_\_.py

----

Pokud nahlédneš do struktury balíčků, určitě si všimneš souboru `__init__.py`.

Jeho účel je v podstatě indexovat adresář balíčku a pomoci *interpreta* najít konkrétní modul.

Pokud v adresáři soubor `__init__.py` chybí, interpret jej nebude prohledávat.

<br>


```python
import json
```


```python
print(json.__version__)
```

    2.0.9


<br>

### \_\_pycache\_\_

----

Pokud spustíš libovolný soubor s příponou **.py**, potom jej *interpret* začne postupně *kompilovat* na *bytecode*.

Z tohoto kroku vznikají soubory **.pyc**.

Ty dále pomáhají (v případě, že nechybí) přeskočit krok *kompilace* příště a spouštět tvůj soubor rychleji.

Pokud náhodou složka `__pycache__` v adresáři balíčku chybí, *interpret* si ji vytvoří na příště při prvním spuštění.

### Jak Python překládá kód až na strojový kód (pro zvídavé)

https://www.remnote.com/a/Princip-fungovani-Python/6708ef898f7fbebbbb06303e

<br>

### Vlastní balíček

---

Stejně jako u *modulu*, můžeš samozřejmě vytvořit **vlastní balíček**.


Pro ilustraci se podívej na tento balíček:
```
matousuv_balik/
├── __init__.py
├── __pycache__
├── adresy.py
└── jmena.py
```

1. Pro vytvoření takového *klasického* balíčku tedy neprve vytvoríš složku `muj_balicek`,
2. přesuneš se dovnitř adresáře `muj_balicek` a v něm vytvoříš prázdný soubor `__init__.py`,
3. dále vytvoříš soubor `adresy.py`,
```python
# adresy.py
zamestnanci = {
    11: {"obec": "praha", "ulice": "milesovska", "c.p.": "11a"},
    12: {"obec": "brno", "ulice": "podebradova", "c.p.": "123"},
    13: {"obec": "olomouc", "ulice": "krizikova", "c.p.": "2a"},
    14: {"obec": "plzen", "ulice": "stribneho", "c.p.": "301"},
}
```

4. nakonec vytvoříš soubor `jmena.py`,
```python
# jmena.py
jmena = {
    11: {"jmeno": "Petr", "prijmeni": "Svetr"},
    12: {"jmeno": "Matous", "ulice": "Svatous"},
    13: {"jmeno": "Lukas", "ulice": "Gulas"},
    14: {"jmeno": "Martin", "ulice": "Tecka"},
}
```

5. složku `__pycache__` tvořit nemusíš. Interpret si ji nachystá sám, až budeš potřebovat balíček spustit.

Nyní si vytvoř nový modul `spojena_data.py`:
```python
# soubor spojena_data.py
from muj_balicek.adresy import zamestnanci
from muj_balicek.jmena import jmena

print(bydliste[11], zamestnanci[11])
```

<img src="https://twixes.gallerycdn.vsassets.io/extensions/twixes/pypi-assistant/1.0.3/1589834023190/Microsoft.VisualStudio.Services.Icons.Default" width="200" style="margin-left:auto; margin-right:auto">

## Knihovny třetích stran

---

Podle **původu knihovny** můžeme říct, že máme **dva typy** knihoven:

1. **Standardní knihovny** (tedy dostupné ihned po instalaci),
2. **knihovny třetích stran** (je nutné je doinstalovat).


```python
import uuid
import random
import typing
```


```python
import flask
```


    ---------------------------------------------------------------------------

    ModuleNotFoundError                       Traceback (most recent call last)

    Cell In[65], line 1
    ----> 1 import flask


    ModuleNotFoundError: No module named 'flask'


Předtím než budeš moct tyto knihovny používat, je musíš vyhledat, stáhnout a nainstalovat.

Většinu dostupných knihoven najdeš na [pypi.org](https://pypi.org/)

Tady si knihovnu najdeš, pročteš a následně stáhneš (*ukázka terminal + PyCharm*).

### Virtuální prostředí

---

Jakmile začneš s Python pracovat na více projektech, je dobré **oddělit jednotlivá prostředí**:
```
/projekty
   ├─projekt01/  # knihovnu 1.1
   ├─projekt02/  # knihovnu 1.2
   ├─projekt03/
   ├─pracovni/
   └─pokus/
```

Každý projekt (složka v ukázce výše) může totiž pracovat **s různými knihovnami** (a různými verzemi).


Různé knihovny znamenají různé související knihovny (a různé verze), drobné úpravy syntaxí, jména metoda a funkcí (příp. proměnných).


Dobrým zvykem bývá **oddělit knihovny pro různé projekty**. Tedy neinstalovat knihovny globálně pro celý tvůj počítač,ale ke konkrétním projektům (pomocí *virtuálních prostředí*).

<br>


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.rkP6qcdgLXFW14tTAIcBewHaHa%26pid%3DApi&f=1&ipt=2e056bff7e07855bd40696229c6e1e570eae2d4f91c4c2155f97668b2d6a8311&ipo=images" width="300" style="margin-left:auto; margin-right:auto">

#### Příkazový řádek

----

1. **Vytvoříš** virtualní pracovní prostředí pomocí následující příkazu:
```
python3 -m venv <jmeno_prostredi>
```

2. **Aktivujeme** virtualní pracovní prostředí pomocí jeho jména. Po aktivaci dostaneme na začátku dotazovacího řádku závorku se jménem prostředí (př. `(env)`):
```
source <jmeno_prostredi>/bin/activate  # aktivace Linux
.\venv\Scripts\activate.bat            # Windows CMD
.\venv\Scripts\activate.ps1            # Windows PowerShell
deactivate                             # ukončení
```

3. **Ověříme dostupnost správce** balíčků (conda, pipenv, poetry, pip je defaultně nainstalovaný ze druhé lekce):
```
pip --version
```

4. Pokud máme, **instalujeme balíčky**:
```
pip install <jmeno_balicku>         # instalace
pip uninstall <jmeno_balicku>       # odstranění
pip --help                          # nápověda
```

5. **Vytvoříme soubor** se souvisejícími knihovnami pro další uživatele `requirements.txt`. Ten obsahuje jména a verze knihoven, aby je mohli snadno nainstalovat i jiní uživatelé:
```
pip freeze > requirements.txt  # přesměruji výstup z příkazu do souboru
```

6. ... soubor `requirements.txt` lze potom naopak nainstalovat **do nového virtuálního prostředí**:
```
pip install -r requirements.txt
```

Jak udržovat balíčky aktuální + kontrola:
```
pip list --outdated                          # zobrazím výpis všech neaktuálních knihoven
pip install --upgrade <jmeno_knihovny>       # upgradování
pip install <jmeno_knihovny>==<cislo_verze>  # alternativní řešení
```

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.p4NKEAqAdgFX_u8PwtI_nwHaHa%26pid%3DApi&f=1" width="200" style="margin-left:auto; margin-right:auto">



#### PyCharm

---

1. Vytvoř si **nový adresář** (prázdný),
2. otevři jej pomocí **PyCharm** (optiona Open...),
3. vlož **nový modul** (klidně prázdný),
4. přejdi do **settings** (ctrl+alt+s),
5. *project interpreter*, *nastavení* ⚙, *vytvořit nové prostředí*,
6. **přidat nové knihovny** (ikonka plus),
7. *tools*, *sync Python requirements* (txt soubor s knihovnami a verzemi).

<br>

➡️ ➡️ **Formulář pro Tvoje hodnocení** [**šesté lekce**](https://forms.gle/8HFnNH4nymJb8nKc9) ⬅️ ⬅️

<br>

<br>

## Domácí úkol

---
<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.O9EkosTHP3lmEAvzA3D-2QHaHa%26pid%3DApi&f=1" width="200" style="margin-left:auto; margin-right:auto" />


Nageneruj data **pro zaměstnance** a jejich **oddělení**. Data budou mít následující strukturu:


```python
# Ukázka pouze pro dva zaměstnance
zamestnanci = {
    "zamestnanec_id": (1, 2),  
    "jmeno": ("Petr", "Matous"),
    "prijmeni": ("Svetr", "Holinka"),
    "telefon": ("+420 777 666 555", "+420 776 665 554"),
    "email": ("p.svetr@firma.cz", "m.holinka@firma.cz"),
    "vytvoreno": ('31/01/1996', '09/09/2000')
}
```

Jak údaje získat:

#### Zaměstnanecké ID

---

Do klíče `"zamestnanec_id"` vlož `tuple` s celými čísly jednotlivých zaměstnanců. Tedy první zaměstnanec dostane **1** a poslední **107**.


*NÁPOVĚDA*, čísla zadej pomocí `range`.

#### Jméno zaměstnance

---

Do klíče `"jmeno"` vlož `tuple` s jednotlivými jmény, které naparsuješ (získáš) ze zadané proměnné `zamestnanci_raw`.

#### Příjmení zaměstnance

---

Do klíče `"prijmeni"` vlož `tuple` s jednotlivými příjmeními, které naparsuješ (získáš) ze zadané proměnné `zamestnanci_raw`.

#### Telefon zaměstnance

---

Do klíče `"telefon"` vlož `tuple` se stringy, které obsahují telefonní čísla.

Tato čísla vytvoříš jako devět náhodných čísel, která připojíš ke stringu `"+420"`. Výsledek tedy bude vypadat jako `"+420"` a správně naformátované hodnoty `"123345343"`. Výsledek: `"+420 123 345 343"`.

*NÁPOVĚDA*, čísla náhodně vyber z knihovny `random`.

#### Email zaměstnance

---

Do klíče `"email"` vlož `tuple` se stringy obsahující emailové adresy zaměstnanců.

Tento email nachystej pomocí:
1. Prvního písmena ze jména zaměstnance (malé písmeno),
2. tečky,
3. celého příjmení zapsaného malými písmeny,
4. @firma.cz.

Všechny údaje musí být bez diakritiky.

Ukázka:
```python
jmeno = "Kryštof"
prijmeni = "Slunečný"

email = "k.slunecny@firma.cz"
```


*NÁPOVĚDA*, knihovna `unidecode`.

#### Datum nástupu zaměstnance

---

Do klíče `"vytvoreno"` vlož `tuple` se stringy obsahující náhodné datumy mezi daty **1.1.1990** a **1.1.2020**.

Datumy nemusí být unikátní, ale musí být ve formátu `"dd/mm/rrrr"`

*NÁPOVĚDA*, knihovna `time`.

<br>


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

---
