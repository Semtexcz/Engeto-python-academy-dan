# Python akademie

---

<br>

## Obsah lekce

---

1. [Prezentace](ss),
2. [Python, obecný úvod](#Python,-obecný-úvod),
3. [Python, pracovní prostředí](#Python,-pracovní-prostředí),
4. [První krůčky](#První-krůčky),
5. [Číselné hodnoty](#Číselné-hodnoty),
6. [Textové hodnoty](#Textové-hodnoty),
7. [Proměnné, odkazy](#Proměnná-v-Pythonu),
8. [Sekvence](#Sekvence-list,-tuple),
9. [Zabudované funkce](#Úvod-do-funkcí),
10. [Domácí úkol](#Domácí-úkol).

---

➡️ ➡️ [Úvodní prezentace](https://docs.google.com/presentation/d/1EvRLT0SgAflGfvTWTY0ldy0jpcpBXVLvEG6sSlGQU1g/edit#slide=id.g27be84891c0_0_78) ⬅️ ⬅️

---

<br>

## Python, obecný úvod


### Co je to **programování**?

---

Programování, obecně, je postup, kdy se člověk snaží předepsat (obecně vysvětlit) úkol počítači.

<br>

### Co je to **programovací jazyk**?

---



**Jazyk lidí** a **počítačů** je odlišný.

Proto je potřeba zavést nějaký **společný jazyk**, aby se obě strany domluvily.


Tímto společným jazykem je právě **programovací jazyk**.

<img src="../languages - Imgur.png" width="1000" style="margin-left:auto; margin-right:auto">


<br>

### Proč se učit **Python**?

---
Některé programovací jazyky, jako je *Python*, jsou pro člověka **snadněji pochopitelné** (syntaxe čitelnější, lidštější).

#### **Python**:


```python
print("Hello world!")
```

    Hello world!


<br>

#### **C**:


```python
#include <stdio.h>

int main(void) {
  printf("Hello World\n");
  return 0;
} 
# => 'Hello World'
```

<br>

#### **Javascript**:


```python
const say_hello = (name) => {
  console.log(`Hello, ${name}`);  // template string
}

say_hello('Matouš')
# => 'Hello, Matouš'
```

Python mj. patří k tzv. *vysokoúrovňové programovací jazyky*.

Ty jsou sice **vzdálenější k řeči počítačů**, za to jsou **čitelnější pro člověka**.


<img src="../scale.png" />

Druhou skupinou programovacích jazyků jsou *nízkoúrovňové programovací jazyky* (mají blíže k jedničkám a nulám).

<br>

Např. jazyky jako **C** nebo **Assembly**, jsou naopak náročnější na **čtení a pochopení**.

Proto nejsou zcela vhodné pro úplné **začátky v programování**.

#### **Demo**: [Stackoverflow comp.](https://insights.stackoverflow.com/survey/2021#most-loved-dreaded-and-wanted-language-want) 👀

<br>

## Python, pracovní prostředí


### Instalace

---

Na [tomto odkaze](https://www.python.org/downloads/) si vybereš verzi podle tvého operačního systému.

<br>

Opatrně, není *Python* jako *Python*.

Některé operační systémy (Linux, MacOS) mají velmi často **předem nainstalovaný Python se starší verzí (<2.7)**.

Díky těmto, dnes již [oficiálně neudržovaným verzím](https://www.python.org/downloads/release/python-2718/) , totiž běží některé původní procesy.

<br>

Ty budeš pracovat s verzemi **Pythonu 3.8+**, abychom si společně mohli ukázat všechny funkce a procesy, které ve starších verzích nefungovaly.

<br>

#### Co je to interpret?
Python je tzv. **interpretovaný jazyk**. Co to vůbec znamená?

<br>

Mezi hlavní výhody patří možnost spouštět stejný soubor na **různých operačních systémech** (jako *Windows*, *Linux*, *MacOS*). Stačí jazyk nainstalovat a můžete spouštět vaše soubory.<br>
Další výhodou je práce se soubory samotná. Stačí jej **otevřít**, **upravit** a můžete ho zase **používat i se všemi změnami**.

<br>

Práce s interpretovaným jazykem má ale i své **nevýhody**. Proces běží **pomaleji**, protože interpret převádí zápis čitelný lidskému oku na nuly a jedničky, kterým rozumí počítače.<br>
Současně vás Python sám neupozorní, že se mu nelíbí **nějaký chybný zápis**. To zjistíte až se objeví chyba po spuštění.

<br>

#### Interpret Pythonu? Ewww

---

Interpret si můžete představit jako nějaký program. Celý cyklus od zápisu, po jeho provedení probíhá následně:
1. Vytvoříme zdrojový kód v Pythonu (s příponou `.py`)
2. Spustíme jej pomocí interpretu Pythonu (standartní CPython)
3. Interpret řádek po řádku vytvoří tzv. bytecode z vašeho zdrojového kódu
4. Interpret pošle nově vytvořený bytecode do virtuálního stroje CPython
5. Ten vrací strojový kód, tedy nuly a jedničky přímo pro váš počítač

<img src="https://i.imgur.com/YXYOE9o.png" width="1000">


### Instalace, video

---


```python
from IPython.display import YouTubeVideo
YouTubeVideo('nzc8lCpWJhk', width=700, height=500)
```


### Spuštění, kontrola

---

V **terminálu** / **příkazovém řádku** napíšeš:
```
python --version  # python3 --version
```

<br>

Žádoucí výstup:
```
Python 3.8.XX
```

<br>

#### **Demo**: *příkazový řádek*  👀

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.3RX0BJUjo1iEcyFBi59JWQHaHa%26pid%3DApi&f=1" width="300" style="margin-left:auto; margin-right:auto" />

### Pracovní prostředí

---

Čtyři typy prostředí na úvod:
1. **Interpret** Pythonu, pro jednoduchá ohlášení, debugování, ověřování syntaxe,
2. **Editor** Pythonu, více ohlášení, delší i souvislejší zápis, jednoduchá rozšíření,
3. **IDE**, plnohodnotné prostředí (vcs, debugování, testování, DB viewer, posílání requestů),
4. **Notebook** Jupyter, není stavěný na vývoj, spíše demonstrativní prvky.

<br>

#### **Demo**: *pracovní prostředí*  👀

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.Xa4yjARXvRP3kQrezRoEKQHaEY%26pid%3DApi&f=1ipt=63f6a8a4954e1e0e99a260779ba2e4a5e6857b842334d5e7fc29c57abaf6cc1e&ipo=images" width="500" style="margin-left:auto; margin-right:auto" />

## První krůčky

---

Pro naučení jakéhokoliv **programovacího jazyka**, si potřebuješ osvojit znalosti z tzv. **tří teoretických pilířů**.

<br>

Na těchto pilířích stojí téměř všechny programovací jazyky:
1. **Syntaxe** (funkce, podmínky, smyčky, aj.)
2. **Datové typy** (čísla, sekvence, aj.)
3. **Knihovny** (decimal, aj.)

<br>


```python
# DEMO 1: terminal
# DEMO 2: module
```

### Zápis v notebooku
---


```python
print("Hello World")
```

    Hello World



```python
print(111 + 99)   # Tady procvičuji sčítání celých čísel
```

    210



```python
print(111+99)     # opět 210, ale bez mezer
```

    210



```python
# První poznámka
print(111 + 99)  # ..inline
# Druhá poznámka
print(111 + 100)
```

    210
    211



```python
111 + 99  
```




    210




```python
111 + 99, 111 + 100, 10+5
```




    (210, 211, 15)




```python
print(111 + 99)
print(111 + 100)
```

    210
    211


**Jednořádkové komentáře** ti pomohou vytvářet poznámky.

### Zápis v editoru
---

Pokud zapomeneš doplnit funkci `print`, potom ohlášení proběhne, ale neuvidíš výsledek.


```python
print(111 + 99)
```

#### **Demo**: *zápis, editor*  👀

<br>

## Číselné hodnoty

---

Mezi dva základní **datové typy**, které pracují s čísly Python rozděluje:
1. **Celá čísla**, tedy *integer* (`int`),
2. **desetinná čísla**, tedy *float* (`float`).

<br>


```python
5, 10, 0, -5, -10
```




    (5, 10, 0, -5, -10)




```python
5.0, 5.25, 5.5, 0.0, -5.5
```




    (5.0, 5.25, 5.5, 0.0, -5.5)




```python
# Vsechno je objekt. A kazdy objekt ma: datovy typ, hodnotu a id
type(210)  # datovy typ
```




    int




```python
210  # hodnota
```




    210




```python
id(210)
```




    139643962989328




```python
type(5.5)  # datovy typ
```




    float




```python
5.5  # hodnota
```




    5.5




```python
id(5.5)
```




    139643625560304



### Běžné aritmetické operace


```python
print(2 + 2)
print(10 - 6)
print(2 * 2)
print(56 / 13)
```

    4
    4
    4
    4.3076923076923075


<br>

### Méně známé ar. operace


```python
print(10 / 3)
```

    3.3333333333333335



```python
print(10 // 3)
```

    3



```python
print(10 / 4)
print(10 // 4)
```

    2.5
    2



```python
10 // 3
```




    3




```python
print(10 % 3)
```

    1



```python
print(11 % 3)
```

    2



```python
print(2 ** 2)  # sec.power 2^2
print(2 ** 5)  # 2^5
```

    4
    32


<br>

### 🧠 CVIČENÍ 1 🧠, číselné datové typy

---

Doplň, tak ať výstup odpovídá hodnotě v komentáři:


```python
print(10 ? 10)   #  = 100
print(9 ? 1)     #  = 8
print(121 ? 3)   #  = 40.333
print(2 ? 5)     #  = 32
print(17 ? 15)   #  = 2
print(56 ? 13)   #  = 4.3076
print(8 ? 8)     #  = 64
```

<details>
    <summary>▶️ Řešení</summary>
    
```python
print(10 * 10)   #  = 100
print(9 - 1)     #  = 8
print(121 / 3)  #  = 11.0
print(2 ** 5)    #  = 32
print(17 % 15)   #  = 2
print(56 // 13)  #  = 4
print(8 + 8.1)   #  = 16.1
```

</details>

<br>

### Potíž s typem float


```python
print(0.1 + 0.2)  # 0.2 + 0.1 --> 0.3
```

    0.30000000000000004



```python
# Float neni ani nekonecne velky ani nekonecny presny: takhle informace je zapsana
# v sys.float_info - min, max a epsilon 
# Epsilon je nejmensi rozdil mezi dvema cisly, ktery se da reprezentovat
import sys
sys.float_info
```




    sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)




```python
# Uvidime to i kdyz zkusime dva cisla s nejakym malym rozdilem porovnat: tady
# nam Python rika, ze 0.30000000000000004 je to stejny jako 0.30000000000000006,
# i kdyz my tam nejaky rozdil urcite vidime
# Python nemuze reprezentovat tak maly rozdil (epsilon)
0.30000000000000006 - 0.30000000000000004
```




    0.0



Občas se při práci s **desetinnými čísly** setkáš s fenoménem známým jako **plovoucí řádová čárka**.

Ten je způsobený tím, že některá desetinná čísla nemají odpovídající **binární tvar**. Proto jsou použity přibližné hodnoty.

<br>

Pro *přesnější práci* s desetinnými čísly vyzkoušej knihovnu **decimal**:


```python
# Knihovna decimal umozni vam presnejsi operaci pri praci s desetinnymi cisly:
# presto se nepouziva tak casto, jak byste si mohli predstavim. V drtive vetsine
# pripadu uvidite standardni float, kde staci jen si myslet na jeho nepresnost
# a s tim pocitat - pak se da pouzit u vetsiny programu a algoritmu.
# Samozrejme ale, pokud chcete napriklad odecitat stav uctu v bankovni aplikaci,
# asi chcete pouzit tu nejpresnejsi variantu, tj decimal ;)

import decimal

type(decimal.Decimal('0.1'))
```




    decimal.Decimal




```python
# POZOR: potrebujete do Decimal predavat string ('0.2'), aby to fungovalo tak, jak chcete.
# Pokud tam nahodou predate float, tak do Decimalu se zapise primo ta cela nepresna 
# float hodnota, a takovy zapis bude k nicemu, protoze vlastne vsechny problemy z floatu
# zustavaji pak bez zmen
decimal.Decimal(0.2)
```




    Decimal('0.200000000000000011102230246251565404236316680908203125')




```python
decimal.Decimal('0.2')
```




    Decimal('0.2')




```python
(decimal.Decimal('0.3') - decimal.Decimal('0.3'))
```




    Decimal('0.0')




```python
# Jak se da casto pracovat s floatem, aniz bychom to prevadeli na Decimal:
# muzeme pouzit zaokruhlovani
round(0.1 + 0.2, 3) - round(0.1 + 0.2, 3) 
```




    0.0



<br>

### Hierarchie matematických operátorů

---

Dávej pozor **na pořadí**, ve kterém interpret počítá s různými operátory.


```python
print(2 + 3 * 2)
```


| Pořadí | Operátor | Proces |
|:-:|:-:|:-|
| 1. | `()` | závorky |
| 2. | `**` | umocňování |
| 3. | `*` | násobení |
| 4. | `/` | dělení |
| 5. | `+` | sčítání |
| 6. | `-` | odčítaní |


```python
print((2 + 3) * 2)  # Upravím pořadí vyhodnocování
```


```python
# Bez zavorek se takove vyrazy strasne spatne ctou
2 + 3 * 2 - 2 ** 1 + 10 / 2
```


```python
# Mnohem lepe se to cte, kdyz prioritu oznacime pres zavorky
(2 + 3) * 2 - (2 ** 1) + (10 / 2)
```

## Textové hodnoty

---

**String**, tedy **řetězec** je různě dlouhé uskupení znaků (písmen, čísel, speciálních symbolů).

Ukázka datového typu `str`:


```python
print("Ahoj, tady Matous")
```


```python
# V Pythonu se da do stringu dat cokoliv co je v Unicode (google: "Unicode code points"),
# takze v podstate asi vsechno, co vam napadne: cinstina, japonstina, smajliky...
"汉语"
```


```python
print(type("Ahoj, tady Matous"))
```

    <class 'str'>


Dále se označuje jako **sekvence**, kterou jakmile jednou vytvoříme nelze změnit (z angl. *immutable*).


<br>

### Jak napsat string

---


```python
print('matous')
print("matous")
```

    matous
    matous



```python
print('matous")
```


```python
print('''matous''')  # speciální význam
print("""matous""")  # ...
```

    matous
    matous


<br>

### Opatrně na uvozovky


```python
# Opatrne: pokud pouzivate " na oznaceni zacatku stringu, tak pouziti " uvnitr 
# stringu vam jen uzavre string a vyvola chybu
"This is book is named "World""
```


```python
# Kdyz chci pouzit v textu ", tak pro oznaceni stringu tim padem pouziju ' 
'This is book is named "World"'
```


```python
print('zapisuji apostrof's')
```


```python
print("zapisuji apostrof's")
```


```python
print('zapisuji apostrof\'s')  # '\' -> escape char.
```

    zapisuji apostrof's



```python
print("zapisuji apostrof\'s")  # '\' -> escape char.
```

    zapisuji apostrof's



```python
"This is book is named \"World\""
```




    'This is book is named "World"'




```python
print("This is book is named \"World\"")
```

    This is book is named "World"


Použití **speciálních symbolů** souvisejících se zpětným lomítkem je víc. Jsou to tzv. **escape characters**. V tabulce níž najdeš soupis těch nejčastějších:

<br>

| Speciální znak | Význam |
| :-: | :-: |
| `\'` | Apostrof |
| \\ |	Zpětné lomítko |
| \n |	Nový řádek |
| \r |	*Return carriage* |
| \t |	Tabulátor |
| \b |	*Backspace* |
| \f |	*Form feed* |


```python
print("prvni radek\ndruhy radek")
```

    prvni radek
    druhy radek



```python
print("""prvni radek,
druhy radek.""")
```

    prvni radek,
    druhy radek.



```python
print('''
prvni radek,
druhy radek.
'''
)
```


```python
print("""prvni radek,
druhy radek.""")
```


```python
# Da se taky vickrat pouzit print(), ale je to
# zbytecne dlouhy kus kodu na neco tak jednoducheho
print("one line")
print() 
print()
print()
print("second line")
```

<br>

### Nemíchat různé datové typy

---


```python
print(2 + 2)      # int + int --> sčítání
```

    4



```python
print(2.0 + 2.0)      # float + float --> sčítání
```

    4.0



```python
"2" + "2"  # str + str --> concatenation
```




    '22'




```python
print(type("2" + "2"))
```

    <class 'str'>



```python
print(2 + "2")    # int + str
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[48], line 1
    ----> 1 print(2 + "2")    # int + str


    TypeError: unsupported operand type(s) for +: 'int' and 'str'



```python
print(2 + 2.0)    # int + float --> sčítání
```

    4.0



```python
print(2 + 2.0 + 1 + 1 + 1 + 1 + 1 - 1)    # int + float --> sčítání
```

    8.0


<br>

### Změna datového typu za jiný

---


```python
print(type("2"))
```

    <class 'str'>



```python
print(type(int("2")))       # řetězení zabudovaných funkcí
```

    <class 'int'>



```python
print(type(float("2")))     # ...
```

    <class 'float'>



```python
print(type(float(2)))
print(type(str(2.11)))
```

    <class 'float'>
    <class 'str'>



```python
str(2.11)
```




    '2.11'




```python
print(type(int("matous")))     # ne každou hodnotu lze "přetypovat"
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[53], line 1
    ----> 1 print(type(int("matous")))     # ne každou hodnotu lze "přetypovat"


    ValueError: invalid literal for int() with base 10: 'matous'



```python
int("t")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[61], line 1
    ----> 1 int("t")


    ValueError: invalid literal for int() with base 10: 't'



```python
print(type(int("2_000")))  
```

    <class 'int'>



```python
2_000_000
```




    2000000




```python
print(type(int("2 000")))  
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[60], line 1
    ----> 1 print(type(int("2,000")))  


    ValueError: invalid literal for int() with base 10: '2,000'



```python
print(1_000_000)               # pomocný oddělovač řádů
```

    1000000



```python
int("200"), int("2_000")
```




    (200, 2000)




```python
float("2,0")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[64], line 1
    ----> 1 float("2,0")


    ValueError: could not convert string to float: '2,0'



```python
int("2 000")
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[66], line 1
    ----> 1 int("2 000")


    ValueError: invalid literal for int() with base 10: '2 000'



```python
float("2.0"), float("2")
```




    (2.0, 2.0)



<br>

### Další procesy u stringů

---
Usnadňují další práci s datovým typem `str`:
1. Spojování,
2. opakování,
3. indexování,
4. slicing,
5. striding,
6. rozšiřující **metody**.


```python
# spojování ~ concatenation, bez třetího stringu
print("Matouš" + "Holinka")
```

    MatoušHolinka



```python
# spojování ~ concatenation, s třetím stringem
print("Matouš" + " " + "Holinka" + "!")
```

    Matouš Holinka!



```python
# opakování ~ repetition
print("#" * 5)
print("#" * 2)
```

    #####
    ##



```python
print("Ahoj!" * 5)
```

    Ahoj!Ahoj!Ahoj!Ahoj!Ahoj!



```python
print(5 * "Ahoj!")
```

    Ahoj!Ahoj!Ahoj!Ahoj!Ahoj!



```python
# ukázka, kde se mi převádění typů hodí
print(2024 - int("31"))
```

    1993



```python
str(2.0) + "ahoj"
```




    '2.0ahoj'




```python
"Ahoj" + "Petre!", "Ahoj " + " Petre!"
```




    ('AhojPetre!', 'Ahoj  Petre!')




```python
# indexování, první znak ze stringu
print("Matouš"[0])
```

    M



```python
# indexování, poslední znak ze stringu
print("Matouš"[-1])
```

    š



```python
"2024"[3]
```




    '4'




```python
# Pokud my zkusime ziskat symbol, ktery neexistuje (napriklad, symbol na indexu
# 10 v stringu s delkou 6), tak uvidime IndexError - chybu/vyjimku
"Matouš"[7]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[77], line 3
          1 # Pokud my zkusime ziskat symbol, ktery neexistuje (napriklad, symbol na indexu
          2 # 10 v stringu s delkou 6), tak uvidime IndexError - chybu/vyjimku
    ----> 3 "Matouš"[7]


    IndexError: string index out of range



```python
# To stejny kdyz my zkusime ziskat 10 symbol od konce ve stringu s delkou 6
print("Matouš"[-8])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[80], line 2
          1 # To stejny kdyz my zkusime ziskat 10 symbol od konce ve stringu s delkou 6
    ----> 2 print("Matouš"[-8])


    IndexError: string index out of range



```python
# POZOR: kdyz string ma delku 6, tak to znamena, ze spravny muze byt jen
# index v rozmezi 0 az 5, index 6 jiz neexistuje
print("Matouš"[6])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[69], line 3
          1 # POZOR: kdyz string ma delku 6, tak to znamena, ze spravny muze byt jen
          2 # index v rozmezi 0 az 5, index 6 jiz neexistuje
    ----> 3 print("Matouš"[6])


    IndexError: string index out of range



```python
# Pokud mame zaporny index v stringu s delkou 6: spravny index je od -1 do -6,
# ale index -7 uz neexistuje
"Matouš"[-7]
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[70], line 3
          1 # Pokud mame zaporny index v stringu s delkou 6: spravny index je od -1 do -6,
          2 # ale index -7 uz neexistuje
    ----> 3 "Matouš"[-7]


    IndexError: string index out of range



```python
# Index muze byt jen cele cislo
"Matouš"[-7.0]
```

    <>:2: SyntaxWarning: str indices must be integers or slices, not float; perhaps you missed a comma?
    <>:2: SyntaxWarning: str indices must be integers or slices, not float; perhaps you missed a comma?
    /tmp/ipykernel_225427/211257573.py:2: SyntaxWarning: str indices must be integers or slices, not float; perhaps you missed a comma?
      "Matouš"[-7.0]
    /tmp/ipykernel_225427/211257573.py:2: SyntaxWarning: str indices must be integers or slices, not float; perhaps you missed a comma?
      "Matouš"[-7.0]
    /tmp/ipykernel_225427/211257573.py:2: SyntaxWarning: str indices must be integers or slices, not float; perhaps you missed a comma?
      "Matouš"[-7.0]



    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[82], line 2
          1 # Index muze byt jen cele cislo
    ----> 2 "Matouš"[-7.0]


    TypeError: string indices must be integers



```python
# Casto chceme ziskat taky nejen jeden symbol, ale nejakou cast stringu,
# na tohle muzeme pouzit slicing: zase mame [], tentokrat ale tam mame
# dva cisla: zacatek a konec slicu. 
# POZOR: tady symbol na indexu 1 bude ve vysledku, ale symbol na indexu
# 6 uz tam nebude - posledni bude index PRED 6, tj 5.
# [1, 6) - vcetne 1, ne vcetne 6
# Proc to je takhle? Pokud pak od druheho indexu odecteme prvni, tak 
# takhle jednoduse ziskame delku vysledku (casto to potrebujeme)
print("matous.holinka@gmail.com"[1:6])  # (6-1) == 5  -> delka
```

    atous



```python
print("matous.holinka@gmail.com"[0:6])  # (6-0) == 6 -> delka
```

    matous



```python
# Zapis [:6] znamena to stejny co [0:6]: defaultne start je 0, takze vezmeme
# string od zacatku a do stop indexu (ne vcetne)
print("matous.holinka@gmail.com"[:6])
```

    matous



```python
# Naopak pokud nenapiseme druhy index, tak to bude znamenat, ze vezmeme
# string od startu az do konce (vcetne posledniho symbolu)
print("matous.holinka@gmail.com"[6:])
```

    .holinka@gmail.com



```python
len("matous.holinka@gmail.com")
```




    24




```python
# Funguje i pro zaporne symbolu: od zacatku do symbolu na indexu -3 (NE vcetne)
print("matous.holinka@gmail.com"[0:-3])
```

    matous.holinka@gmail.



```python
# Zapis [:] znamena zaroven defaultni start a defaultni stop, tj od
# zacatku do konce (u stringu ale neni uzitecne)
print("matous.holinka@gmail.com"[:])
```

    matous.holinka@gmail.com



```python
# Rozsirime to dal a pouzijeme striding (stride = krok): defaultne 
# totiz je 1, coz znamena, ze bereme kazdy symbol. Takze [:] a 
# [::1] nam vrati stejne vysledky. 
print("12345678901"[::1])
```

    12345678901



```python
# My muzeme ale zmenit krok: napriklad, [::2] nam vrati kazdy druhy symbol
print("1234567890"[::2])
```

    13579



```python
print("1234567890"[::4])  # kazdy ctvrty symbol
```

    159



```python
# Pokud krok je prilis velky, tak ziskame jen symbol na indexu start
# a pak uz nic - chyba tam ale nebude
print("1234567890"[::400])
```

    1



```python
"matous.holinka@gmail.com"[::-1]
```




    'moc.liamg@akniloh.suotam'




```python
# Zajimavy je ze i krok/stride muze byt zaporny: pak vysledek bude otoceny
# POZOR: v takove situaci start musi byt betsi nez stop
# Tady: od 14 (vcetne) do 0 (NE VCETNE!!! stop vzdycky ne vcetne, pokud je zadany) 
# zprava doleva s krokem -1
"matous.holinka@gmail.com"[:0:-1]
```




    'moc.liamg@akniloh.suota'




```python
# Pokud to popletu a napisu start menzi nez stop, jak u kladneho kroku, tak vysledek bude
# vzdycky prazdny string
"matous.holinka@gmail.com"[0:4:-1]
```




    ''




```python
# Pokud chci i prvni symbol, tak zadny stop tam nedam: tohle znamena
# od 14 (vcetne) do zacatku (vcetne symbolu na pozici 0) zprava doleva s krokem -1
"matous.holinka@gmail.com"[14::-1]
```


```python
# Pokud chci jen otocit posloupnost hodnot: od konce do zacatku zprava doleva
"matous.holinka@gmail.com"[::-1]
```




    'moc.liamg@akniloh.suotam'




```python
# Zaporny krok nemusi byt jen -1: 
# od 14 (vcetne) do 0 (NE VCETNE) zprava doleva s krokem -2
"matous.holinka@gmail.com"[14:0:-2]
```


```python
# Shrnuti:
# index
"123"[0]  # ---> jeden symbol "1"
# slice 
"123"[1:3]  # ---> vic symbolu "23" 
# stride
"123456"[::2] # ---> "135", kazdy druhy
# slice + stride 
"123456"[1:6:2] # ---> "246", kazdy druhy od 1 (vcetne) do 6 (ne vcetne)
```

### 🧠 CVIČENÍ 2 🧠, stringy

---

Doplň, tak ať výstup odpovídá hodnotě v komentáři:


```python
# Najdi a vypiš písmeno "u"
print("Matouš")
```


```python
# Najdi a vypiš poslední znak
print("Matouš")
```


```python
# Najdi a vypiš "matous"
print("matous.holinka@gmail.com")
```


```python
# Najdi a vypiš všechny sudé číslice (bez nuly)
print("1234567890")
```


```python
# Spoj a vypiš "Matouš" a "Holinka" pomocí mezery
print("Matouš" + "Holinka")
```


```python
print("Matous"[10])
```


    ---------------------------------------------------------------------------

    IndexError                                Traceback (most recent call last)

    Cell In[107], line 1
    ----> 1 print("Matous"[10])


    IndexError: string index out of range



```python
print("Matous"[3:100])
```

    ous



```python
len("Matous")
```




    6



<details>
    <summary>▶️ Řešení</summary>
    
```python
print("Matouš"[4])
print("Matouš"[-1])
print("matous.holinka@gmail.com"[:6])
print("1234567890"[1:-2:2])
print("Matouš" + " " + "Holinka")
```

</details>

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.k1p6JyN8Tr1Yya7R6T0YPQHaHl%26pid%3DApi&f=1" width="250" style="margin-left:auto; margin-right:auto" />



## Proměnná v Pythonu

---

Pokud máš objekty, které chceš použít **více než jedenkrát**, **ulož je** do proměnné.

Pokud chceš hodnotu použít **pouze jednou**, **nemusíš ji ukládat**.

<br>

### Standardní zápis proměnné s hodnotou

---

Pokud chceš interpretovi oznámit, že chceš objekt schovat na později, učiníš tak pomocí symbolu `=`:
    


```python
jmeno = "Matouš"
vek = 55
```


```python
print(jmeno, vek)
```

    Matouš 55



```python
moje_cislo = 11
print(moje_cislo)
```

    11



```python
moje_cislo = "11"
print(moje_cislo)
```

    11


Označení `jmeno, vek` jsou jen **jména, označení, identifikátory**, které označí hodnoty `"Matous"` a `55` u tebe v paměti.

### Pravidla pro pojmenování objektů

---

Jméno proměnné (někdy také odkaz) **může obsahovat** tyto znaky:
1. **Písmenné** znaky,
2. **Číselné** znaky,
3. **Podtržítka**.


```python
jmeno   = "Matous"
jmeno2  = "Matous"
jmeno_2 = "Matous"
```

Existují ovšem znaky, které jméno proměnné **obsahovat nesmí**:
1. Jméno proměnné nesmí **začínat číselným znakem**,
2. jméno proměnné nesmí **obsahovat speciální znaky** (kromě podtržítka),
3. jméno proměnné nesmí **obsahovat mezery**.

Obvykle se nedoporučuje začínat jména **odkazů** pomocí **podtržítka** (pokud nevíš proč to dělat, raději to nedělej):


```python
1jmeno = "Matous"
```


      Cell In[78], line 1
        1jmeno = "Matous"
         ^
    SyntaxError: invalid imaginary literal




```python
jmeno@ = "Matouš"
```


      Cell In[79], line 1
        jmeno@ = "Matouš"
               ^
    SyntaxError: invalid syntax




```python
moje jmeno = "Matous"
```


      Cell In[80], line 1
        moje jmeno = "Matous"
             ^
    SyntaxError: invalid syntax



<br>

Dále nepoužívej pro jméno proměnné žádný **z rezervovaných klíčových slov**:


```python
moje_cislo = 11 
moje_cislo = "11"
```


```python
# Špatně
print = "Matous"
print("M")
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[81], line 3
          1 # Špatně
          2 print = "Matous"
    ----> 3 print("M")


    TypeError: 'str' object is not callable



```python
# Správně
name = "Matous"
print(name)
```

    Matous


<br>

Pokud potřebuješ použít klíčový výraz **jako jméno proměnné**, můžeš použít podtržítko **jako příponu**:


```python
# Správně
str_ = "Matous"
print(str_)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    Cell In[83], line 3
          1 # Správně
          2 str_ = "Matous"
    ----> 3 print(str_)


    TypeError: 'str' object is not callable


<br>

### Forma zápisu

---
Je jedno, jestli preferuješ tzv. `camelCase` nebo `snake_case`. Důležité je konzistentní používání skrz celý tvůj zápis.


```python
moje_datum_narozeni = ...
mojeDatumNarozeni = ...
```


```python
dorucovaci_adresa = "U Potoka 11"
```

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.XikDkNKNuZHeuGBWc1KgcQHaGf%26pid%3DApi&f=1" width="400" style="margin-left:auto; margin-right:auto" />

## Sekvence list, tuple

---
Doposud jsme si ukázali jak pracovat **s jednou hodnotou** (`int`, `float`, `str`).

<br>

V Pythonu můžeš ale sdružovat **více hodnot** společně. Na jednom místě.

<br>

Takové hodnoty potom budeme označovat jako tzv. **sekvenční datové typy** (tedy několik údajů oddělených *oddělovačem*).
1. `list` (z angl. *list*, česky *seznam*),
2. `tuple` (z angl. *tuple*, česky *n-tice*),
3. `range` (z angl. *range*, česky *rozsah*) - na něj přijde řada později.


```python
jmeno = "Matouš"
```


```python
print(jmeno)
```

    Matouš


### List

---
*List* je první *sekvenční* datový typ. Poznáš jej podle:
1. **hranatých závorek**,
2. oddělovačem **je čárka**,
3. jeho obsah (uvnitř závorek) můžeš po vytvoření **změnit** (přidávat a odebírat).

```python
["Matous", "Marek", "Lukas", "Jan"]
```


```python
["Matous", "Marek", "Lukas", "Jan"]  
# pokrocile: numpy
```




    ['Matous', 'Marek', 'Lukas', 'Jan']




```python
["Matous", 1.0, 1]
```




    ['Matous', 1.0, 1]




```python
print(type(["Matous", "Marek", "Lukas", "Jan"]))
```

    <class 'list'>


### Tuple

---
*Tuple* je druhý *sekvenční* datový typ. Poznáš jej podle:
1. **kulatých závorek** (může být i bez závorek),
2. oddělovačem **je čárka**,
3. jeho obsah (uvnitř závorek) **nemůžeš** po vytvoření změnit.

```python
("Matous", "Marek", "Lukas", "Jan")
```


```python
("Matous", 1.0, 1)
```




    ('Matous', 1.0, 1)




```python
print(type(("Matous", "Marek", "Lukas", "Jan")))
```

    <class 'tuple'>


### Nový list, nový tuple
---

##### List


```python
print(type([]))
print(type(list()))
```

    <class 'list'>
    <class 'list'>



```python
muj_seznam = []
```


```python
list()
```




    []



##### Tuple


```python
print(type(()))
print(type(tuple()))
```

    <class 'tuple'>
    <class 'tuple'>



```python
print(type(("hr", "admin", "development", "qa")))
```

    <class 'tuple'>


### Jak s listem pracovat

---
Podobně jako u typu `str`, můžeš s `list` pracovat hned několika způsoby:
1. Spojování,
2. opakování,
3. indexování,
4. slicing,
5. striding.

<br>

### Jak pracovat s tuplem

---
Podobně jako u typu `list`, můžeš s `tuple` pracovat hned několika způsoby:
1. Spojování,
2. opakování,
3. indexování,
4. slicing,
5. striding.

<br>

### Spojování

---


```python
# LIST
print(["Matous", "Lukas"] + ["Petr", "Jan"])
```

    ['Matous', 'Lukas', 'Petr', 'Jan']



```python
# TUPLE
muj_novy_tuple = ("a", "b") + ("c", "d")
print(muj_novy_tuple)
```

    ('a', 'b', 'c', 'd')


<br>

### Opakování

---


```python
# LIST
print(["@"] * 3)
```

    ['@', '@', '@']



```python
# LIST
print(["@", "!"] * 3)
```

    ['@', '!', '@', '!', '@', '!']



```python
# TUPLE
print(("@",) * 3)
```

    ('@', '@', '@')



```python
# TUPLE
print(("@",) * 3)
```

    ('@', '@', '@')



```python
# TUPLE
print(type(("@",)))
```

    <class 'tuple'>



```python
print(("@", "!") * 3)
```

    ('@', '!', '@', '!', '@', '!')


<br>

### 🧠 CVIČENÍ 3 🧠, list & tuple

---

Doplň, tak ať výstup odpovídá hodnotě v komentáři:


```python
# Najdi a vypiš hodnotu ze sekvence "Lukas"
print(["Matous", "Lukas", "Petr", "Jan"][1])
```

    Lukas



```python
# Najdi a vypiš hodnoty ze sekvence "Lukas" a "Petr"
print(("Matous", "Lukas", "Petr", "Jan")[1:3])
```

    ('Lukas', 'Petr')



```python
# najdi a vypiš hodnoty ze sekvence 'Lukas', 'Jan'
# ..pomocí jedné hranaté závorky
print(["Matous", "Lukas", "Petr", "Jan"][1::2])
```

    ['Lukas', 'Jan']


<details>
    <summary>▶️ Řešení</summary>
    
```python
print(["Matous", "Lukas", "Petr", "Jan"][1])
print(("Matous", "Lukas", "Petr", "Jan")[2:4])
print(["Matous", "Lukas", "Petr", "Jan"][1:4:2])
```

</details>

<br>

## Úvod do funkcí
---

Obecně řečeno Python disponuje dvěma typy funkcí. Tebe budou zajímat:
1. **Zabudované funkce** (~*built-in functions*),
2. **Uživatelské funkce** (~*user-defined functions*) - ty přijdou na řadu později.

<br>

Funkce jsou v podstatě **pomocné nástroje**, které ti umožní snazší a efektivnější práci.

To, že nesou označení **zabudované** znamená, že je máš k dispozici ihned po instalaci. Tedy v každém souboru (s příponou `.py`), který do budoucna vytvoříš.

<br>

### Použití zabudované funkce

---

| Jméno funkce | Účel funkce |
| :-: | :- |
| `type` | Vrací datový typ zadané hodnoty |
| `str` | Vrací *string* ze zadané hodnoty |
| `list` | Vrací nový objekt, sekvenční datový typ *list* |
| `tuple` | Vrací nový objekt, sekvenční datový typ *tuple* |
| `help` | Vratí nápovědu k zadanému objektu |
| `print` | Vypisuje zadné hodnoty jako výstupy |
| `input` | Umožňuje ukládat vstupy od uživatele |

<br>

Pokud máš se zabudovanými funkcemi nějaké zkušenosti, nebo tě zajímá, které další bys mohl v rámci Pythonu využít, mrkni na [oficiální tabulku](https://docs.python.org/3/library/functions.html) všech zabudovaných funkcí.


```python
("Filip", 23, "programator")
```


```python
help(input)
```

    Help on method raw_input in module ipykernel.kernelbase:
    
    raw_input(prompt='') method of ipykernel.ipkernel.IPythonKernel instance
        Forward raw_input to frontends
        
        Raises
        ------
        StdinNotImplementedError if active frontend doesn't support stdin.
    


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.GMJvJ-GG0YS8H5JmHR3CbwHaHm%26pid%3DApi&f=1" width="400" style="margin-left:auto; margin-right:auto">


## Domácí úkol

---

Představ si situaci, že chceš napsat takový program, který ti umožní rezervovat jízdenky.

Samozřejmě nepůjde o žádnou produkční verzi ale **jednoduchý skript** postavený na komunikaci *uživatele* a *interpretu*.

<br>

Program bude umět:

1. **Pozdravit** uživatele,
2. **Vypsat** nabídku,
3. Dovolit uživateli **zadat vstupní data**,
4. **Zpracovat** vstupní data,
5. **Vypsat** zpracovaná data.

### 1/6 Vstupní údaje

---


```python
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
```

### 2/6 Pozdrav uživatele

---

Očekávaný výstup:

```
VITEJTE U NASI APLIKACE DESTINATIO!
===================================
```


```python
# Zapiš pozdrav a odděl jej pomocnou proměnnou
```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
cara = "=" * 35

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)
```
</details>

### 3/6 Vypsání nabídky

---

Očekávaný výstup:

```
VITEJTE U NASI APLIKACE DESTINATIO!
===================================
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180

```


```python
# Vypiš nabídku cílových destinací a odděl ji pomocnou proměnnou
```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
cara = "=" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)
print(nabidka)
print(cara)
```
</details>

### 4/6 Zadání vstupních dat od uživatele

---

Očekávaný výstup:

```
<predchozi_ukoly>
===================================
CISLO DESTINACE: 1
JMENO: Matous
PRIJMENI: Holinka
EMAIL: matous@matous.cz
===================================
```


```python
# Dovol uživateli zadat 'destinace', 'cele_jmeno', 'email', 'rok_narozeni' a doplň oddělovač
```

**Opatrně!** nezapomeň na to, jaký **datový typ** používáš.

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
cara = "=" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)
print(nabidka)
print(cara)

destinace = input("CISLO DESTINACE:")
jmeno = input("JMENO:")
prijmeni = input("PRIJMENI:")
email = input("EMAIL:")
print(cara)
```
</details>

### 5/6 Zpracování dat

---

Očekávaný výstup:

```
<predchozi_ukoly>
===================================
CISLO DESTINACE: 2
===================================
Viden
200
===================================
```


```python
# Zkus propojit stávající datový typ "mesta" a "destinace"
```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)
print(nabidka)
print(cara)

destinace = input("CISLO DESTINACE:")

spravna_destinace = mesta[int(destinace) - 1]
cena = ceny[int(destinace) - 1]
print(cara)
```
</details>

### 6/6 Výpis zpracovaných hodnot

---

Očekávaný výstup:

```
VITEJTE U NASI APLIKACE DESTINATIO!
===================================
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
===================================
CISLO DESTINACE: 2
JMENO: Matous
PRIJMENI: Holinka
EMAIL: matous@matous.cz
===================================
DEKUJI, Matous ZA OBJEDNAVKU,
CIL. DESTINACE: Viden, CENA JIZDNEHO: 200,
NA TVUJ MAIL matous@matous.cz JSME TI POSLALI LISTEK.
===================================
```


```python
# Vypiš tyto informace pro objednávajícího uživatele
# - Kdo si objednal,
# - kam cestuje a za kolik,
# - kam mu přijde lístek.
```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """
1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""

print("VITEJTE U NASI APLIKACE DESTINATIO!")
print(cara)
print(nabidka)
print(cara)

destinace = input("CISLO DESTINACE:")
jmeno = input("JMENO:")
prijmeni = input("PRIJMENI:")
email = input("EMAIL:")
print(cara)

spravna_destinace = mesta[int(destinace) - 1]
cena = ceny[int(destinace) - 1]

print(f"""DEKUJI, {jmeno} ZA OBJEDNAVKU,
CIL. DESTINACE: {spravna_destinace}, CENA JIZDNEHO: {cena},
NA TVUJ MAIL {email} JSME TI POSLALI LISTEK.""")
```
</details>

➡️ ➡️ **Formulář pro Tvoje hodnocení** [**první lekce**](https://forms.gle/Rr5shgG77Xw6JTGXA) ⬅️ ⬅️


---
