# Python akademie

---

## Obsah lekce
---

1. [Obecně k funkcím v Pythonu](#Obecně-k-funkcím-v-Pythonu),
2. [zápis uživatelských funkcí](),
3. [vstupy funkcí](#Vstupy-funkcí),
4. [dokumentace funkcí](#Dokumentace-funkcí),
5. [co je \_\_name\_\_](#Co-je-__name__),
5. [vícenásobné přiřazování](#).

---

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.50tQvVlVwtVFceew6tmZWgHaHa%26pid%3DApi&f=1&ipt=a9d603c0ed3f44eae11a95794d95f926d86054b4838f2ce663fbee5d1a8a3d42&ipo=images" width="150" style="margin-left:auto; margin-right:auto"/>

## Obecně k funkcím v Pythonu

---

V Pythonu už některé *funkce* znáš a umíš je používat.

Třeba funkce `print` a `enumerate`:


```python
print("Praha", "Brno", "Ostrava")
```

    Praha Brno Ostrava



```python
print(tuple(enumerate(("Praha", "Brno", "Ostrava"))))
```

<br>

Obecné rozdělení **funkcí v Pythonu**:
1. [**Zabudované funkce**](https://docs.python.org/3/library/functions.html), (z angl. *built-in functions*), tedy `print`, `input`, `str`, `int`, `bool`, aj. ,
2. **Uživatelské funkce**, (z angl. *user-defined functions*), klíčové slovo `def`.

<br>

Největší rozdíl mezi **zabudovanými** a **uživatelskými funkcemi** je v tom, že *zabudované funkce* stačí **spustit pomocí jejich jména**.

Zatímco *uživatelskou funkci* je nejprve nutné **definovat** (vytvořit) a teprve poté **použít** (spustit).

<br>

### Zabudované funkce

---
Tyto funkce jsou velkými pomocníky, protože ti umožní zjednodušit různé procesy.


```python
jmena = enumerate(('Matouš', 'Lukáš'))
```

Navíc můžeš jejich použití **doplnit volitelnými argumenty**.

*Volitelný argument* je objekt, který můžeš (ale nemusíš) zadávat.

Funkce umí pracovat bez něj, případně má dopředu nachystanou nějakou **počáteční hodnotu**.


```python
# Jak začít číslovat "enumerate" objekt od 0
print(tuple(enumerate(('Matouš', 'Lukáš'))))
```


```python
# print(help(enumerate))
```


```python
# Jak začít číslovat "enumerate" objekt od 1
print(tuple(enumerate(('Matouš', 'Lukáš'), start=10)))
```

<br>

Pokud funkci `print` napíšeš **bez argumentů**, s několika různými hodnotami za sebou, tvůj výstup se seřadí za sebe.

Zobraz si nápovědu pomocí ohlášení `help(print)`:


```python
print("Matous", "Marek", "Lukas")
```


```python
print(help(print))
```

<br>

Všimni si, že **argument** `sep` má přednastavenou defaultní hodnotu – mezeru.

Proto jsou jednotlivé hodnoty řazené s mezerou za sebou.


Tuto hodnotu můžeš přepsat podle svých potřeb. Například vypsat jednotlivé hodnoty **pod sebe** pomocí speciálního znaku `\n`:


```python
print("Matous", "Marek", "Lukas", sep='\n')
```

<br>

*Volitelné argumenty* můžeš používat téměř u všech **zabudovaných funkcí**.

Proto pokud budeš potřebovat pracovat s **zabudovanými funkcemi** vždy zkontroluj, jestli neobsahují nějaký nepovinný argument, který ti pomůže.


<details>
  <summary><strong>Seznam používaných zabudovaných funkcí</strong></summary>
  <table>
<thead>
<tr>
<th>Funkce</th>
<th>Popis</th>
<th>Příklad použití</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>print()</code></td>
<td>Vypisuje hodnotu nebo hodnoty na výstup (obvykle konzoli).</td>
<td><code>print(&quot;Hello, World!&quot;)</code></td>
</tr>
<tr>
<td><code>len()</code></td>
<td>Vrací délku objektu (řetězec, seznam, tuple atd.).</td>
<td><code>len([1, 2, 3])  # Výstup: 3</code></td>
</tr>
<tr>
<td><code>range()</code></td>
<td>Generuje sekvenci čísel.</td>
<td><code>list(range(5))  # Výstup: [0, 1, 2, 3, 4]</code></td>
</tr>
<tr>
<td><code>type()</code></td>
<td>Vrací typ objektu.</td>
<td><code>type(123)  # Výstup: &lt;class &#39;int&#39;&gt;</code></td>
</tr>
<tr>
<td><code>int()</code></td>
<td>Převede hodnotu na celé číslo, pokud je to možné.</td>
<td><code>int(&quot;42&quot;)  # Výstup: 42</code></td>
</tr>
<tr>
<td><code>str()</code></td>
<td>Převede hodnotu na řetězec.</td>
<td><code>str(123)  # Výstup: &#39;123&#39;</code></td>
</tr>
<tr>
<td><code>float()</code></td>
<td>Převede hodnotu na desetinné číslo, pokud je to možné.</td>
<td><code>float(&quot;3.14&quot;)  # Výstup: 3.14</code></td>
</tr>
<tr>
<td><code>input()</code></td>
<td>Čte vstup od uživatele jako řetězec.</td>
<td><code>name = input(&quot;Zadej své jméno: &quot;)</code></td>
</tr>
<tr>
<td><code>abs()</code></td>
<td>Vrací absolutní hodnotu čísla.</td>
<td><code>abs(-5)  # Výstup: 5</code></td>
</tr>
<tr>
<td><code>round()</code></td>
<td>Zaokrouhlí číslo na zadaný počet desetinných míst.</td>
<td><code>round(3.14159, 2)  # Výstup: 3.14</code></td>
</tr>
<tr>
<td><code>max()</code></td>
<td>Vrací největší hodnotu z iterovatelného objektu nebo několika čísel.</td>
<td><code>max([1, 2, 3])  # Výstup: 3</code></td>
</tr>
<tr>
<td><code>min()</code></td>
<td>Vrací nejmenší hodnotu z iterovatelného objektu nebo několika čísel.</td>
<td><code>min([1, 2, 3])  # Výstup: 1</code></td>
</tr>
<tr>
<td><code>sum()</code></td>
<td>Sečte všechny hodnoty v iterovatelném objektu.</td>
<td><code>sum([1, 2, 3])  # Výstup: 6</code></td>
</tr>
<tr>
<td><code>sorted()</code></td>
<td>Vrací seřazený seznam z iterovatelného objektu.</td>
<td><code>sorted([3, 1, 2])  # Výstup: [1, 2, 3]</code></td>
</tr>
<tr>
<td><code>list()</code></td>
<td>Převede iterovatelný objekt na seznam.</td>
<td><code>list(&quot;abc&quot;)  # Výstup: [&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]</code></td>
</tr>
<tr>
<td><code>dict()</code></td>
<td>Vytváří slovník z dvojic klíč-hodnota.</td>
<td><code>dict(a=1, b=2)  # Výstup: {&#39;a&#39;: 1, &#39;b&#39;: 2}</code></td>
</tr>
<tr>
<td><code>set()</code></td>
<td>Převede iterovatelný objekt na množinu (bez duplikátů).</td>
<td><code>set([1, 2, 2, 3])  # Výstup: {1, 2, 3}</code></td>
</tr>
<tr>
<td><code>tuple()</code></td>
<td>Převede iterovatelný objekt na tuple.</td>
<td><code>tuple([1, 2, 3])  # Výstup: (1, 2, 3)</code></td>
</tr>
<tr>
<td><code>bool()</code></td>
<td>Převede hodnotu na <code>True</code> nebo <code>False</code> na základě její pravdivosti.</td>
<td><code>bool(0)  # Výstup: False</code></td>
</tr>
<tr>
<td><code>isinstance()</code></td>
<td>Testuje, zda objekt patří do specifikované třídy nebo typu.</td>
<td><code>isinstance(5, int)  # Výstup: True</code></td>
</tr>
<tr>
<td><code>all()</code></td>
<td>Vrací <code>True</code>, pokud jsou všechny prvky iterovatelného objektu pravdivé.</td>
<td><code>all([True, True, False])  # Výstup: False</code></td>
</tr>
<tr>
<td><code>any()</code></td>
<td>Vrací <code>True</code>, pokud je alespoň jeden prvek iterovatelného objektu pravdivý.</td>
<td><code>any([False, True, False])  # Výstup: True</code></td>
</tr>
<tr>
<td><code>map()</code></td>
<td>Aplikuje funkci na všechny prvky iterovatelného objektu.</td>
<td><code>list(map(str, [1, 2, 3]))  # Výstup: [&#39;1&#39;, &#39;2&#39;, &#39;3&#39;]</code></td>
</tr>
<tr>
<td><code>filter()</code></td>
<td>Filtruje prvky iterovatelného objektu na základě podmínky.</td>
<td><code>list(filter(lambda x: x &gt; 1, [1, 2, 3]))  # Výstup: [2, 3]</code></td>
</tr>
<tr>
<td><code>zip()</code></td>
<td>Kombinuje více iterovatelných objektů do jednoho iterátoru tuple.</td>
<td><code>list(zip([1, 2], [&#39;a&#39;, &#39;b&#39;]))  # Výstup: [(1, &#39;a&#39;), (2, &#39;b&#39;)]</code></td>
</tr>
<tr>
<td><code>enumerate()</code></td>
<td>Vrací iterátor s indexy a hodnotami iterovatelného objektu.</td>
<td><code>list(enumerate([&#39;a&#39;, &#39;b&#39;, &#39;c&#39;]))  # Výstup: [(0, &#39;a&#39;), (1, &#39;b&#39;), (2, &#39;c&#39;)]</code></td>
</tr>
<tr>
<td><code>open()</code></td>
<td>Otevírá soubor a vrací objekt souboru.</td>
<td><code>open(&#39;file.txt&#39;, &#39;r&#39;)</code></td>
</tr>
<tr>
<td><code>reversed()</code></td>
<td>Vrací iterátor, který prochází iterovatelný objekt v opačném pořadí.</td>
<td><code>list(reversed([1, 2, 3]))  # Výstup: [3, 2, 1]</code></td>
</tr>
</tbody>
</table>


</details>


<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.SdA4GDooZXTMbDZDgDA6aQAAAA%26pid%3DApi&f=1" width="150" style="margin-left:auto; margin-right:auto">

## Uživatelské funkce

---

Můžeš se dostat do situace, kdy žádná z nabízených *zabudovaných funkcí* nedělá přesně to, co potřebuješ.

V takovém případě potřebuješ vytvořit vlastní funkci, která ti bude umět pomoct.

<br>

Tvůj úkol je napsat proces, který sečte **všechny číselné hodnoty** uvnitř sekvence.


```python
ciselna_rada = (1, 2, 3, 4)
```


```python
print(sum(ciselna_rada))
```

Pomocí zabudované funkce `sum` to není žádný problém.

<br>

Co když sekvence obsahuje **neočekávaný datový typ**:


```python
ciselna_rada = (1, 2, 3, "pět", 6)
```


```python
print(sum(ciselna_rada))
```


```python
soucet_cisel = 0
```


```python
print(isinstance("M", list))
```


```python
for cislo in ciselna_rada:
    if isinstance(cislo, str) and not cislo.isnumeric():
        continue
    soucet_cisel += int(cislo)
else:
    print(soucet_cisel)
```

<br>

Co když ale dostaneš **pět různých sekvencí**?

Můžeš samozřejmě přepsat zápis pro každou sekvenci zvlášť.

Ale co když těch sekvencí bude **100**, **10 000**?

Právě proto existují **uživatelské funkce**, kterou stačí **jedenkrát definovat** a následně spouštět kolikrát potřebuješ:


```python
# Zatím neznámá syntaxe
def secti_vsechny_cisla(sekvence):
    soucet_cisel = 0

    for cislo in sekvence:
        if isinstance(cislo, str) and not cislo.isnumeric():
            continue
        soucet_cisel += int(cislo)
    else:
        print(soucet_cisel)
```


```python
ciselna_r_1 = (1, 2, 3, "a")
ciselna_r_2 = (1, 2, 3, 4)
ciselna_r_3 = (5, 6, 7, 8)
ciselna_r_4 = (9, 10, 11, 12)
ciselna_r_5 = ("sto", 200, 300)
```


```python
secti_vsechny_cisla(ciselna_r_1)
secti_vsechny_cisla(ciselna_r_2)
secti_vsechny_cisla(ciselna_r_3)
secti_vsechny_cisla(ciselna_r_4)
secti_vsechny_cisla(ciselna_r_5)
```

Ukázku výše **nemusíš nyní chápat**.

Je tu hlavně pro ilustraci, jak je důležité mít uživatelské funkce.

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.zQJEQEbVVbu2Fh8wQgPyEwHaGv%26pid%3DApi&f=1&ipt=23162684677d95a2283e1659fe266bd09c2b8909726510adaa084be6204c0a85&ipo=images" width="150" style="margin-left:auto; margin-right:auto">

## Používání uživatelských funkcí

---

Jak tedy *uživatelskou funkci* správně používat?

Z jakých kroků se správné použití skládá?

<br>

Nejprve musíš funkci:
1. 📃 Jednou **definovat** (*vytvořit*),
2. ▶️ ▶️ ▶️ a potom ji můžeš začít opakovaně **spouštět**.

Pořadí je **důležité**! Takže nemůžeš spouštět takovou uživatelskou funkci, kterou **prvně nedefinuješ**.



```python
vysledek = scitej_dve_hodnoty(1, 14)  # 1 + 14
```


```python
def scitej_dve_hodnoty(cislo_1, cislo_2):             # POVINNÉ: Předpis funkce a parametry funkce
    """
    Vraci soucet dvou hodnot uvnitr parametru.
    """                                               # VOLITELNÉ: dokumentace funkce
    return cislo_1 + cislo_2                          # VOLITELNÉ: vracené hodnoty
```

Pokud si předchozí ukázku spustíš, nic se nestane. Je to kvůli tomu, že funkci **pouze definuješ** a nespouštíš.

<br>

V příkladu si můžeš všimnout těchto **charakteristických rysů** pro uživatelskou funkci:
1. `def` je *klíčový výraz* označující předpis (definici) funkce,
2. `scitej_dve_hodnoty` je tvoje označení funkce, díky kterému můžeš funkci později spustit (ideálně má představovat účel funkce),
3. `(cislo_1, cislo_2)` v kulaté závorce jsou umístěné **parametry** funkce. Tedy proměnné, se kterými chceš, aby funkce pracovala.
4. `:` předpisový řádek musí být ukončený dvojtečkou (jako u podmínkových zápisů, cyklů, aj.),
5. `"""Vraci soucet dvou .."""` na odsazeném řádku následuje *docstring*, tedy bližší popis účelu funkce (zejména pokud jméno nedostačuje),
6. `return` ohlášení z funkce vrací žádané hodnoty (nemusí být součástí funkce vždy).

### Spuštění funkcí

---

Takže pokud máš funkci **definovanou**, můžeš ji spouštět kolikrát chceš a kde chceš (samozřejmě potom, co ji definuješ).


```python
soucet_1 = scitej_dve_hodnoty(1, 14)  # 1. spuštění funkce
soucet_2 = scitej_dve_hodnoty(2, 8)   # 2. spuštění funkce
```


```python
print(soucet_1, soucet_2, sep="\n")
```

Spouštění bez ohlášení `return`:


```python
def scitej_dve_hodnoty(cislo_1, cislo_2):             # POVINNÉ: Předpis funkce a parametry funkce
    """
    Vraci soucet dvou hodnot uvnitr parametru.
    """                                               # VOLITELNÉ: dokumentace funkce
    vysledek = cislo_1 + cislo_2                      # VOLITELNÉ: vracené hodnoty
```


```python
soucet_3 = scitej_dve_hodnoty(2, 2)
```


```python
print(soucet_3)
```

<br>

### ⚠️ ⚠️ Chyby na začátek ⚠️ ⚠️

---


```python
scitej_dve_hodnoty           # zapomněl jsem závorky
```


```python
scitej_dve_hodnoty()         # chybějící vstupní hodnoty, tzv. argumenty
```


```python
scitej_dve_hodnoty(1, 9, 5)  # špatný počet argumentů při spouštění
```


```python
scitej_dve_hodnoty(1, 99)    # správný počet parametrů & argumentů
```

**DEMO: Ukázka pro skript**


```python
scitej_dve_hodnoty(1, 99)    # zapoměl jsem uložit vrácenou hodnotu do proměnné
```


```python
vysledek = scitej_dve_hodnoty(2, 3)
```


```python
print(vysledek)
```

### Souhrn

---

Pár detailů pro spuštění funkcí:
1. Funkci *spouštíš* přes její **jméno, kulaté závorky a vstupů**,
2. při definování, do kulatých závorek píšeš obecné proměnné, **parametry** funkcí (zajištují obecné použití),
3. při spouštění, do kulatých závorek musíš zapsat skutečné hodnoty, tedy **argumenty** funkcí,
4. argumenty si funkce sama skládá do parametrů podle několika vzorů,
5. pokud má funkce vracet hodnoty, obsahuje ohlášení `return`,
6. vrácenou hodnotu si musíš schovat do proměnné (`soucet_1`, `soucet_2`). Pokud to neuděláš, o součet **přijdeš**.


```python
def moje_funce(x, y):
    return x
```


```python
vracene_hodnoty = moje_funce("a", "b")
```


```python
print(vracene_hodnoty)
```

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s *uživatelskými funkcemi*:

1. Nahraj knihovnu `random`,
2. vytvoř definici uživatelské funkce `vygeneruj_tuple`,
3. funkce potřebuješ zadat **dva celočíselné parametry** `delka` a `max_hodnota`,
4. funkce vrací datový typ `tuple`,
5. obecným účelem funkce je vrátit takový *tuple*, který má délku podle `delka` a rozsah náhodných celých čísel je z intervalu `0 ~ max_hodnota`,
6. nakonec funkci zavolej pro tyto argumenty: `5, 50`, `10, 100` a `15, 150` (pro parametry `delka`, `max_hodnota`).


```python
from random import choices  # help(random.choices)
```


```python

```


```python
print(
    vygeneruj_tuple(5, 50),
    vygeneruj_tuple(10, 100),
    vygeneruj_tuple(15, 150),
    sep="\n"
)
```

<details>
  <summary>▶️ Klikni zde pro zobrazení řešení</summary>
   
```python
import random


def vygeneruj_tuple(delka, stop):
    return tuple(choices(range(stop), k=delka))


print(
    vygeneruj_tuple(5, 50),
    vygeneruj_tuple(10, 100),
    vygeneruj_tuple(15, 150),
    sep="\n"
)
```
</details>

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.gvxRdZcKOECoPck4y_-vlQHaD4%26pid%3DApi&f=1&ipt=929a3dae2ce99e1f988755713c8581862700ca34780089216a705d23e8a0f6b7&ipo=images" width="200" style="margin-left:auto; margin-right:auto">

## Vstupy funkcí

---


Obecně funkce pracuje se **vstupy**.

Tento pojem souhrnně označuje nejen *parametry*, ale také *argumenty*.

Ty jsou potom do funkce dávkované dle několika vzorů.

<br>

Rozdíl mezi nimi je následující:
- **parametry** slouží jako obecné proměnné při definici, 
- **argumenty** jsou konkrétní hodnoty, které vkládáš při spouštění.

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.bUbr5JhWe_1wmqncA78cIgHaHa%26pid%3DApi&f=1&ipt=b5486e0a2625fb93691e72daa535e6513f570af8391582c74e44e9e292bcab1c&ipo=images" width="200" style="margin-left:auto; margin-right:auto">


<br>

Prohlédni si ukázku:


```python
def vytvor_cele_jmeno(jmeno, prijmeni):
    """
    Spoj zformatovane hodnoty v parametrech.

    Priklad:
    >>> vytvor_cele_jmeno("Petr", "Svetr")
    p.svetr
    """
    return ".".join(
        (
            jmeno[0].lower(),
            prijmeni.lower()
        )
    )
```


```python
print(vytvor_cele_jmeno("Adam", "Novak"))
```

<br>

<img src="http://mathinsight.org/media/image/image/function_machine.png" width="300" style="margin-left:auto; margin-right:auto">

Co jsou tedy **parametry** a co **argumenty**?

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.uufe_GDvF2057NFWgKOVXwAAAA%26pid%3DApi&f=1" width="150" style="margin-left:auto; margin-right:auto">

## Dokumentace funkcí

---


Psát **dokumentaci** funkce resp. *docstring* je volitelnou záležitostí.

<br>

### Důsledné jméno funkce

---

Někdy potřebuješ vytvořit jednoduchou funkci, jejíž účel plně vystihuje její **jméno**:


```python
def vynasob_dve_cisla(x, y):
    return x * y
```


```python
print(vynasob_dve_cisla(2, 8))
```

V takovém případě **není potřeba** zapisovat *docstring*.

<br>

Někdy se ale popis může hodit.

Zejména tehdy pokud **jméno** *uživatelské funkce* **nedostačuje**:


```python
def vypocitej_vyskyt_pismen(pismena):
    vyskyt = dict()

    for slovo in pismena:
        vyskyt[slovo] = vyskyt.setdefault(slovo, 0) + 1
    else:
        return vyskyt
```

Nyní už **není zcela patrné**, jaký je účel funkce, že?

<br>

### Popisek funkce

---

**Jméno** samotné funkce, v ukázce výš, není dostačující:


```python
def vypocitej_vyskyt_dat(pismena):
    """
    Vrať slovník, který obsahuje výčet
    jednotlivých prvků v zadaném parametru.

    Inkrementaci hodnoty u klíčů ve slovníků probíhá tak,
    že pokud klíč ve slovníku není, založím jej
    s hodnotou 0 + 1 = 1.
    
    Pokud klíč ve slovníku 'vyskyt' máme, nezakládám,
    pouze inkrementuji x + 1.
    """
    vyskyt = dict()

    for pismeno in pismena:
        vyskyt[pismeno] = vyskyt.setdefault(pismeno, 0) + 1
    else:
        return vyskyt
```


```python
print(vypocitej_vyskyt_dat(("a", "b", "a", "c", "d", "b", "a")))
```

Jednou větou **vysvětlená podstata** této *uživatelské funkce* lépe popíše účel funkce `vypocitej_vyskyt_dat`.

<br>

Dále můžeš tuto *nápovědu* získat pomocí zabudované funkce `help`:


```python
help(vypocitej_vyskyt_dat)
```

<br>


### Vysvětlivky parametrů a vrácené hodnoty

---

Pokud je krátký *docstring* **nedostatečný**, nebo pracuješ s různými **parametry**, které jsou pro uživatele komplikované, můžeš je také popsat:


```python
def vypocitej_vyskyt_dat(pismena):
    """
    Vrať slovník, který obsahuje výčet jednotlivých prvků v zadaném parametu.

    Inkrementaci hodnoty u klíčů ve slovníků probíhá tak, že pokud klíč ve slovníku
    není, založím jej s hodnotou 0 + 1 = 1.
    Pokud klíč ve slovníku 'vyskyt' máme, nezakládám, pouze inkrementuji x + 1.

    :param pismena: parametr "pismena" obsahující zadaný text.
    :type pismena: tuple
    :return: hodnota se znaky z textu a počet jejich výskytů.
    :rtype: dict
    """
    vyskyt = {}
       
    for pismeno in pismena:
        vyskyt[pismeno] = vyskyt.setdefault(pismeno, 0) + 1

    return vyskyt
```


```python
print(vypocitej_vyskyt_dat(("a", "b", "a", "c", "d", "b", "a")))
```


```python
help(vypocitej_vyskyt_dat)
```

<br>

### Příklad průběhu funkce

---

Někdy je dobrá ukázka lepší jak tisíc slov, proto je později vhodné úvadět **příklad použití**:


```python
def vypocitej_vyskyt_dat(pismena):
    """
    Vrať slovník, který obsahuje výčet jednotlivých prvků v zadaném parametru.

    Inkrementaci hodnoty u klíčů ve slovníků probíhá tak, že pokud klíč ve slovníku
    není, založím jej s hodnotou 0 + 1 = 1.
    Pokud klíč ve slovníku 'vyskyt' máme, nezakládám, pouze inkrementuji x + 1.
    
    :param pismena: parametr "pismena" obsahující zadaný text.
    :type pismena: tuple
    :return: slovník se znaky z textu a počet jejich výskytů.
    :rtype: dict

    :Example:
    >>> vysledek = vypocitej_vyskyt_dat(("a", "b", "a"))
    >>> vysledek
    {'a': 2, 'b': 1}
    """
    vyskyt = dict()

    for slovo in pismena:
        vyskyt[slovo] = vyskyt.setdefault(slovo, 0) + 1

    return vyskyt
```


```python
print(vypocitej_vyskyt_dat(("a", "b", "a", "c", "d", "b", "a")))
```


```python
help(vypocitej_vyskyt_dat)
```

<br>

Je tedy **nutné** zapisovat *docstring*? Určitě to **není nutnost**.

Ale rozhodně je to velmi nápomocné, protože ti pomůže uvědomit si:
1. Jestli dostatečně rozumíš **účelu funkce**,
2. jestli funkce skutečně **provádí jen to, co má**,
3. jestli má správný **počet parametrů**, případně jakého typu,
4. jestli a jaké objekty **funkce vrací**.

<br>

Do budoucna potom můžeš využít *docstring* při:
1. Generování **dokumentace projektu** pomocí nástroje [Sphinx](https://www.sphinx-doc.org/en/master/),
2. **testování funkcí** pomocí modulu [doctest](https://docs.python.org/3/library/doctest.html).


```python
def vypocitej_vyskyt_dat(pismena):
    """
    Vrať slovník, který obsahuje výčet jednotlivých prvků v zadaném parametru.

    :Example:
    >>> vysledek = vypocitej_vyskyt_dat(("a", "b", "a"))
    >>> vysledek
    {'a': 2, 'b': 1}
    >>> vysledek = vypocitej_vyskyt_dat(("a", "b"))
    >>> vysledek
    {'a': 1, 'b': 2}
    """
    vyskyt = dict()

    for slovo in pismena:
        vyskyt[slovo] = vyskyt.setdefault(slovo, 0) + 1

    return vyskyt


import doctest
doctest.testmod()
```

    **********************************************************************
    File "__main__", line 10, in __main__.vypocitej_vyskyt_dat
    Failed example:
        vysledek
    Expected:
        {'a': 1, 'b': 2}
    Got:
        {'a': 1, 'b': 1}
    **********************************************************************
    1 items had failures:
       1 of   4 in __main__.vypocitej_vyskyt_dat
    ***Test Failed*** 1 failures.





    TestResults(failed=1, attempted=4)



<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s docstringy v *uživatelských funkcích*:

1. Vytvoř takovou *uživatelskou funkci*, která potřebuje jeden *parametr* `udaje` (typu `tuple`),
2. funkce musí opět vracet typ `tuple`,
3. jejím účelem je odstranit ze zadaného argumentu všechny `None` hodnoty a vrátit zbytek,
4. vhodně **funkci pojmenuj**,
5. napiš krátký *docstring*, který pomůže funkci lépe dovysvětlit.


```python
krestni_jmena = ('Matouš', None, 'Marek', 'Lukáš', None, 'Jan')
prijmeni = ('Holinka', None, 'Novák', 'Holinka', None, None)
```


```python
def XYZ(udaje):
    """
    Funkce vrací zadanou sekvenci bez prázdný/ chybějících hodnot
    
    

```


```python
print(
    ocistit_od_prazdnych(krestni_jmena),
    ocistit_od_prazdnych(prijmeni),
    sep='\n'
)
```

<details>
  <summary>▶️ Klikni zde pro zobrazení řešení</summary>
   
```python
krestni_jmena = ('Matouš', None, 'Marek', 'Lukáš', None, 'Jan')
prijmeni = ('Holinka', None, 'Novák', 'Holinka', None, None)


def filtruj_prazdne_hodnoty(udaje: tuple) -> tuple:
    """
    Funkce vrací pole hodnot bez prázdných hodnot.

    :param udaje: Zadané pole, které může obsahovat prázdné hodnoty,
    :type udaje: tuple
    :return: pole bez prázdných hodnot,
    :rtype: tuple
    """
    return tuple(
        hodnota for hodnota in udaje
        if hodnota
    )


print(
    filtruj_prazdne_hodnoty(krestni_jmena),
    filtruj_prazdne_hodnoty(prijmeni),
    sep="\n"
)
```
</details>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.cjfmUt8xYHoEdmQWxT1fBgHaHa%26pid%3DApi&f=1" width="150" style="margin-left:auto; margin-right:auto">

## Co je `__name__`

---

Velmi často se při čtení cizího kódu můžeš setkat s **tímto ohlášením**:
```python
if __name__ == "__main__":
    # ...
```

Bývá velmi často vložené právě **na konci modulu** (tedy souboru s příponou `.py`)

Představ si situaci, že potřebuješ nahrát jen objekt `funkce_2`:


```python
%%file muj_modul_1.py
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

hlavni_funkce()
```

    Writing muj_modul_1.py


<br>

Díky, **nahrávání knihoven** můžeš snadno použít *funkci* z jiného modulu.

Víš totiž, kde je soubor `muj_soubor.py` umístěný:
```python
import muj_modul

muj_modul.funkce_2()
```

<br>

Jakmile tebou vytvořený soubor **s nahraným modulem** spustíš, získáš tento výstup:
```bash
Spouštění první funkce...
Spouštění druhé funkce...
Spouštění třetí funkce...
Spouštění druhé funkce...
```

⚠️ Místo, aby došlo ke spuštění **pouze** *uživatelské funkce* `funkce_2`, došlo ke spuštění **všech funkcí**! ⚠️

<br>

V této ukázce to není tak zásadní problém. Ale představ si, že by spuštění funkcí trvalo **několik minut** a potřebovalo **nezanedbatelné množství paměti** tvého počítače.

Tomu je potřeba rozhodně zabránit, jinak nemůžeš rozumně pracovat s takovým modulem.

<br>

Je tedy nutné:
1. `muj_modul.py` **spouštět jako skript (program)** pro Python s funkcí `hlavni_funkce()`,
2. `muj_modul.py` **nahrávat jako modul** Pythonu bez funkce `hlavni_funkce()`.


```python
%%file muj_modul_2.py
# soubor muj_modul.py
def hlavni_funkce():
    funkce_1()
    funkce_2()
    funkce_3()

def funkce_1():
    print("Spouštění první funkce...")

def funkce_2():
    """Funkce, kterou potřebuješ."""
    print("Spouštění druhé funkce...")

def funkce_3():
    print("Spouštění třetí funkce...")


if __name__ == "__main__":
    hlavni_funkce()
```

Pokud zkusíš tentokrát **spustit soubor** `muj_modul.py`:
```
$ python muj_modul.py
```
Dostaneš výstupem:
```
Spouštění souboru..
Spouštění první funkce..
Spouštění druhé funkce..
Spouštění třetí funkce..
```

<br>

Pokud budeš chtít `muj_modul.py` **nahrávat** pomocí ohlášení `import`:
```python
import muj_modul

muj_modul.funkce_2()
```
Dostaneš jako výstup:
```
Nahrávání modulu..
Spouštění druhé funkce..
```

<br>

Tím dosáhneš toho, že tebou vytvořený soubor `muj_modul.py` funguje pro oba scénaře. Tedy pracuje jako **spustitelný soubor** (skript) a současně jako **plnohodnotný modul**.

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.I_ciaAqJVtH3k_LDV-4a8AHaEc%26pid%3DApi&f=1&ipt=74100f497253ea415c13868adb6e91d832625b2dfe1b2cf852efaf93feeb7546&ipo=images" width="350" style="margin-left:auto; margin-right:auto">

## Řádné funkce uživatele

---

Psaní uživatelských funkcí má ovšem jistá doporučení.

### Znovu nevymýšlet kolo

---

Nejprve zkontroluji *zabudované funkce*, pak tvořím vlastní funkci:


```python
cisla = (1, 2, 3)
```


```python
# TAKHLE NE!
def vypocitej_sumu(cisla):
    suma = 0

    for cislo in cisla:
        suma = suma + cislo
    return suma
```


```python
print(vypocitej_sumu(cisla))
```

    6



```python
# TAKHLE ANO!
suma = sum(cisla)
```


```python
def vypis_pozdrav():
    return "Ahoj!"
```


```python
vypis_pozdrav()
```




    'Ahoj!'




```python
class Zdravic:
    def pozdrav(self):
        return "Ahoj!"
```


```python
zdravici = Zdravic()
```


```python
zdravici.pozdrav()
```




    'Ahoj!'




```python
print("Ahoj!")
```

    Ahoj!


<br>

### Na jménu záleží

---
Popisuje totiž účel funkce (pokud nelze napsat, zapiš *docstring* funkce):


```python
# TAKHLE NE!
def email():
    pass
```


```python
email()
```

Slovesem vždycky začni popisovat jméno funkce:


```python
# TAKHLE ANO!
def posli_email():
    pass
```


```python
posli_email()
```

<br>

### Rozumné množství parametrů

---
Ideálně **2-3 parametry** (jsou ovšem výjimky):


```python
# TAKHLE NE!
def zobraz_nabidku(titulek, obsah, tlacitko, datum):
    pass
```


```python
# TAKHLE ANO!
def vytvor_popisek(titulek, obsah):
    pass

def vytvor_tlacitko(tlacitko):
    pass

def vytvor_datum():
    pass
```

<br>

### Co je psáno, to je dáno

---


Funkce by měla provádět **jedinnou věc** (jinak je špatně čitelná, pochopitelná, testovatelná):


```python
# TAKHLE NE!
def posli_email_seznamu_klientu(klienti):
    """
    Filtruj pouze aktivni klienty a odesli zpravu.
    """
    for klient in klienti:
        if klient.je_aktivni:
            posli_email(klient)
```


```python
# TAKHLE ANO!
def jen_aktivni_klienti(klienti):
    return [klient for klient in klienti if klient.je_aktivni]

def posli_email(klient):
    pass
```

<br>

### Počítá se jen to doma

---

Funkce pracuje pouze **s vlastními parametry** (proměnnými):


```python
# TAKHLE NE!
oddelovac = "---"
datum = "01.01.2001"

def vytvor_zpravu(autor, zapis):
    vytvor_hlavicku(datum, oddelovac)
    vytvor_text(autor, zapis)
```


```python
# TAKHLE ANO!
def vytvor_zpravu(autor, zapis):
    oddelovac = "---"
    vytvor_hlavicku(dnesni_datum(), oddelovac)
    vytvor_text(autor, zapis)

def dnesni_datum():
    pass
```

😍 Interpret Pythonu miluje funkce! 😍 Vytváří oddělená prostředí pro proměnné, se kterými efektivněji pracuje.

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.W6yGtI3IFcM0MeXy2LfTkAAAAA%26pid%3DApi&f=1&ipt=c39ef8447701e7e226d2410bb12fc7f55372748d3f93302cf78ec775ef9c938f&ipo=images" width="150" style="margin-left:auto; margin-right:auto">

## Vícenásobné přiřazení hodnot

---

Doposud přiřazuješ hodnoty k odkazům tímto způsobem:


```python
jmeno = 'Matouš'
```


```python
print(jmeno)
```

    Matouš


<br>

Současně přiřadit více hodnot **do několika proměnných**:


```python
prvni_jmeno = ('Matouš', 'Lukáš')[0]
```


```python
druhe_jmeno = ('Matouš', 'Lukáš')[1]
```


```python
print(prvni_jmeno, druhe_jmeno, sep="\n")
```

    Matouš
    Lukáš


Současně ale existují i **další varianty přiřazení** hodnoty/hodnot.

<br>

### Vícenásobné přiřazení (LS = PS)

---

Pokud máš na pravé straně (PS) více hodnot, můžeš je rozdělit.

Rozdělení probíhá následovně:


```python
prvni_jmeno, druhe_jmeno = ('Matouš', 'Jan')  # LS: 2 nazvy promennych = PS: 2 udaje
```


```python
print(prvni_jmeno, druhe_jmeno, sep="\n")
```

    Matouš
    Jan


<br>

Vícenásobné přiřazování **při vrácených hodnotách**:


```python
def ziskej_cele_jmeno_a_vek() -> tuple:
    return ('Matouš', 'Holinka', 30)
```


```python
vysledek = ziskej_cele_jmeno_a_vek()
```


```python
print(vysledek)
```

    ('Matouš', 'Holinka', 30)



```python
krestni_jmeno = ziskej_cele_jmeno_a_vek()[0]
prijmeni = ziskej_cele_jmeno_a_vek()[1]
vek = ziskej_cele_jmeno_a_vek()[2]
```


```python
print(krestni_jmeno, prijmeni, vek, sep="\n")
```

    Matouš
    Holinka
    30


<br>

Nyní potřebuji rozdělit indexy z tuplu **do oddělených proměnných**:


```python
krestni_jmeno, prijmeni, vek = ziskej_cele_jmeno_a_vek()
```


```python
print(krestni_jmeno, prijmeni, vek, sep="\n")
```

    Matouš
    Holinka
    30


Hodnot a proměnných může být samozřejmě více.

Zásadní je dodržet s tímto zápisem pravidlo, **kolik hodnot, tolik proměnných**.


```python
jmeno_1, jmeno_2 = ["Matous", "Lukas", "Petr"]
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[42], line 1
    ----> 1 jmeno_1, jmeno_2 = ["Matous", "Lukas", "Petr"]


    ValueError: too many values to unpack (expected 2)



```python
jmeno_1, jmeno_2, jmeno_3 = ["Matous", "Lukas"]
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[43], line 1
    ----> 1 jmeno_1, jmeno_2, jmeno_3 = ["Matous", "Lukas"]


    ValueError: not enough values to unpack (expected 3, got 2)


<br>

### Vícenásobné přiřazení s hvězdičkou (*)

---

Syntaxe je velice podobná té předchozí.

Nicméně doplněná hvězdička má za účel sbalit všechny zbývající hodnoty do jedinné proměnné.


```python
jmeno_1, jmeno_2, zbytek_jmen = ["Matous", "Marek", "Lukas", "Jan"]
```


    ---------------------------------------------------------------------------

    ValueError                                Traceback (most recent call last)

    Cell In[44], line 1
    ----> 1 jmeno_1, jmeno_2, zbytek_jmen = ["Matous", "Marek", "Lukas", "Jan"]


    ValueError: too many values to unpack (expected 3)



```python
jmeno_1, jmeno_2, *zbytek_jmen = ["Matous", "Marek", "Lukas", "Jan"]
```


```python
print(jmeno_1, jmeno_2, zbytek_jmen, sep="\n")
```

    Matous
    Marek
    ['Lukas', 'Jan']


Všimněte si jak se hodnoty v proměnných změní, pokud změníme pořadí, kdy hvězdičku zapíšeme:


```python
jmeno_1, *zbytek_jmen, jmeno_2 = ["Matous", "Marek", "Lukas", "Jan"]
```


```python
print(jmeno_1, zbytek_jmen, jmeno_2, sep="\n")
```

    Matous
    ['Marek', 'Lukas']
    Jan



```python
jmeno_1, *zbytek_jmen, jmeno_2, jmeno_3 = ["Matous", "Marek", "Lukas", "Jan", "Petr", "Krystof"]
```


```python
print(jmeno_1, jmeno_2, jmeno_3, zbytek_jmen, sep="\n")
```


```python
prvni_jmeno, *zbytek = ["Matous", "Marek", "Lukas", "Jan"]
```


```python
print(prvni_jmeno, zbytek, sep='\n')
```


```python
print(zbytek[0])
```


```python
jmeno_souboru, *zbytek = 'MAIN-INFO-UBUNTU-Toto je loggovaci zprava'.split('-', maxsplit=1)
```


```python
print(jmeno_souboru)
```

    MAIN


<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s *uživatelskými funkcemi* a *vícenásobné přiřazování*:

1. Nahraj knihovny `pprint` a `collections`,
2. vytvoř definici funkce `vyber_plnolete_klienty`, která potřebuje jedinný parametr `klient: tuple`,
3. tato funkce opět vrací datový typ `tuple`,
4. účelem funkce je projít zadané pole a vybrat pouze ty klienty, kteří jsou starší 18 let,
5. vrácenou hodnotu ulož do proměnné `plnoleti`,
6. z proměnné `plnoleti` přiřaď poslední záznam do proměnné `posledni_plnolety` pomocí vícenásobného přiřazování.


```python
from pprint import pprint
from collections import namedtuple

Klient = namedtuple('Klienti', field_names=['krestni_jmeno',
                                            'prijmeni',
                                            'email',
                                            'vek'])
vsichni_klienti = (
    Klient(krestni_jmeno='Matouš', prijmeni='Holinka', email='matous@holinka.com', vek=30),
    Klient(krestni_jmeno='Lukáš', prijmeni='Holinka', email='lukas.holinka@gmail.com', vek=20),
    Klient(krestni_jmeno='Petr', prijmeni='Svetr', email='psvetr@email.cz', vek=16),
    Klient(krestni_jmeno='Marek', prijmeni='Párek', email='parekm@seznam.cz', vek=14)
)
```


```python
pprint(posledni_plnolety)
```

<details>
  <summary>▶️ Klikni zde pro zobrazení řešení</summary>
   
```python
from pprint import pprint
from collections import namedtuple

Klient = namedtuple('Klienti', field_names=['krestni_jmeno',
                                            'prijmeni',
                                            'email',
                                            'vek'])
vsichni_klienti = (
    Klient(krestni_jmeno='Matouš', prijmeni='Holinka', email='matous@holinka.com', vek=30),
    Klient(krestni_jmeno='Lukáš', prijmeni='Holinka', email='lukas.holinka@gmail.com', vek=20),
    Klient(krestni_jmeno='Petr', prijmeni='Svetr', email='psvetr@email.cz', vek=16),
    Klient(krestni_jmeno='Marek', prijmeni='Párek', email='parekm@seznam.cz', vek=14)
)


def vyber_plnolete_klienty(klienti: tuple) -> tuple:
    """
    Vrať nezměnitelné pole, které obsahuje jen takové klienty, kteří
    jsou stařší 18 let.

    :param klienti: Pole všech klientů,
    :type klienti: tuple
    :return: pole plnoletých klientů,
    :rtype: tuple
    """
    return tuple(
        klient
        for klient in klienti
        if klient.vek > 18
    )
        

plnoleti = vyber_plnolete_klienty(vsichni_klienti)
_ , posledni_plnolety = plnoleti
```
</details>

<br>

➡️ ➡️ **Formulář pro Tvoje hodnocení** [**sedmé lekce**](https://forms.gle/kBLzN7YJFJemaSQV8) ⬅️ ⬅️

<br>

<br>

<img src="https://www.creativefabrica.com/wp-content/uploads/2021/07/21/Homework-icon-Graphics-14972340-1.jpg" width="400" style="margin-left:auto; margin-right:auto">

## Domácí úkol

---

Napiš funkci, která bude umět převádět označení typu bytu (**byt0001**, **byt0003**):
```
byt0001,55m2,Olomouc,ul.Heyrovského,
byt0003,65m2,Olomouc,ul.Novosadský_dvůr,
```


```python
vzor = {
    "byt0001": "1+1",
    "byt0002": "2+1",
    "byt0003": "2+kk",
    "byt0004": "3+1",
    "byt0005": "3+kk",
    "byt0006": "4+1",
    "byt0007": "4+kk",
}
```

Funkce musí umět extrahovat údaj a pak jej převést:
```
byt0001,55m2,Olomouc,ul.Heyrovského,
byt0003,65m2,Olomouc,ul.Novosadský_dvůr,
...
```

výstup bude vypadat jako:
```
1+1,55m2,Olomouc,ul.Heyrovského,
2+kk,65m2,Olomouc,ul.Novosadský_dvůr,
...
```   

[Formulář po sedmé lekci](https://forms.gle/reGzS39hSDetatpE7)

---
