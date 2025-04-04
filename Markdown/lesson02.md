# Python akademie

---

<br>

## Obsah lekce

---

1. [Rozhodování](#Rozhodování),
2. [Datový typ boolean](#Datový-typ-bool-(~boolean)),
3. [Operace s boolean](#Operace-související-s-dat.-typem-bool),
4. [Jednoduchý podmínkový zápis](#Jednoduchý-podmínkový-zápis),
5. [Rozvinutý podmínkový zápis](#Rozvinutý-podmínkový-zápis),
6. [Ternární operátor](#Ternární-operátor),
7. [Metody](#Metody),
8. [Domácí úkol](#Domácí-úkol).

---

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.yLOyM3kOmMLeoCCP47fziQHaHa%26pid%3DApi&f=1" width="300" style="margin-left:auto; margin-right:auto" />

## Rozhodování

---

Jeden ze **základních algoritmů**, který programátor (..a nejen on) musí znát, je naučit náš skript se sám **rozhodovat**.

<br>

### Praktické situace

1. Uživatel Matouš **není plnoletý**. Proto mu **omezím přístup** k naší aplikaci.
```python
jmeno = "Matous"
vek = 11
# Jak uživateli Matouš omezím přístup?
```

<br>

2. Potřebuji ověřit, jestli zadané jméno **patří k zaměstnancům** firmy.
```python
zamestnanci = ("Ladislav Dvořák", "Nikola Lehká", "Jitka Adamová")
cele_jmeno = "Ladislav Dvořák"
# Jak potvrdím, že osoba Ladislav Dvořák je zaměstnanec?
```

<br>

3. Co když budu chtít přidat novou tabulku do DB a tabulka **již existuje**?
```python
soupis_tabulek = ["users", "models", "employees"]
jmeno_tabulky = "employees"
# Jak potvrdím, že tabulka employees již je součástí seznamu?
```

<br>

Jak řešit tyto a podobné otázky se dozvíš dále.

Budeš k tomu potřebovat další datový typ **boolean** a s ním související **podmínkový zápis**.


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.6naTquItTnMaoNEZW-MPPQHaHa%26pid%3DApi&f=1" width="300" style="margin-left:auto; margin-right:auto"/>

## Datový typ `bool` (~boolean)

---

**Boolean** vychází z datového typu `integer` (~z celých čísel) a nabývá pouze **dvou hodnot**:
* `True` (odpovídá hodnotě `1`),
* `False` (odpovídá hodnotě `0`).

Tento **datový typ** pomáhá *rozhodovat*, jestli je celý **zápis** (ohlášení) či **hodnota**(výraz) pravdivý a nebo nepravdivý.

<br>


```python
vek = 11             # int
jmeno = "Matous"     # str
je_plnolety = False  # bool
```


```python
print(type(je_plnolety))
```

    <class 'bool'>


<br>

### Funkce `bool`

---

Tato *zabudovaná funkce* Ti pomůže lépe pochopit práci s datovým typem `bool` a co je pravdivé či nikoliv.

<br>

Funguje jako nějaký **rozhodčí**, kterému zadáš **hodnotu** a funkce ji *ohodnotí*, jestli je **pravdivá** nebo **nepravdivá**.


```python
print(bool(1))
```

    True



```python
print(bool(0))
```

    False


<br>

### Funkce `bool` a jiné datové typy

---


```python
print(bool(2))
print(bool("Matous"))
print(bool(2.5))
print(bool(["a", "b"]))
```

    True
    True
    True
    True



```python
print(bool(""))
print(bool([]))
print(bool(()))
print(bool(None))
```

    False
    False
    False
    False


`None` v Pythonu používáme pro označení **absence hodnoty** (*odkaz* nemá hodnotu). V jiných jazycích třeba `Null`, `NaN`.

<br>

##### Verdikt

<br>

| Hodnota | Vyhodnocení funkcí `bool`|
|:-:|:-:|
|`2`| `True` |
|`"Matous"`| `True` |
|`2.5`| `True`|
|`[]`|`False`|
|`""`| `False`|
|`None`| `False`|

<br>

Můžeš tedy prohlásit, že pokud použiješ **neprázdnou hodnotu** (`str`, `int`, `list`, aj.), funkce `bool` vypíše hodnotu `True`.

V opačném případě dostaneš `False`.

<br>

Teď, když víš, jakým způsobem Python pracuje s datovým typem *boolean* uvidíš, kde všude toho využiješ.

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.jcR4ASfryZwpiwc6WTRvyQHaHa%26pid%3DApi&f=1&ipt=b7026ac0b680ab9052a70cb4b2057fb60daf6c6e73133cf43c074210414992c8&ipo=images" width="300" style="margin-left:auto; margin-right:auto"/>

## Operace související s dat. typem `bool`

---

1. Srovnávací operace,
2. *boolean* operace,
3. srovnávání *identit* objektů,
4. *membership testing*.


<br>

### 1. Srovnávácí operace

---

<br>

| Operátor | Význam |
|:-:|:-|
| `<` | menší než |
| `>` | větší než |
| `<=` | menší nebo rovno |
| `>=` | větší nebo rovno |
| `==` | rovnost |
| `!=` | nerovnost |


```python
print(bool(144 > 1))     # True
print(bool(144 == 142))  # False
print(bool(144 != 100))  # True
```

    True
    False
    True



```python
print(144 > 1)      # True, funguje také bez funkce "bool"
print(144 == 142)   # False
print(144 != 100)   # True
```

    True
    False
    True


### 2. Boolean operace

---

<br>

*Operátory* sloužící **ke spojování** několika *srovnání* nebo *výrazů* (*vypsané podle rostoucí důležitosti*):
1. `or`
2. `and`,
3. `not`.

<br>

##### Operátor `and`

---


```python
print(bool(True and True))  # opět možnost nepoužít funkci bool()
print(bool(True and False))
print(bool(False and False))
```

    True
    False
    False



```python
print(bool(True and True and True))
print(bool(True and True and True and False))
```

    True
    False


Pokud použiješ **boolean operátor** `and` a od jednotlivých výroků získáš byť jednu hodnotu `False`, **celý výsledek** bude **nepravdivý** (`False`).

<br>

Dále můžeš aplikovat princip tzv. *zkráceného vyhodnocování*. Pokud uvidíš jako první hodnotu `False` (a pracuji s operátorem `and`), nemusíš procházet dálší výrazy. Výsledek je `False`.

<br>

##### Operátor `or`

---


```python
print(bool(True or False))
print(bool(False or True))
print(bool(False or False))
print(bool(True or True))
```

    True
    True
    False
    True



```python
print(bool(False or False or False))
print(bool(False or False or True))
```

    False
    True


Pokud použiješ **boolean operátor** `or` a od jednotlivých výroků získáš byť jednu hodnotu `True`, **celý výsledek** bude **pravdivý** (`True`).

<br>

Opět lze použít princip *zrychleného vyhodnocování*. Tedy pokud funkce `bool` vrátí aspoň jednu hodnotu `True` (a pracuji s operátorem `or`), výsledek celého zápisu bude `True`.

<br>

##### Operátor `not`

---


```python
print(bool(not True))
print(bool(not False))
```

    False
    True


Při použití operátoru `not` získáš obrácenou hodnotu.

<br>

Pokud potřebuješ **spojit** více porovnávání hodnot, můžeš je doplnit o *boolean operace*.


```python
print(bool(False and False or True))  # výsledek?
```

    True



```python
print(1 < 5 and 5 > 10)               # True and False --> False
```

    False


Ovšem dávej pozor na **důležitosti jednotlivých operátorů**. Srovnávací operátory mají totiž vyšší prioritu než boolean operátory, proto dojde nejprve k jejich vyhodnocení.

<br>

Pro lepší názornost můžeš použít **kulaté závorky**.

Pokud potřebuješ **současně spojuješ** pomocí `and` a v obou výrazech je stejná hodnota, můžeš zápis zkrátit:


```python
print(1 < 5 and 5 > 10)  # původní zápis
print(1 < 5 > 10)        # zkrácený zápis
```


```python
print(1 < 2 and 2 < 3 and 3 < 4)  # původní zápis
print(1 < 2 < 3 < 4)              # zkrácený zápis
```

<br>

### 3. Srovnání identit objektů


---

<br>

| Operátor | Význam |
| :-: | :-: |
| `is` | totožná identita |
| `is not` | různá identita |

<br>

Každý objekt má svůj **identifikátor** (~číslo, poznávací značku).

<br>

Tento **identifikátor** můžeš vypsat pomocí *zabudované funkce* `id`:


```python
print(id("a"))
```

    140156869520048



```python
jmeno_1 = "Matous"
jmeno_2 = "Lukas"
```


```python
prijmeni_1 = "Holinka"
prijmeni_2 = "Holinka"
```


```python
print("Matous:\t" + str(id(jmeno_1)))
print("Lukas: \t" + str(id(jmeno_2)))
```

    Matous:	140156728432432
    Lukas: 	140156728497264



```python
print("Holinka: " + str(id(prijmeni_1)))
print("Holinka: " + str(id(prijmeni_2)))
```

    Holinka: 140156728498800
    Holinka: 140156728498800


▶️ **pozn.** Jde o tzv. <a href="https://stackabuse.com/guide-to-string-interning-in-python/" target="_blank">*string interning*</a>, tedy koncept, který souvisí s tím, že je string **nezměnitelný datový typ**.

<img src="https://i.imgur.com/mXZ8xXj.png" title="source: imgur.com" width="1000" style="margin-left:auto; margin-right:auto"/>

Dále *internování* znamená, že pokud vytvoříš **dva stejné stringy** `"Holinka"`, *interpret* zařídí, že **pouze jeden** se alokuje do paměti a druhý pouze ukazuje na stejné místo (číslo).


```python
jmeno_1 = "Matous"
jmeno_2 = "Lukas"
```


```python
prijmeni_1 = "Holinka"
prijmeni_2 = "Holinka"
```


```python
print(bool(jmeno_1 is jmeno_2))
```

    False



```python
print(bool(prijmeni_1 is prijmeni_2))
```

    True


<br>

### 4. Membership testing (~Ověření členství)


---

Nejde o proces, který by přímo pracoval s `bool` hodnotami.

Ovšem právě `True` a `False` jsou hodnoty, které jsou **výsledkem toho procesu**.

<br>



```python
print(bool("m" in "Matous"))  # False
print(bool("M" in "Matous"))  # True
```

    False
    True



```python
print("m" in ("a", "n", "c", "ma"))  # False
print(bool("M" in ("P", "Q", "M")))  # True
```

    False
    True


Opět si můžeš všimnout **rezervovaného slova** `in`, které je pro **membership testing** typické.

V podstatě se ptáš, jestli je výraz **na levé straně** součásti výrazu **na pravé straně**.

<br>

**Ověření členství** je ve skutečnosti proces, který obecně zařazujeme mezi operace jako *indexing*, *slicing*, *striding*. Resp. operace, které můžeme provádět se **sekvencemi**.

<br>

#####  `is` nebo `==` ?

<br>

Opatrně na aplikaci operátorů porovnávání **identit** a **hodnot**:
* `==` a `!=` **porovnávají hodnotu**,
* `is` a `is not` porovnávají, jestli dvě proměnné ukazují v paměti počítače **na stejný objekt**.


```python
muj_seznam_1 = [1, 2, 3]
muj_seznam_2 = [1, 2]
```


```python
print(muj_seznam_1 == muj_seznam_2)  # [1, 2, 3] != [1, 2]
```

    False



```python
muj_seznam_3 = [1, 2, 3]
muj_seznam_4 = [1, 2, 3]
```


```python
print(muj_seznam_3 == muj_seznam_4)  # [1, 2, 3] == [1, 2, 3]
```

    True



```python
print(id(muj_seznam_3))
print(id(muj_seznam_4))
```

    140156241530560
    140156241538880



```python
print(muj_seznam_3 is muj_seznam_4)  # ?
```

    False



```python
muj_seznam_5 = []
muj_seznam_6 = []
```


```python
print(id(muj_seznam_5))
print(id(muj_seznam_6))
```


```python
muj_seznam_7 = ()  # 140179552598144
muj_seznam_8 = ()  # 140179546821440
```


```python
print(id(muj_seznam_7))
print(id(muj_seznam_8))
```

Použití datového typu *boolean* nesouvisí pouze s těmito procesy, ale také s tvorbou **rozhodovacích procesů**.

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.-i3k3_zQEjLhFLuMGEW5NAHaHZ%26pid%3DApi&f=1&ipt=1cd115c93942aa169dd40aa5a11f192af6a24b0975c0797ca2dc7bc0ab5b4a56&ipo=images" width="300" style="margin-left:auto; margin-right:auto"/>

## Jednoduchý podmínkový zápis

---

**Podmínkový zápis** je proces, který budeš potřebovat, pokud budeš chtít, aby **tvůj skript** sám rozhodoval.


V Pythonu můžeš rozhodování zapsat pomocí tzv. *podmínkového zápisu*, který začíná rezervovaným výrazem `if`. 

Velkou výhodou oproti jiným programovacím jazykům, je možnost **nepsat závorky** (jak tomu je u *Javy*, *R* aj.).

<br>

##### Předpis pouze s klíč. slovem `if`


```python
if True:
    print("Ahoj, Matouši!")

print("Pokračuji..")
```

    Ahoj, Matouši!
    Pokračuji..



```python
if False:  # 18 != 11 --> False
    print("Ahoj, Matouši!")

print("Pokračuji..")
```

    Pokračuji..



```python
vek = 21
```


```python
if vek > 18:
    print("Ahoj, Matouši!")

print("Pokračuji..")
```

    Ahoj, Matouši!
    Pokračuji..



```python
if vek > 18:
    print("Ahoj, Matouši!")

print("Pokračuji..")
```

*Interpret* se podívá na **výraz** (v záhlaví) a pokud jej vyhodnotí **jako pravdivý** (`True`), **provede odsazený řádek** pod předpisem.

<br>

**Odsazení** provedeš pomocí 4 mezer (nebo 1 tabulátor). Odsazení musíš používat konzistentně v celém skriptu, jinak nastane `IndentationError`.


```python
if False:
    print("Ahoj, Matouši!")
      print("Chybné odsazení..")  # chybné odsazení
    # .. další ohlášení

print("Pokračuji..")
```


      Cell In[37], line 3
        print("Chybné odsazení..")
        ^
    IndentationError: unexpected indent




```python
if False:
    print("Ahoj, Matouši!")
    print("Chybné odsazení..")  # řádné odsazení
    # .. další ohlášení

print("Pokračuji..")
```

    Pokračuji..


Pokud *výraz* vyhodnotí **jako nepravdivý** (`False`), **přeskočí odsazený řádek** pod předpisem.

Zápis se skládá z:
1. `if`, klíčové slovo pro předpis podmínky,
2. `True`, výraz nebo proměnná (`bool(...)`),
3. `:`, řádek ukončený dvojtečkou,
4. `print(...)`odsazený následující řádek.


##### Předpis `if` / `else`


```python
jmeno = "Matouš"
plnolety = True
```


```python
if plnolety:
    print("Uživatel", jmeno, "je plnoletý.")
else:
    print("Uživatel", jmeno, "není plnoletý.")
```

    Uživatel Matouš je plnoletý.



```python
plnolety = True

if plnolety:
    # vystup = "plnoletý"
    print("Uživatel", jmeno, "je plnoletý.")
else:
    # vystup = "není plnoletý"
    print("Uživatel", jmeno, "není plnoletý.")

print(vystup)
```

    plnoletý


Zápis se nyní skládá z:
1. `if`, klíčové slovo pro **předpis podmínky**,
2. `plnolety`, **výraz**,
3. `:`, řádek **ukončený dvojtečkou**,
4. `print(...)` odsazený následující řádek, který nastane pokud je podmínka **pravdivá**,
5. `else`, klíčové slovo, pokud výraz pro větev v případě, že je výraz **nepravdivý**,
6. `:`, řádek **ukončený dvojtečkou**,
7. `print(...)` odsazený **následující řádek**.

<br>

Jednoduchý podmínkový zápis můžeš ale potkat také **v nestované podobě**:


```python
jmeno = "Matouš"
dospely = False
uzivatel = True
```


```python
if uzivatel:
    if dospely:
        print("Ahoj,", jmeno, "tady je naše kompletní nabídka.")
    else:
        print("Ahoj,", jmeno, "tady je naše nabídka pro mladistvé.")
else:
    if dospely:
        print("Ahoj, neregistrovaný uživateli, tady je naše kompletní nabídka.")
    else:
        print("Ahoj, neregistrovaný uživateli, tady je naše nabídka pro mladistvé.")


# print("Pokračuji pod podmínkou...")
```

    Ahoj, Matouš tady je naše nabídka pro mladistvé.


<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si porovnávání desetinných čísel

1. Vytvoř proměnné `cislo_1` a `cislo_2`, kam budeš ukládat vstup uživatele jako **desetinná čísla**,
2. pokud je hodnota v proměnné `cislo_1` **větší než** `cislo_2`, program by měl vypsat `"První číslo je větší než druhé."`,
3. pokud je hodnota v proměnné `cislo_1` **menší než** `cislo_2`, program by měl vypsat `"První číslo je menší než druhé."`,
4. pokud jsou obě hodnoty stejné, vypiš `"Obě čísla jsou stejná."`.


```python

```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
cislo_1 = float(input("Zadejte první číslo: "))
cislo_2 = float(input("Zadejte druhé číslo: "))

if cislo_1 == cislo_2:
    print("Obě čísla jsou stejná.")
else:
    if cislo_1 < cislo_2:
    print("První číslo je menší než druhé.")
else:
    print("První číslo je větší než druhé.")
```
</details>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.yLOyM3kOmMLeoCCP47fziQHaHa%26pid%3DApi&f=1" width="300" style="margin-left:auto; margin-right:auto"/>

## Rozvinutý podmínkový zápis

---

Podmínkový zápis ale není jen obyčejné `if`, `elif` a `else`.

<br>

Záleží na okolnostech a možných scénářích, ale pomocí operátorů můžeš zápis ještě **rozšířit**.


```python
cislo = 18
```


```python
if 0 < cislo < 10:    # 0 < cislo and cislo < 10:
    print("Patřím mezi prvních deset")
elif 0 < cislo < 20:  # --> bool
    print("Patřím mezi druhých deset")
else:
    print("Nepatřím mezi prvních dvacet")
```

    Patřím mezi druhých deset


<br>

### Předpis if / elif / else

---

Předchozí zápis ale není **ani přehledný**, **ani šikovný** (zejména kvůli nadbytečnému *nestování*).

Můžeš totiž často kombinovat některé podmínky pomocí boolean operátorů `and`, `or` a `not`.

K tomu však potřebuješ další podmínkovou větev, kterou dostaneš kombinací `else if`, tedy `elif`:


```python
jmeno = "Matouš"
uzivatel = True
dospely = False
```


```python
if uzivatel and dospely:  # False
    print("Ahoj,", jmeno, "tady je naše kompletní nabídka.")
    
elif uzivatel and not dospely:  # True and True --> True
    print("Ahoj,", jmeno, "tady je naše nabídka pro mladistvé.")
    
elif not uzivatel and dospely:
    print("Ahoj, neregistrovaný uživateli, tady je naše kompletní nabídka.")
    
else:
    print("Ahoj, neregistrovaný uživateli, tady je naše nabídka pro mladistvé.")
```

    Ahoj, Matouš tady je naše nabídka pro mladistvé.


Zápis se nyní skládá z:
1. `if`, klíčové slovo pro **předpis podmínky**,
2. `uzivatel == "Matouš"`, výrazu,
3. `:`, řádek **ukončený dvojtečkou**,
4. `print(...)` odsazený následující řádek, který se interpretuje pokud je podmínka u `if` **pravdivá**,
5. `elif`, klíčové slovo, pokud je větev `if` **nepravdivá**, zkontroluj tuto větev,
6. `:`, řádek ukončený **dvojtečkou**,
7. `elif`, ...,
8. `:`, ...,
9. `print(...)` ...,
10. `else`, klíčové slovo, proveď automaticky tuto větev, pokud byly předchozí podmínky **nepravdivé**.



```python
jmeno = "Lukas"
je_zdravy = False
```


```python
if jmeno == "Matous" and je_zdravy:
   zprava = "Ahoj, Matousi! Tak at te zdravi neopousti!"

elif jmeno == "Lukas" and je_zdravy:
    zprava = "Ahoj, Lukasi! Tak at te zdravi neopousti!"

elif jmeno == "Matous" and not je_zdravy:
    zprava = "Ahoj, Matousi! Hlavne se brzy uzdrav!"
    
elif jmeno == "Lukas" and not je_zdravy:
    zprava = "Ahoj, Lukasi! Hlavne se brzy uzdrav!"

else:
    zprava = "Ahoj, vsem ostatnim!"
```


```python
print(zprava)
```

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si hru `FizzBuzz`

1. Vytvoř proměnnou `cislo`, kam budeš ukládat vstup uživatele jako **celé číslo**,
2. pokud je číslo **dělitelné třemi**, program by měl vypsat `"Fizz"`,
3. pokud je číslo **dělitelné pěti**, program by měl vypsat `"Buzz"`,
4. pokud je číslo **dělitelné třemi i pěti**, program by měl vypsat `"FizzBuzz"`,
5. pokud číslo **není dělitelné ani třemi, ani pěti**, program by měl vypsat toto číslo.


```python

```

    True


<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
cislo = int(input("Zadejte celé číslo: "))

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

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.IILYpGKvngRy65EHQ1cMEwHaHa%26pid%3DApi&f=1&ipt=41e29f87d6cd642019c9bc57ef56de2515f8111fc83b7854775221164e2898a6&ipo=images" width="200" style="margin-left:auto; margin-right:auto"/>

## [mírně pokročilé] Ternární operátor

---
V Pythonu 2.5 byl přidán jednořádkový zápis pro jednoduchou podmínku `if/else`. Jde o **pokročilejší variantu** zápisu podmínky:

```python
<proveď_toto> if <pokud_platí_toto> else <jinak_proveď_toto>
```


```python
vek = 18
```


```python
if vek >= 18:
    print("Dospělý")
else:
    print("Mladiství")
```


```python
print("Dospělý") if vek >= 18 else print("Mladiství")
```


```python
je_dospely = True if vek >= 18 else False
```


```python
print(je_dospely)
```

<br>

Uložení hodnoty do proměnné:


```python
vek = 15

stav = "Dospělý" if vek >= 18 else "Mladiství"
```


```python
print(stav)
```

<br>

## Metody

---

Kromě *zabudovaných funkcí*, které jsou k dispozici v Pythonu, máme také tzv. **metody datových typů**.


**Metody** jsou také v podstatě nástroje, které rozšiřují použití jednotlivých datových typů.


Jaký je tedy rozdíl mezi *metodou* a *funkcí*?


1. **Funkce** jsou obecnější, protože umí pracovat s různými datovými typy (`print`),
2. **Metody** jsou úzce zaměřené na konkrétní datový typ (`str`).


```python
# Zabudovaná funkce
print(1)        # int
print(1.00)     # float
print("Ahoj!")  # str
```

    1
    1.0
    Ahoj!


### Metody stringu

Některé metody pro datový typ `str`:


```python
print(dir(str))
```

    ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']



```python
print(help(str.isnumeric))
```

    Help on method_descriptor:
    
    isnumeric(self, /)
        Return True if the string is a numeric string, False otherwise.
        
        A string is numeric if all characters in the string are numeric and there is at
        least one character in the string.
    
    None



```python
help(print)
```


```python
print("matous".isnumeric())
```

    False



```python
print("1234".isnumeric())
```

    True



```python
print("matous".upper())
```

    MATOUS



```python
print("MaTouS".lower())
```

    matous



```python
print("matous".title())
```

    Matous


<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si metody pro `str`:

1. Ze stringu `"matous.holinka@gmail.com"`, získej jenom `"matous.holinka"`,
2. nahraď ve `"matous.holinka"` znak `"."` pomocí mezery `" "`,
3. vypiš jméno *title-case*, tedy `"Matous Holinka"`.


```python

```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
print("matous.holinka@gmail.com".split("@")[0].replace(".", " ").title())
```
</details>

<br>

### Metody listu

---

Některé metody pro datový typ `list`:


```python
jmena = ["Matouš", "Lukáš"]
```


```python
print(jmena)
```


```python
jmena.append("Petr")
```


```python
print(jmena)
```


```python
help(list.insert)
```


```python
jmena.insert(0, "Marek")
```


```python
print(jmena)
```


```python
jmena.split()
```

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si metody pro `list`:

1. Z proměnné `zaznam`, získej jednotlivé hodnoty rozdělené na řádcích, vyselektuj jen validní hodnoty:
   ```python
   ['2021-01-01 11:11:11:1111 - něco se děje,',
 '2021-01-01 11:12:11:1111 - nic to nebylo,',
 '2021-01-01 11:13:11:1111 - a přece něco!,']
   ```
3. na **nultý index** přidej hodnotu:
   ```python
   ['2021-01-01 11:10:11:1111 - BANG,\n',
 '2021-01-01 11:11:11:1111 - něco se děje,',
 '2021-01-01 11:12:11:1111 - nic to nebylo,',
 '2021-01-01 11:13:11:1111 - a přece něco!,']
   ```
4. na **poslední index** přidej hodnotu:
   ```python
   ['2021-01-01 11:10:11:1111 - BANG,\n',
 '2021-01-01 11:11:11:1111 - něco se děje,',
 '2021-01-01 11:12:11:1111 - nic to nebylo,',
 '2021-01-01 11:13:11:1111 - a přece něco!,',
 '2021-01-01 11:14:11:1111 - BANG BANG!,\n']
   ```


```python
zaznam = """\
2021-01-01 11:11:11:1111 - něco se děje,\n
2021-01-01 11:12:11:1111 - nic to nebylo,\n
2021-01-01 11:13:11:1111 - a přece něco!,\n
"""
```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
zaznam = """\
2021-01-01 11:11:11:1111 - něco se děje,\n
2021-01-01 11:12:11:1111 - nic to nebylo,\n
2021-01-01 11:13:11:1111 - a přece něco!,\n
"""
zaznam_delene.insert(0, "2021-01-01 11:10:11:1111 - BANG,\n")
zaznam_delene.append("2021-01-01 11:14:11:1111 - BANG BANG!,\n")
```
</details>

➡️ ➡️ **Formulář pro Tvoje hodnocení** [**druhé lekce**](https://forms.gle/g3gH2eCGpqX14ca99) ⬅️ ⬅️

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.GMJvJ-GG0YS8H5JmHR3CbwHaHm%26pid%3DApi&f=1" width="300" style="margin-left:auto; margin-right:auto" />

## Domácí úkol

---

Vytvoř takový podmínkový zápis, který bude reagovat na nesprávně zadaná hesla (viz. příklad níže):


```python
heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
heslo_3 = "123456"      # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"
```


```python
heslo = heslo_6
```


```python
heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
heslo_3 = "12345678"    # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"
```

<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
heslo_0 = ""            # FAIL -> "Vynechal jsi pole s heslem!"
heslo_1 = "1panpes738"  # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_2 = "panpessss"   # FAIL -> "Heslo musí obsahovat jak číselné znaky, tak písmena"
heslo_3 = "12345678"    # FAIL -> "Heslo nesmí začínat číselným znakem"
heslo_4 = "aa1234"      # FAIL -> "Heslo musí být alespoň 8 znaků dlouhé"
heslo_5 = "p@npes7778"  # FAIL -> "Heslo nesmí obsahovat '@'"
heslo_6 = "panpes7778"  # PASS -> "Heslo je v pořádku"

heslo = heslo_3

if not heslo:
    print("Vynechal jsi pole s heslem!")
elif heslo[0].isdigit() and not heslo.isnumeric():
    print("Heslo nesmí začínat číselným znakem")
elif len(heslo) < 8:
    print("Heslo musí být alespoň 8 znaků dlouhé")
elif heslo.find("@") != -1:
    print('Heslo nesmí obsahovat \"@\"')
elif heslo.isnumeric() or heslo.isalpha():
    print("Heslo musí obsahovat jak číselné znaky, tak písmena")
else:
    print("Heslo je v pořádku")
```
</details>

---
