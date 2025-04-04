# Python akademie

---

<br>

## Obsah lekce
---

1. [Vstupy uživatelských funkcí](#Vstupy-funkcí),
2. [funkční rámce](#Rámce),
3. [funkce jako objekt](#Funkce-jako-objekt),
4. [domácí úkol](#Domácí-úkol).

---

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.qpcc6K7Yys3TFhifE4tuywHaHa%26pid%3DApi&f=1&ipt=b330b6e19fba2fceb06c29cb1f32b58d348ccefa9c27b39dedc996951b8c0588&ipo=images" width='300' style="margin-left:auto; margin-right:auto" />

## Vstupy funkcí

---

*Vstupem* pro uživatelskou funkci obecně můžeš rozumět:
1. **Parametry**, sloužící jako obecné proměnné při definici,
2. **argumenty**, tedy konkrétní hodnoty, které vkládáš při spouštění.


```python
cela_zprava = '2006-02-08 22:20:02,165: ESHOP.app:NOVA-OBJEDNAVKA: Vytvářím novou objednávku..'
```

<details>
  <summary>▶️ Cheat sheet ke knihovně typing</summary>
   
[https://www.remnote.com/a/typing/6720c85810f2334581acc922](https://www.remnote.com/a/typing/6720c85810f2334581acc922)
</details>


```python
def ziskej_zpravu_z_logu(zaznam: str) -> list:
    """
    Vrať zprávu pouze zprávu ze zadaného logu.
    """
    return zaznam.split(":")[-2:]
```


```python
print(ziskej_zpravu_z_logu(cela_zprava))
```

<br>

Vstupy do funkcí ale nemusíš skládat pouze pořadí.

Existuje dokonce několik vzorů, které můžeš vyzkoušet.

<br>

Důvod je prostý, každá *uživatelská funkce* je trochu jiná.

Proto existuje tento seznam různých vzorů:
* **poziční parametry** (argumenty),
* **klíčové argumenty**,
* **defaultní parametry**,
* **position-only** parametry,
* **\*args**,
* **\*\*kwargs**.

### Poziční parametry

---

Zejména je patrné, že v této variantě záleží na pozici (tedy pořadí), ve kterém parametry (i argumenty) zapíšeš:


```python
def uloz_informace(jmeno: str, prijmeni: str, telefon: str) -> dict:
    return {
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "telefon": telefon
    }
```


```python
print(uloz_informace("Matouš", "Holinka", "+420 777 666 555"))
```

V ukázce vidíš, že parametry jsou uspořádané **za sebou**.

Jednotlivé argumenty jsou potom zapsané **v odpovídajícím pořadí**:

| Pozice | Parametr | Argument |
| :-: | :-: | :-: |
| 1 | jmeno | "Matouš" |
| 2 | prijmeni | "Holinka" |
| 3 | telefon | "420 777 666 555" |

<br>

Jde o jednu **z nejpoužívanějších a nejznámějších variant**.

Takže pokud není komplikované pochopit, jaký *argument* patří do jakého *parametru*, budeš chtít zapsat vstupy touto formou.

Současně je ale nutné dbát na fakt, že ne vždy je patrné, který argument patří **ke kterému parametru**.


```python
print(uloz_informace("Holinka", "Matouš", "+420 777 666 555"))
```

<br>

### Klíčové argumenty

---

Zapisování *podle pozice* nemusí být ale vždy přehledné.

Třeba pokud jsou všechny tři parametry **stejného datového typu** (`int`) a ještě jsou samotné **hodnoty podobné**:


```python
def uloz_informace(jmeno: str, prijmeni: str, telefon: str) -> dict:
    return {
        "jmeno": jmeno,
        "prijmeni": prijmeni,
        "telefon": telefon
    }
```


```python
print(uloz_informace("Matouš", "Holinka", "+420 777 666 555"))
```


```python
print(uloz_informace("Holinka", "Matouš", "+420 777 666 555"))
```

V okamžiku, kdy přestává být pořadí patrné, nebo zapamatovatelné, je vhodné pracovat **s klíči**.
<br>

Platí to třeba pro rovnice, nebo objekty, kde se zkrátká hůře orientuješ.

Právě v takovém případě je velice příhodné přiřadit jednotlivé hodnoty **explicitně k příslušným parametrům**:


```python
print(uloz_informace(jmeno="Matouš", prijmeni="Holinka", telefon="+420 777 666 555"))
```


```python
print(uloz_informace(prijmeni="Holinka", telefon="+420 777 666 555", jmeno="Matouš"))
```

<br>

Pomocí *klíčových argumentů* se zápis prodlouží.

Proto je občas vhodné, udělat spuštění funkce **ještě přehlednější** pomocí zápisu pod sebou:


```python
print(uloz_informace(prijmeni="Holinka",
                     telefon="+420 777 666 555",
                     jmeno="Matouš"))
```

<br>

Takže pokud budeš mít **větší množství parametrů**, nebo se v nich budeš ztrácet, určitě použij tuto variantu.

<br>

### Defaultní parametry

---

Někdy dojdeš k závěru, že *uživatelská funkce*, kterou tvoříš, potřebuje alespoň **jeden parametr**, který bude ve většině spouštění používat tutéž hodnotu.

V takovém případě můžeš do předpisu zapsat *defaultní parametr*:

<details>
  <summary>▶️ Cheat sheet k urllib.parse</summary>
   
[https://www.remnote.com/a/urllib.parse/6720a9c210f2334581a9b2a9](https://www.remnote.com/a/urllib.parse/6720a9c210f2334581a9b2a9)
</details>


```python
from urllib.parse import urljoin
```


```python
def vytvor_adresu(cesta: str,
                  host: str = "https://www.brickranker.com") -> str:
    return urljoin(host, cesta)
```


```python
print(vytvor_adresu("rankings"))
```

<br>

Při spuštění funkce `vytvor_adresu` je přítomen **pouze jeden argument** a funkci lze přesto spustit.


```python
print(vytvor_adresu("news"))
```

<br>

Takže pokud **nevložíš žádný argument**, bude funkce `vytvor_pozdrav` automaticky pracovat se stringem `"https://www.brickranker.com"`.

Pokud se však rozhodneš, že tebou zadaný **defaultní parametr** bude potřeba upravit, můžeš jej snadno přepsat jinou hodnotou:


```python
print(vytvor_adresu("prehled-kurzu", "https://engeto.cz"))
```


```python
print(vytvor_adresu(cesta="kontakt", host="https://engeto.cz"))
```

<br>

*Defaultní parametry* je potřeba zadávat **až po pozičních parametrech**:


```python
def vytvor_adresu_spatne(base_url: str = "https://www.brickranker.com",
                         url_path: str) -> str:
    return urljoin(base_url, url_path)
```


```python
def vytvor_firemni_adresu(jmeno: str,
                          prijmeni: str,
                          domena: str = 'superfirma.cz') -> str:
    print(domena)
    print(domena)
    return f"{jmeno[0].lower()}.{prijmeni.lower()}{domena}"
```


```python
print(vytvor_firemni_adresu(jmeno='Marek', prijmeni='Petr'))
```

<br>

### Jen poziční parametry

---

Od verze **Pythonu 3.8** je dostupná tato nová varianta pro zápis parametrů u *uživatelských funkcí*:


```python
def vypis_pozdrav(jmeno: str, /, je_uzivatel: bool) -> None:
    if je_uzivatel:
        print("Ahoj,", jmeno)
    else:
        print("Nejsi uživatel!")
```


```python
vypis_pozdrav("Matouš", je_uzivatel=True)
```


```python
vypis_pozdrav("Matouš", True)
```

<br>

Účelem tohoto typu **zápisu argumentů** je **vynutit od uživatele** zápis všech parametrů nalevo od lomítka `/` jako **poziční argumentů**:


```python
vypis_pozdrav(jmeno="Matouš", je_uzivatel=True)
```


```python
vypis_pozdrav(jmeno="Matouš", True)
```

Zatím co parametry napravo od lomítka můžeš:
* zapsat jako **poziční**,
* zapsat jako **klíčové**.

Kde se s tímto zápisem můžeš setkat:


```python
# help(float)
```


```python
float(x="3.141")
```


```python
float("3.141")
```

Vzhledem k tomu, že je to novější varianta **není tolik běžná**.

Spatřit ji můžeš tehdy, pokud chce programátor ostatní uživatele jeho uživatelských funkcí omezit při používání **klíčových argumentů**.

### *args

---

Pokud znáš jiné programovací jazyky (jako C nebo C++), možná v tobě znak `*` připomene tzv. *pointery*:
```c
int *pointer_c, c;
c = 11;
pointer_c = &c;

printf("Hodnota pointer_c: %d\n", c);    // 'Hodnota pointer_c: 11'
printf("Hodnota c: %d\n\n", *pointer_c); // 'Hodnota c: 11'
```

Nicméně Python tuto funcionalitu **nepodporuje**.

<br>

Naopak pomáhá v rámci parametrů oznámit interpretu, že funkce umí pracovat **s různým množstvím argumentů**:


```python
def vypocitej_prumer(args):
    return sum(args) / len(args)
```


```python
print(vypocitej_prumer(1, 2, 3, 4, 5))
```

<br>

Zásadní je právě přítomnost `*`. Ta sbalí hodnoty **do sekvence**:


```python
def vypocitej_prumer(*args):
    return sum(args) / len(args)
```


```python
print(vypocitej_prumer(1, 2, 3, 4, 5))
```

<br>

Jméno parametru `args` potom slouží hlavně jako konvence mezi programátory.

V ukázce můžeš klidně použít **jiné jméno**:


```python
def vypocitej_prumer(*cislice):
    return sum(cislice) / len(cislice)
```


```python
print(vypocitej_prumer(1, 2, 3, 4, 5, 6))
```

<br>

Můžeš namítnout, že podobnou situaci můžeš řešit rovnou pomocí **sekvenčního datového typu**:


```python
from typing import Tuple
```


```python
def vypocitej_prumer(cislice: Tuple[int]) -> float:
    return sum(cislice) / len(cislice)
```


```python
cislice = (1, 2, 3, 4, 5, 6, 7)
```


```python
print(vypocitej_prumer(cislice))
```

<br>

Často ale **nemáš/nebudeš možnost si takhle proměnnou pěkně nachystat** (*uložit*).

Třeba tehdy, pokud ti někdy číselné řady posílá, aktuální a s různou délkou:


```python
def vypocitej_prumer(cislice):
    return sum(cislice) / len(cislice)
```


```python
print(
    vypocitej_prumer(1, 2),
    vypocitej_prumer(1, 2, 3),
    vypocitej_prumer(1, 2, 3, 4),
    sep="\n"
)
```


```python
def vypocitej_prumer(*args):
    return sum(args) / len(args)
```


```python
print(
    vypocitej_prumer(1, 2),
    vypocitej_prumer(1, 2, 3),
    vypocitej_prumer(1, 2, 3, 4),
    sep="\n"
)
```

Nyní funkci `vypocitej_prumer` zapsanou hvězdičkou oznamuješ, že parametr `args` může mít jakýkoliv počet hodnot.


```python
print("a", "b")
print(("a", "b"))
```

<br>

### **kwargs

---

Dalším způsobem pro *zápis vstupů*, je varianta **pomocí dvou hvězdiček** `**`.

<br>

Tentokrát seskupuješ dohromady libovolném množství párů:
1. **jména objektů, klíčů**,
2. **jejich hodnot**.

Opět si představ situaci, že postupně dostáváš hodnoty, které potřebuješ schovávat do slovníku:


```python
def vytvor_slovnik(**kwargs) -> None:
    """
    Vypiš slovník, který obsahuje libovolné množství sbalených hodnot. 
    """
    for klic, hodnota in kwargs.items():
        print(klic.upper(), hodnota, sep=":")
```


```python
vytvor_slovnik(jmeno="Matous")
```


```python
vytvor_slovnik(jmeno="Matous", prijmeni="Holinka")
```

<br>

**Jméno parametru** je opět volitelné, ale je doporučováno, držet se všeobecné konvence `kwargs` (~keyword arguments):


```python
def vytvor_slovnik(**osobni_udaje):
    """
    Vypiš slovník, který obsahuje libovolné množství sbalených hodnot. 
    """
    detaily_uzivatele = dict()
    
    for klic, hodnota in osobni_udaje.items():
        detaily_uzivatele[klic.upper()] = hodnota
                                               
    return detaily_uzivatele
```


```python
from pprint import pprint
pprint(vytvor_slovnik(
        jmeno="Matous",
        prijmeni="Holinka",
        vek=90,
        email="matous@holinka.cz"
))
```


```python
print(vytvor_slovnik(
        jmeno="Matous",
        vek=90,
        email="matous@holinka.cz"
))
```

<br>

### Souhrn

---

Aby v tom byl alespoň částečně pořádek, níže je uvedená tabulka se **základními charakteristikami**.

| Typ vstupu | Ukázka | Kdy používat |
| :- | :- | :- |
| **poziční vstupy** | `moje_funkce(jmeno, prijmeni)` | ve většině případech, kde není matoucí **pořadí** argumentů, | 
| **klíčové argumenty** | `moje_funkce(jmeno="Tom", prijmeni="Hrom")` | pokud je pořadí argumentů **nepřehledné**, pojmenuj je, |
| **defaultní parametry** | `moje_funkce(email, registrovany=True)` | pokud potřebuješ při spouštění stejný parametr, napiš jej jako *defaultní*, |  
| **position-only parametry** | `moje_funkce(jmeno, /, registrovany)` | pokud potřebuješ vynutit zápis **pozičního argumentu**, |
| **\*args** | `moje_funkce(*args)` | pokud má funkce pracovat **s různým množstvím** hodnot v *sekvenci*, |
| **\*\*kwargs** |  `moje_funkce(**kwargs)` | pokud má funkce pracovat **s různým množstvím** hodnot v párech *klíč*, *hodnota*. |

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s *uživatelskými funkcemi*:

1. Vytvoř definici uživatelské funkce `spoj_slova`,
2. funkce bude pracovat s parametrem `*args`, který bude obsahovat různé množství stringových hodnot,
3. funkce ověří, že `*args` není prázdný, jinak vrací `None`,
4. pokud  `*args` není prázdný, spoj jednotlivá slova, třeba pomocí pomlčky `-`,
5. spojenou stringovou hodnot z funkce vrať.
6. funkce vrací datový typ `tuple`,


```python
from typing import Optional
```


```python
def spoj_slova(*args, spojovac: str = '-') -> Optional[str]:
    if not args:
        return None

    return spojovac.join(args)
```


```python
'#'.join(('s', 'a', 'b'))
```


```python
print(spoj_slova("Hello","world", "!"))  # Výstup bude "Hello-world-!"
```


```python
print(spoj_slova("Ahoj","všem!"))        # Výstup bude "Ahoj-všem!"
```

<details>
  <summary>▶️ Klikni zde pro zobrazení řešení</summary>
   
```python
from typing import Optional


def spoj_slova(*args) -> Optional[str]:
    if not args:
        return None

    return "-".join(args)

print(spoj_slova("Hello","world", "!"))  # Výstup bude "Hello-world-!"
print(spoj_slova("Ahoj","všem!"))  # Výstup bude "Ahoj-všem!"
```
</details>

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.3zH2XO4Ec77ugwOJQSR5KAHaGl%26pid%3DApi&f=1&ipt=da0860e815b2df5c7483ba605846462ead01ddc816a6391c7a24853c7354c4d4&ipo=images" width="350" style="margin-left:auto; margin-right:auto" />

## Rámce

---

*Scope* nebo také rámec je koncept, na kterém pracuje spousta programovacích jazyků, Python není výjimkou.

Rámec v podstatě řeší tuto otázku: **"K jakým proměnným mám v tuto chvíli přístup?"**

### Globální rámec

---


```python
print(jmeno)
```

Po spuštění předchozí buňky s funkcí `print` dostaneme chybu s argumentem: `name 'jmeno' is not defined`.

Důvodem je **absence proměnné** `jmeno`.

Tento problém lze ale popsat jako chybějící `jmeno` v **aktualním rámci**.


```python
jmeno = "Matouš"
```


```python
print(jmeno)
```

Teprve nyní tvoříš odkaz/ukazatele na hodnotu stringu `"Matouš"`.

Současně tím **v globálním rámci** zapíšeš proměnnou `jmeno`.

Ověřit si, které proměnné máme dostupné v aktuálním globalním rámci můžeme pomocí funkce `globals`:


```python
from pprint import pprint
# pprint(globals())
```

##### Demo: V příkazovém řádku

<br>

### Lokální rámec

---


```python
def nedelej_vubec_nic():
    # global dalsi_jmeno
    dalsi_jmeno = "Lukas"
```


```python
nedelej_vubec_nic()
```


```python
print(dalsi_jmeno)
```

Opět výstup: `name 'dalsi_jmeno' is not defined`.

Tentokrát však máš proměnnou `dalsi_jmeno` předepsanou.

<br>

Proměnná jmeno tentokrát existuje, ale pouze **v lokálním rámci** funkce `nedelej_vubec_nic`.

*Lokální rámec* není *globalní rámec*. Proto nemůžeš použít proměnnou `dalsi_jmeno` v **globálním rámci**, pokud je vytvořená v **lokálním rámci**.


```python
def nedelej_nic_znovu():
    treti_jmeno = "Lukáš"
    print(treti_jmeno)
```

Pokud potřebuješ zpřístupnit proměnnou `treti_jmeno` uvnitř funkce, musíš použít funkci `print` **v daném lokálním rámci**.


```python
nedelej_nic_znovu()
```

Co funkce, to nový **lokální rámec**.

Každá funkce ma **svůj vlastní lokální rámec**.

Jednotlivé *lokální rámce* jsou od sebe izolované (nevidí proměnné ostatních funkcí).

**To je jejich největší výhoda, pracují totiž odděleně.**

<br>

*Lokální rámce* souvísí s funkcemi, ne **s odsazeným zápisem**:


```python
ctvrte_jmeno = "Matouš"
```


```python
if ctvrte_jmeno == "Matouš":
    prijmeni = "Holinka"
```


```python
pprint('Holinka' in globals().values())
```

Pokud chceš ověřit, jaké proměnné máš v daném **lokalním rámci**, použij uvnitř konkretního prostředí funkci `locals`:


```python
def vypis_cele_jmeno():
    """
    Funkce LOCALS bude pracovat jen uvnitř funkce.
    """
    jmeno = "Lukáš"
    prijmeni = "Holinka"
    print("Lokální rámec:", locals())
```


```python
vypis_cele_jmeno()
```

<br>

Naproti tomu, rámec funkce `vypis_cele_jmeno_znovu` neeviduje globální proměnnou:


```python
krestni_jmeno = "Matouš"


def vypis_cele_jmeno_znovu():
    """
    Funkce LOCALS bude pracovat jen uvnitř funkce.
    """
    jmeno = "Lukáš"
    prijmeni = "Holinka"
    print("Lokální rámec:", locals())
```


```python
vypis_cele_jmeno_znovu()
```


```python
print(globals()['krestni_jmeno'])
```

<br>

Pokud budeš mít uživatelských funkcí víc, můžeš pozorovat, jak žádná nevidí do jiné funkce:


```python
def zapis_zahlavi(jmeno):
    datum = "11/11/2011"
    print("Lokální rámec 'zapis_zahlavi':", locals())
    return f"{datum}-{jmeno}"
```


```python
def zapis_zpravu(hlavicka, text):
    print("Lokální rámec 'zapis_zpravu':", locals())
    return f"{hlavicka}: {text}"
```


```python
zahl = zapis_zahlavi("Matouš")
```


```python
zprava = zapis_zpravu(zahl, "Ahoj všichni!")
```

Tudíž nejsi obyčejně schopen ve funkci `zapis_zpravu` použít parametr `jmeno` atd.


```python
def zapis_zpravu(hlavicka: str) -> str:
    return hlavicka
```


```python
globalni_hlavicka = zapis_zpravu('---')
```


```python
print(globals()['globalni_hlavicka'])
```

<br>

### Zabudovaný rámec (~built-in scope)

---

Tento rámec obsahuje všechny *výjimky*, *zabudované funkce*, aj:


```python
print(sum)
```

Máš jej k dispozici okamžitě, po spuštění *interpretu*, takže můžeš použít objekty, které má k dispozici.


```python
import builtins
```


```python
dir(builtins)
```

Takže to jsou **3 základní rámce** v Pythonu:

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.PyAwJkVFGp6IVXtRpQXaowHaE6%26pid%3DApi&f=1&ipt=113d12a3bc2e90ece37b5ab11754b3e28c8bfca59a154810dc08376f9ee634e8&ipo=images" width="350">

### Uzavírající rámec (~enclosing scope)

---

Jde o téma pouze **pro ostřílenější pythonisty.**

Celé to vypadá jako jedna *uživatelská funkce* **zanořená** do jiné *uživatelské funkce*:


```python
def rozdel_podle_znaku(adresa, znak="@"):  # Uzavírající rámec
    rozdeleny_mail = adresa.split(znak)
    
    def oddel_domenu(nedomena, znak="."):  # Lokální rámec
        return nedomena[1].split(znak)[0]
    
    return oddel_domenu(rozdeleny_mail) 
```


```python
print(rozdel_podle_znaku("matous@holinka.cz"))  # ['holinka', 'cz']
```

Tedy původní *lokální rámec* se mění na *uzavírající rámec* tehdy, pokud uvnitř funkce (`rozdel_podle_znaku`) najdeš jinou, uzavřenou funkci (`oddel_domenu`).

Aplikace této složitější tématiky pak lze dohledat u:
1. *Closures*,
2. [*dekorátorů*](https://gist.github.com/Bralor/ea1c0a0430aacf2f71625ee8be1c1ddd).

#### Ukázka dekorátoru (~enclosing scope)

---


```python
def muj_dekorator(func: callable):
    def obalovaci_ohlaseni(*args, **kwargs):
        print('Začínám spouštět funkci')
        vystup = func(*args, **kwargs)
        print('Ukončuji celý průběh')
        return vystup
    return obalovaci_ohlaseni
```


```python
@muj_dekorator
def vytvor_pozdrav(jmeno: str) -> None:
    print(f"Ahoj, {jmeno}!")
```


```python
vytvor_pozdrav("Monika")
```


```python
# --> pole: 'm'
```

<br>

### Shrnutí rámců

---

Proč je tedy znalost a pochopení **pravidel rámců** tak důležitá?


```python
prostredi = "globalni"

def funkce_a():
    prostredi = "uzavirajici"

    def funkce_b():
        prostredi = "lokalni"
        print(prostredi)

    funkce_b()
funkce_a()
```

<br>

V okamžiku, kdy **nedodržuješ zdravé koncepty práce s rámci**, se můžeš snadno spálit.


```python
# prostredi = "globalni"        # Přejmenovat a odstranit

def funkce_a():
    # prostredi = "uzavirajici" # Odstranit

    def funkce_b():
        # prostredi = "lokalni" # Odstranit
        print(prostredi)

    funkce_b()
funkce_a()
```

*Interpret* totiž dodržuje následující postup:
1. Nejprve prohledá **lokalní rámec**, v němž se nachází,
2. pokud není objekt uvnitř, zkus **uzavírající rámec** nebo obecně **nadřazený rámec**,
3. pokud není objekt uvnitř **uzavírajícího prostředí**, zkus **globální rámec**,
4. pokud není objekt uvnitr **globálního**, zkus **zabudovaný rámec**,
5. pokud není objekt uvnitř **zabudovaného rámce** vyvolej `NameError`.

Spoléhat však na toto chování **není doporučováno**. Je totiž neintuitivní.

Proto je dobré pamatovat na poučku, že **pěkná uživatelská funkce** umí pracovat pouze:
1. svými **proměnnými**,
2. svými **parametry**.


```python
def funkce_a(prostredi):

    def funkce_b(prostredi):
        print(prostredi)
    
    funkce_b(prostredi)
```


```python
funkce_a("globalni")
```

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s *uživatelskými funkcemi*:

1. Vytvoř definici uživatelské funkce `preved_format_na_kapitalku`,
2. ta pracuje s jedním parametrem `text`,
3. zadanou hodnotu v parametru `text` převede slovo po slovu na *Capitalize* formát (tedy `'ahoj'` na `'Ahoj'`),
4. nakonec převedenou hodnotu z funkce `preved_format_na_kapitalku` vrať,
5. vytvoř definici uživatelské funkce `zobraz_text`,
6. funkce `zobraz_text` pracuje s jedním parametrem `zadany_text`,
7. tento zadaný text naformátuje a vypíše do věty: `Formátovaný text: Toto Je Ukázkový Text`.


```python

```


```python
zadany_string = "toto je ukázkový text"
naformatovana_zprava = preved_format_na_kapitalku(zadany_string)
zobraz_text(naformatovana_zprava)
```

<details>
  <summary>▶️ Klikni zde pro zobrazení řešení</summary>
   
```python
def preved_format_na_kapitalku(text: str) -> str:
    return ' '.join(word.capitalize() for word in text.split())


def zobraz_text(zadany_text: str):
    print(f"Formátovaný text: {zadany_text}")


zadany_string = "toto je ukázkový text"
naformatovany_text = preved_format_na_kapitalku(zadany_string)
zobraz_text(naformatovany_text)
```
</details>

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Q_UFkYOMsF4WZPqR5JASrwHaHa%26pid%3DApi&f=1&ipt=5cc98c3ef4fcc27589e45d9966d8c05f1d7723927ad5c59a0f82d2e753d14ba8&ipo=images" width="200" style="margin-left:auto; margin-right:auto" />

## Funkce jako objekt
---


*Uživatelské funkce* v Pythonu jsou *objekt* jako všechny ostatní.

Podle toho s nimi lze také zacházet:
1. Funkce umí zacházet **s obyčejnými datovými typy** jako vstupy,
2. funkce umí zacházet **s jinými funkcemi** jako vstupy,
3. funkce umí vracet **různé datové typy**,
4. funkce umí vracet **jiné funkce**.

### Běžná uživatelská funkce

---

V ukázce napiš klasickou *uživatelskou funkci*, která prochází libovolné množství stringů (jmen).

Ty potřebuješ vypsat **všechny velkými písmeny**:


```python
def vypis_jmeno(*args):
    for jmeno in args:
        print(jmeno.upper())  # str --> AttributeError
```


```python
vypis_jmeno("matouš", "marek", "jan", "lukáš")
```

<br>

### Funkce jako vstup

---

Nejenom hodnoty můžeš zapisovat jako vstupní parametry.

Také funkce lze takhle zapsat.

Proto se také uznačují jako **funkce vyššího řádu**. Tedy:

- **Přijímá jednu nebo více funkcí jako argumenty**,
- **Vrací funkci jako svůj výstup**.


```python
zamestnanci = ({'jmeno': 'Matouš', 'mzda': 40_000},
               {'jmeno': 'Petr', 'mzda': 50_000})
```


```python
def navys_mzdu(zamestnanec: dict, navyseni: int) -> dict:
    if not zamestnanec:
        return None

    zamestnanec['mzda'] += navyseni
    return zamestnanec
```


```python
# navys_mzdu(zamestnanec={'jmeno': 'Matouš', 'mzda': 40_000},  # namedtuple
#            navyseni=500)
```


```python
def navys_mzdu_vsem_zamestnancum(
    zamestnanci: tuple,
    navysovaci_fce: callable
) -> list:
    navysene_mzdy = list()

    for zamestnanec in zamestnanci:
        upravena_mzda = navysovaci_fce(zamestnanec=zamestnanec,
                                       navyseni=10_000)
        navysene_mzdy.append(upravena_mzda)

    return navysene_mzdy
    
    # return [navys_mzdu(zamestnanec=zamestnanec, navyseni=10_000)
    #         for zamestnanec in zamestnanci]
```


```python
po_navyseni = navys_mzdu_vsem_zamestnancum(zamestnanci=zamestnanci,
                                           navysovaci_fce=navys_mzdu)
```


```python
po_navyseni
```

### Funkce vrací hodnoty

---

Nyní zapiš *uživatelskou funkci*, která vrátí klíče zadaného slovníku (spojené jako string):


```python
def vypis_klice(udaj):
    if isinstance(udaj, dict):
        return ", ".join(udaj.keys())
```


```python
vypis_klice({"jméno": "Matouš"})
```


```python
vypis_klice({"jméno": "Matouš", "příjmení": "Holinka"})
```

### Funkce vrací funkce

---

Tentokrát může funkce získat parametry různého datového typu (`list` a `dict`), proto musíš zpracovat klíče **dvěma způsoby**:


```python
from typing import Union
```


```python
#def vypis_klice(udaj: Union[dict, list]):
def vypis_klice(udaj: list | dict):  # Union[dict, list]
    if isinstance(udaj, dict):
        return ziskej_klice_ze_slovniku(udaj)

    elif isinstance(udaj, list):
        return ziskej_klice_z_listu(udaj)
```


```python
def ziskej_klice_ze_slovniku(slovnikovy_udaj: dict) -> str:
    return ", ".join(slovnikovy_udaj.keys())
```


```python
def ziskej_klice_z_listu(list_udaj: list):
    klice = set()

    for udaj in list_udaj:
        if not isinstance(udaj, dict):
            continue

        for jmeno in udaj.keys():
            klice.add(jmeno)
    else:
        return ", ".join(klice)
```


```python
vypis_klice({"jméno": "Matouš", "příjmení": "Holinka"})
```


```python
vypis_klice([
        {"jméno": "Matouš", "email": "matous@holinka.cz"},
        {"jméno": "Marek", "příjmení": "Párek"},
        {"jméno": "Marek", "příjmení": "Párek", "věk": 11}
    ]
)
```

Místo aby funkce `vypis_klice` manipulovala pouze s jedním stringem, umí nyní procházet i slovníky v listu.

Pokud bude parametr datového typu:
1. `dict`, vytáhne jména klíčů pomocí metody,
2. `list`, vytáhne jména klíčů pomocí nestované smyčky.


Narozdíl od **obyčejných proměnných**, které by *uživatelská funkce* mimo parametr neměla upravovat, uživ. funkce takový prohřešek nejsou.

Dovnitř *uživatelských funkcí* sice nevidí, ale jejich odkazy (jména) *intepret* eviduje již při definici.

Pořád ale platí, že je nutné dávat pozor **na kolize ve jménech objektů**.

### Rekurzivní zápis

---

*Rekurzivní zápis* je takový, kdy **uživatelská funkce** volá (spouští) sebe sama.


```python
def secti_sekvenci_cisel(cisla: tuple):
    if len(cisla) == 1:
        return cisla[0]
    else:
        return cisla[0] + secti_sekvenci_cisel(cisla[1:])  # 1 + 2 + 3 + 4
```


```python
print(secti_sekvenci_cisel((1, 2, 3, 4)))
```


```python
print(secti_sekvenci_cisel((1, 2, 3, 4, 5)))
```


```python
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```


```python
for i in range(10):
    print(fibonacci(i))
```


```python
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)
```


```python
def show_whole_example(n):
    result = "1"
    if n <= 0:
        return result
    for i in range(1, n + 1):
        result += f" × {i}"
    return result

```


```python
for i in range(10):
    print(i, factorial(i), sep=":", end=" ")
    print(f"({show_whole_example(i)})")
```

Na většinu zadání v programování není optimální *rekurzivní zápis* funkce používat:
1. Pokud řešení zápisu **není elegantní** a působí **komplikovaně**,
2. ☢️ rekurze **bere více paměti** než nerekurzivní řešení ☢️,
3. runtime rekurzivního zápisu může **trvat delší dobu**.

Jsou ovšem scénaře, kde se naopak rekurze perfektně hodí.

Dokonce bude **stručnější a čitelnější**. Třeba procházení *stromových datových struktur*.


```python
nestovany_slovnik = {
    "jméno": "Matouš",
    "příjmení": "Holinka",
    # "práce_1": "222-333-444",
    # "práce_2": "444-333-222"
    # ...
    "kontakt": {
        "mail": "matous@holinka.com",
        "telefon": {
            "osobní": "111-222-333", 
            "služební": {
                "práce_1": "222-333-444",
                "práce_2": "444-333-222",   
            }
        }
    }
}
```


```python
def zplosti_nestovany_slovnik(
    nestovany_slovnik: dict
) -> dict:
    vysledek = dict()
    
    for klic, hodnota in nestovany_slovnik.items():
        if not isinstance(hodnota, dict):
            vysledek[klic] = hodnota
        else:
            vysledek.update(zplosti_nestovany_slovnik(hodnota))
    else:
        return vysledek
```


```python
vystup = zplosti_nestovany_slovnik(nestovany_slovnik)
```


```python
from pprint import pprint
pprint(nestovany_slovnik)
pprint(zplosti_nestovany_slovnik(nestovany_slovnik))
```

    {'jméno': 'Matouš',
     'kontakt': {'mail': 'matous@holinka.com',
                 'telefon': {'osobní': '111-222-333',
                             'služební': {'práce_1': '222-333-444',
                                          'práce_2': '444-333-222'}}},
     'příjmení': 'Holinka'}
    {'jméno': 'Matouš',
     'mail': 'matous@holinka.com',
     'osobní': '111-222-333',
     'práce_1': '222-333-444',
     'práce_2': '444-333-222',
     'příjmení': 'Holinka'}



```python
pprint("Matouš" in vystup.values())
```

<br>

#### Rekurzivně

---


```python
from timeit import timeit
```


```python
r_ohlaseni = """
print("Délka rekurzivní řešení:")
def vypocitej_faktorial_r(cislo):
    if cislo <= 1:
        return 1
    else:
        return cislo * vypocitej_faktorial_r(cislo - 1)
"""
```


```python
timeit("vypocitej_faktorial_r(10)", setup=r_ohlaseni, number=10_000_000)
```

    Délka rekurzivní řešení:





    5.901113525000255



<br>

#### Nerekurzivně

---


```python
ohlaseni = """
print("Délka nerekurzivní řešení:")
def vypocitej_faktorial(cislo):
    vracena_hodnota = 1
    for hodnota in range(2, cislo + 1):
        vracena_hodnota *= hodnota
    else:
        return vracena_hodnota
"""
```


```python
timeit("vypocitej_faktorial(10)", setup=ohlaseni, number=10_000_000)
```

    Délka nerekurzivní řešení:





    3.693549540999811



<br>

#### Funkce implementovaná v C

---


```python
c_ohlaseni = "from math import factorial\nprint('Délka řešení C funkcí:')"
```


```python
timeit("factorial(10)", setup=c_ohlaseni, number=10_000_000)
```

    Délka řešení C funkcí:





    0.3465202900006261



[Formulář po osmé lekci](https://forms.gle/VBacWAtdNAGU72kPA)

---

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.GMJvJ-GG0YS8H5JmHR3CbwHaHm%26pid%3DApi&f=1&ipt=110157bae9409977a59d895a970a6d51afa8a31e0c7fca53a1f95fd2402f9a35&ipo=images" width="200">

## Domácí úkol

---

Napiš soubor funkcí, které bude spouštět hlavní funkce `main`.

Tato funkce bude umět generovat captcha kód o libovolné délkce znaků.

Bude umět přidávat číselné znaky, malá písmena, velká písmena, podle zadání:
```
ZDngoM  # malá a velká písmena, délka 6 znaků
ngom    # malá písmena, délka 4 znaků
ZDng0   # malá, velká písmena, čísla , délka 5 znaků
```

Skript musí obsahovat tyto funkce:
1. `vrat_ciselne_znaky`,
2. `vrat_male_textove_znaky`,
3. `vrat_velke_textove_znaky`,
4. `vytvor_captchu`,
5. `vytvor_davku`, (*volitelné*)
6. `main`,

---
