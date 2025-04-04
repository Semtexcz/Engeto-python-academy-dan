## Úvod

---

1. [Další datové typy](##Další-datové-typy),
2. [Datový typ dictionary](#Datový-typ-dict-(~dictionary)),
3. [Datový typ set](#Datový-typ-set),
4. [Datový typ frozenset](#Datový-typ-frozenset),
5. [Volitelné argumenty](#Volitelné-argumenty),
5. [Domácí úkol](#Domácí-úkol).

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.RbCdrSpe208dpm4QsfhhhwHaGL%26pid%3DApi&f=1&ipt=0cb87e93ae327ef0f85f12f5e92e5104f67410c32a9277390d3f6bb4e838004e&ipo=images" width="200" />


## Další datové typy

---

Zatím znáš pouze několik vybraných **datových typů** (`int`, `float`, `str`, `list`, `tuple`, `bool`).

Umožní ti jednoduše pracovat při různých situacích.


```python
udaje = ("Matouš", "Holinka", "matous@holinka.com", "+420 777 666 555")
print(udaje[0])
```

Co když budeš potřebovat přistupovat k údajům v sekvenci *lépe* nebo *exaktněji*, než **pomocí indexů**.

Třeba má sekvence stovky indexů a v takovém případě se dříve upočítáš.


```python
emaily = [
    'h.vybíralová@firma.cz', 'w.štrumlová@firma.cz', 'm.vybíralová@firma.cz',
    's.bechyňka@firma.cz', 'z.urbánková@firma.cz', 'l.riečan@firma.cz',
    'v.koudelová@firma.cz', 'f.vorlová@firma.cz', 'i.seleš@firma.cz',
    'm.železný@firma.cz', 'p.niklesová@firma.cz', 'b.skok@firma.cz',
    'j.šmíd@firma.cz', 'j.procházková@firma.cz', 'd.hlavatá@firma.cz'
]
```

Co když máš dlouhou sekvenci, kde potřebuješ pracovat pouze **s unikátními hodnotami**?

Proto se dnes seznámíš s dalšími typy objektů, které se ti mohou hodit, pokud budeš pracovat s Pythonem.

<br>

Nejprve tedy *datový typ*, který ti dovolí označovat hodnoty lépe než pomocí indexu.

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.xflNvuQDVUlb2fSnRlvULgHaHa%26pid%3DApi&f=1&ipt=8ef18ba5e38de61f9dc03b35d60d0f65920f43ee0e6165fed821d9fcce0311d7&ipo=images" width="200" />


## Datový typ `dict` (~dictionary)

---

*Dictionary* (v Pythonu repr. `dict`) nebo také **slovník**:
* v jiných jazycích *hashtable*, *map*,
* v Pythonu **standartní datový typ**,
* tvořený páry `klíč: hodnota`,
* **nemá indexy** jako `list` a `tuple`, hranatá závorka pracuje odlišně,
* **nemají pořadí** (u menšího množství párů se to může zdát),
* **změnitelný** datový typ.


```python
uzivatel = {
    "jmeno": "Matouš",
    "vek": 100,
    "rid_opravneni": True,
    "volny_cas": ["klavír", "čtení", "Python!"]
}
```


```python
print(type(uzivatel))
```

    <class 'dict'>


* Podle **klíče** dohledávám (*~ mapuji*) **hodnotu** (ne naopak),


```python
print(uzivatel["jmeno"])
```

    Matouš



```python
# print(uzivatel[0])
```

Hranaté závorky u datového typu `dict` neslouží k *indexování*, nýbrž jako prostor zadat **jméno** klíče.


```python
print(uzivatel["vek"])
```

    100



```python
print(uzivatel["volny_cas"])
```

    ['klavír', 'čtení', 'Python!']



```python
print(uzivatel["rid_opravneni"])
```

    True


Opatrně na *mapování*. Funguje pouze pokud vyhledáváš **hodnotu podle klíče**:


```python
print(uzivatel["Matouš"])
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-9-52addb5b1c15> in <module>
    ----> 1 print(uzivatel["Matouš"])
    

    KeyError: 'Matouš'


* klíč musí být **unikátní** (`str`, `int`, `bool`, nelze použít `list`)(pomůcka s funkcí `hash`),
* hodnota nemusí být unikátní (př. `str`, `int`, `list`, `tuple`, jiný `dict`).


```python
uzivatel_2 = {["jmeno", "heslo"]: ["Matouš", "Holinka"]}
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-10-fabaf8cbb5d2> in <module>
    ----> 1 uzivatel_2 = {["jmeno", "heslo"]: ["Matouš", "Holinka"]}
    

    TypeError: unhashable type: 'list'



```python
print(hash(["jmeno", "heslo"]))
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-11-45347e9be0df> in <module>
    ----> 1 print(hash(["jmeno", "heslo"]))
    

    TypeError: unhashable type: 'list'


Hašovat tedy můžeš jen nezměnitelné (*immutable*) datové typy:


```python
print(hash(("jmeno", "heslo")))
```

    -2536092688205852161


Funkci `hash` můžeš použít jako takového pomocníka na začátek.

Pokud ti vrátí celé číslo, je zadaný datový typ *hashovatelný*.

Tedy můžeš jej použít jako *klíč*.

### Nový slovník


```python
novy_uzivatel_1 = dict()
novy_uzivatel_2 = {}
```


```python
print(type(novy_uzivatel_1))
print(type(novy_uzivatel_2))
```

    <class 'dict'>
    <class 'dict'>



```python
print(id(novy_uzivatel_1))  # ?
print(id(novy_uzivatel_2))
```

    140659999349312
    140660008307520


### Přidávání dat


```python
novy_uzivatel_1["jmeno"] = "Petr"
```


```python
print(novy_uzivatel_1)
```

    {'jmeno': 'Petr'}



```python
novy_uzivatel_1["rid_opravneni"] = True
novy_uzivatel_1["hobby"] = ("fotbal", "hry", "pratele")
novy_uzivatel_1["vek"] = 22
```


```python
print(novy_uzivatel_1)
```

    {'jmeno': 'Petr', 'rid_opravneni': True, 'hobby': ('fotbal', 'hry', 'pratele'), 'vek': 22}


Pokud vložíš **jinou hodnotu** do **existujícího klíče**, *přepíšeš* původní hodnotu:


```python
novy_uzivatel_1["jmeno"] = "Marek"
```


```python
print(novy_uzivatel_1)
```

    {'jmeno': 'Marek', 'rid_opravneni': True, 'hobby': ('fotbal', 'hry', 'pratele'), 'vek': 22}



```python
print(hash(1))
print(hash(1.0))
```

    1
    1


### Zanořené ("Nestované hodnoty"), získávání hodnot


```python
uzivatel_3 = {
    "jmeno": "Lukáš",
    "prijmeni": "Holinka",
    "vek": 28,
    "hobby": ("fotbal", "hry", "pratele"),
    "kontakt": {
        "telefon": "000 123 456 789",
        "email": "lukas@gmail.com",
        "web": "www.lukas.cz"
    }
}
```


```python
# Vyber emailovou adresu na Lukáše
print(uzivatel_3["kontakt"]["email"])
```

    lukas@gmail.com


### Metody slovníků

| Metoda          | Vysvětlení                                                       | Příklad                                              |
|-----------------|-------------------------------------------------------------------|------------------------------------------------------|
| `dict.get(key)` | Vrátí hodnotu pro daný klíč, pokud klíč existuje, jinak `None`.    | `d.get('a')  # Vrátí hodnotu pro klíč 'a'.`          |
| `dict.keys()`   | Vrátí seznam všech klíčů ve slovníku.                             | `d.keys()  # Vrátí všechny klíče ve slovníku.`       |
| `dict.values()` | Vrátí seznam všech hodnot ve slovníku.                            | `d.values()  # Vrátí všechny hodnoty ve slovníku.`   |
| `dict.items()`  | Vrátí seznam párů (klíč, hodnota).                                | `d.items()  # Vrátí všechny páry klíč-hodnota.`      |
| `dict.update()` | Aktualizuje slovník přidáním dvojic klíč-hodnota z jiného slovníku.| `d.update(d2)  # Přidá páry z jiného slovníku d2.`   |
| `dict.pop(key)` | Odstraní zadaný klíč a vrátí jeho hodnotu. Pokud klíč neexistuje, vyvolá chybu. | `d.pop('a')  # Odstraní a vrátí hodnotu pro 'a'.` |
| `dict.clear()`  | Vymaže všechny položky ze slovníku.                               | `d.clear()  # Vymaže celý slovník.`                  |
| `dict.copy()`   | Vrátí mělkou kopii slovníku.                                  | `d2 = d.copy()  # Vytvoří kopii slovníku.`           |
| `dict.setdefault(key, default)` | Vrátí hodnotu pro klíč, pokud existuje, jinak přidá klíč s výchozí hodnotou. | `d.setdefault('b', 0)  # Vrátí hodnotu nebo přidá 'b'.` |
| `dict.fromkeys(keys, value)` | Vytvoří nový slovník s klíči ze seznamu a stejnou hodnotou pro všechny klíče. | `dict.fromkeys(['a', 'b'], 0)  # Nový slovník s hodnotou 0 pro 'a' a 'b'.` |



##### Vytvoř kopii mého slovníku


```python
dalsi_uzivatel = uzivatel_3.copy()
```


```python
print(id(uzivatel_3))
print(id(dalsi_uzivatel))
```

    140659999395264
    140659999350272


<div style="color: red;">
⚠️ <strong>Upozornění:</strong> Metoda <em>copy()</em> vytváří jen tzv. mělkou kopii
</div>



```python
filmy = ["Šakalí léta", "Pelíšky", "Pupendo"]
reziser = {
    "jmeno": "Jan Hřebejk",
    "filmy": filmy
}
reziser2 = reziser.copy()
```


```python
print(reziser)
print(reziser2)
```

    {'jmeno': 'Jan Hřebejk', 'filmy': ['Šakalí léta', 'Pelíšky', 'Pupendo']}
    {'jmeno': 'Jan Hřebejk', 'filmy': ['Šakalí léta', 'Pelíšky', 'Pupendo']}



```python
reziser2["filmy"].append("Učitelka")
```


```python
print(reziser)
print(reziser2)
```

    {'jmeno': 'Jan Hřebejk', 'filmy': ['Šakalí léta', 'Pelíšky', 'Pupendo', 'Učitelka']}
    {'jmeno': 'Jan Hřebejk', 'filmy': ['Šakalí léta', 'Pelíšky', 'Pupendo', 'Učitelka']}


##### Odstraň klíč v mé kopii


```python
print(uzivatel_3)
print()
print(dalsi_uzivatel)
```

    {'jmeno': 'Lukáš', 'prijmeni': 'Holinka', 'vek': 28, 'hobby': ('fotbal', 'hry', 'pratele'), 'kontakt': {'telefon': '000 123 456 789', 'email': 'lukas@gmail.com', 'web': 'www.lukas.cz'}}
    
    {'jmeno': 'Lukáš', 'prijmeni': 'Holinka', 'vek': 28, 'hobby': ('fotbal', 'hry', 'pratele'), 'kontakt': {'telefon': '000 123 456 789', 'email': 'lukas@gmail.com', 'web': 'www.lukas.cz'}}



```python
vek = dalsi_uzivatel.pop("vek")  # .popitem()
```


```python
print(vek)
print(uzivatel_3)
print()
print(dalsi_uzivatel)
```

    28
    {'jmeno': 'Lukáš', 'prijmeni': 'Holinka', 'vek': 28, 'hobby': ('fotbal', 'hry', 'pratele'), 'kontakt': {'telefon': '000 123 456 789', 'email': 'lukas@gmail.com', 'web': 'www.lukas.cz'}}
    
    {'jmeno': 'Lukáš', 'prijmeni': 'Holinka', 'hobby': ('fotbal', 'hry', 'pratele')}



```python
dalsi_uzivatel.popitem()
```




    ('kontakt',
     {'telefon': '000 123 456 789',
      'email': 'lukas@gmail.com',
      'web': 'www.lukas.cz'})




```python
dalsi_uzivatel.pop("vek")
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-34-b4b73f4faa05> in <module>
    ----> 1 dalsi_uzivatel.pop("vek")
    

    KeyError: 'vek'


##### Zobraz mi klíče, hodnoty, nebo vše


```python
print(uzivatel_3.keys())
```

    dict_keys(['jmeno', 'prijmeni', 'vek', 'hobby', 'kontakt'])



```python
print(uzivatel_3.values())
```

    dict_values(['Lukáš', 'Holinka', 28, ('fotbal', 'hry', 'pratele'), {'telefon': '000 123 456 789', 'email': 'lukas@gmail.com', 'web': 'www.lukas.cz'}])



```python
print(uzivatel_3.items())
```

    dict_items([('jmeno', 'Lukáš'), ('prijmeni', 'Holinka'), ('vek', 28), ('hobby', ('fotbal', 'hry', 'pratele')), ('kontakt', {'telefon': '000 123 456 789', 'email': 'lukas@gmail.com', 'web': 'www.lukas.cz'})])


Opatrně, jde o *speciální datové typy*:


```python
print(type(uzivatel_3.keys()))
```

    <class 'dict_keys'>


... které **nelze standardně indexovat**:


```python
spec_objekt = uzivatel_3.keys()
```


```python
print(uzivatel_3.keys()[0])
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-40-a8a99ae62b85> in <module>
    ----> 1 print(uzivatel_3.keys()[0])
    

    TypeError: 'dict_keys' object is not subscriptable



```python
prevedeny_tupl = tuple(spec_objekt)
```


```python
print(prevedeny_tupl[0])
```

    jmeno


##### Vrať mi hodnotu pro neexistující klíč


```python
print(uzivatel_3)
```

    {'jmeno': 'Lukáš', 'prijmeni': 'Holinka', 'vek': 28, 'hobby': ('fotbal', 'hry', 'pratele'), 'kontakt': {'telefon': '000 123 456 789', 'email': 'lukas@gmail.com', 'web': 'www.lukas.cz'}}



```python
print(uzivatel_3["jmeno"])
```

    Lukáš



```python
print(uzivatel_3["pohlavi"])
```


    ---------------------------------------------------------------------------

    KeyError                                  Traceback (most recent call last)

    <ipython-input-46-ec0d1cdb4b7e> in <module>
    ----> 1 print(uzivatel_3["pohlavi"])
    

    KeyError: 'pohlavi'


Velmi často se dostaneš do situace, kde nemůžeš jistě vědět, jestli **je hledaný klíč ve slovníku**.

Pokud není, skončí tvůj skript vyjímkou `KeyError`.


```python
print(uzivatel_3.get("jmeno"))
```

    Lukáš



```python
print(uzivatel_3.get("pohlavi"))
```

    None



```python
print(uzivatel_3.get("pohlavi", "Klíč 'pohlavi' neexistuje"))
```

    Klíč 'pohlavi' neexistuje


##### Odstraň všechno ze slovníku


```python
dalsi_uzivatel.clear()
print(uzivatel_3)
print(dalsi_uzivatel)
```

    {'jmeno': 'Lukáš', 'prijmeni': 'Holinka', 'vek': 28, 'hobby': ('fotbal', 'hry', 'pratele'), 'kontakt': {'telefon': '000 123 456 789', 'email': 'lukas@gmail.com', 'web': 'www.lukas.cz'}}
    {}



```python
# dir(dict)
```


```python
# help(dict.pop)
```

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si metody pro `dict`:

Máš následující česko-anglický slovník:

```python
slovnik = {
    "kočka": "cat",
    "pes": "dog",
    "strom": "tree",
    "auto": "car",
    "dům": "house"
}
```

#### Zadání:

1. Zjisti, kolik slov slovník obsahuje.
   
2. Vypiš všechna česká slova obsažená ve slovníku.

3. Vypiš všechny anglické překlady ve slovníku.

4. Přidej do slovníku slovo a jeho překlad zadaný uživatelem.

5. Ověř, zda slovník obsahuje slovo zadané uživatelem a vypiš jeho anglický překlad, pokud existuje. Pokud neexistuje, tak vypiš: `"Slovo <české slovo> není ve slovníku."`

6. Odstraň slovo zadané uživatelem a zobraz aktuální obsah slovníku.


<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
# Česko-anglický slovník
slovnik = {
    "kočka": "cat",
    "pes": "dog",
    "strom": "tree",
    "auto": "car",
    "dům": "house"
}

# 1. Zjištění počtu slov ve slovníku
pocet_slov = len(slovnik)
print("Počet slov ve slovníku je:", pocet_slov)

# 2. Výpis všech českých slov
ceska_slova = slovnik.keys()
print("Česká slova:", list(ceska_slova))

# 3. Výpis všech anglických překladů
anglicke_preklady = slovnik.values()
print("Anglické překlady:", list(anglicke_preklady))

# 4. Přidání slova a překladu zadaného uživatelem
nove_ceske_slovo = input("Zadej nové české slovo: ")
novy_anglicky_preklad = input(f"Zadej anglický překlad pro '{nove_ceske_slovo}': ")
slovnik[nove_ceske_slovo] = novy_anglicky_preklad
print("Aktualizovaný slovník po přidání:", slovnik)

# 5. Ověření, zda slovník obsahuje slovo zadané uživatelem a výpis překladu
ceske_slovo = input("Zadej české slovo pro ověření: ")
preklad = slovnik.get(ceske_slovo)
if preklad:
    print(f"Anglický překlad pro '{ceske_slovo}' je: {preklad}")
else:
    print(f"Slovo '{ceske_slovo}' není ve slovníku.")

# 6. Odstranění slova zadaného uživatelem a výpis aktualizovaného slovníku
slovo_k_odstraneni = input("Zadej české slovo pro odstranění: ")
if slovo_k_odstraneni in slovnik:
    slovnik.pop(slovo_k_odstraneni)
    print(f"Slovo '{slovo_k_odstraneni}' bylo odstraněno.")
else:
    print(f"Slovo '{slovo_k_odstraneni}' není ve slovníku.")
    
print("Aktualizovaný slovník:", slovnik)

```
</details>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.RAQa2_CvZxiwnXMYFD_V5AHaHa%26pid%3DApi&f=1&ipt=62c71c5e1001bb4e1b0c8bc5e9ed3414910bf4031aa7fceee8397879872e1782&ipo=images" width="200" />

## Datový typ `set`

---

*Set* nebo také *množina*:
* v Pythonu **standartní datový typ**,
* tvořený **unikatními hodnotami**,
* nepracuje s jednotlivými údaji ale s daty jako celkem,
* hodnoty mohou být jak `str`, tak číselné hodnoty,
* **nemá pořadí** (podobné slovníkům),
* **změnitelný** datový typ.


```python
zensky_rod = {"žena", "růže", "píseň", "kost"}
```


```python
print(type(zensky_rod))
```

    <class 'set'>


* klíčové operace setů:
  - sjednocení `|`, 
  
  <img src="https://math24.net/images/set-operations1.svg" style="width: 400px; background-color: white">
  
  - průnik `&`, 
  
  <img src="https://math24.net/images/set-operations2.svg" style="width: 400px; background-color: white">
  
  - rozdíl `-`,

  <img src="https://math24.net/images/set-operations3.svg" style="width: 400px; background-color: white">

  - symetrický rozdíl `^`.

  <img src="https://math24.net/images/set-operations4.svg" style="width: 400px; background-color: white">

Některé *operátory* jsou stejné symboly jako *bitwise* operátory.

### Metody množin (`set`)

| Metoda                                  | Vysvětlení                                                                 | Příklad                                                 | Operátor                    |
|-----------------------------------------|-----------------------------------------------------------------------------|---------------------------------------------------------|-----------------------------|
| `set.add(element)`                      | Přidá prvek do množiny. Pokud již existuje, nic se nestane.                 | `s.add(1)  # Přidá 1 do množiny.`                       | N/A                         |
| `set.remove(element)`                   | Odstraní prvek z množiny. Pokud prvek neexistuje, vyvolá chybu `KeyError`.  | `s.remove(1)  # Odstraní 1 z množiny.`                  | N/A                         |
| `set.discard(element)`                  | Odstraní prvek z množiny, pokud existuje. Pokud neexistuje, nic se nestane. | `s.discard(1)  # Bezpečně odstraní 1, pokud existuje.`  | N/A                         |
| `set.pop()`                             | Odstraní a vrátí libovolný prvek z množiny. Pokud je množina prázdná, vyvolá chybu. | `s.pop()  # Odstraní a vrátí náhodný prvek.`  | N/A                         |
| `set.clear()`                           | Vymaže všechny prvky z množiny.                                            | `s.clear()  # Vymaže celou množinu.`                    | N/A                         |
| `set.copy()`                            | Vytvoří povrchovou kopii množiny.                                          | `s2 = s.copy()  # Vytvoří kopii množiny.`               | N/A                         |
| `set.union(other_set)`                  | Vrátí sjednocení dvou množin (všechny prvky z obou množin).                | `s.union(s2)  # Vrátí sjednocení s a s2.`               | `s | s2`                    |
| `set.intersection(other_set)`           | Vrátí průnik dvou množin (společné prvky).                                 | `s.intersection(s2)  # Vrátí průnik s a s2.`            | `s & s2`                    |
| `set.difference(other_set)`             | Vrátí rozdíl mezi dvěma množinami (prvky, které jsou jen v jedné množině).  | `s.difference(s2)  # Vrátí prvky, které jsou jen v s.`  | `s - s2`                    |
| `set.symmetric_difference(other_set)`   | Vrátí symetrický rozdíl dvou množin (prvky, které nejsou v obou množinách). | `s.symmetric_difference(s2)  # Vrátí nesdílené prvky.`  | `s ^ s2`                    |
| `set.issubset(other_set)`               | Vrátí `True`, pokud je tato množina podmnožinou jiné množiny.              | `s.issubset(s2)  # Zjistí, jestli je s podmnožinou s2.` | `s <= s2`                   |
| `set.issuperset(other_set)`             | Vrátí `True`, pokud je tato množina nadmnožinou jiné množiny.              | `s.issuperset(s2)  # Zjistí, jestli je s nadmnožinou s2.`| `s >= s2`                  |
| `set.isdisjoint(other_set)`             | Vrátí `True`, pokud nemají množiny žádný společný prvek.                   | `s.isdisjoint(s2)  # Zjistí, jestli nemají s a s2 žádné společné prvky.` | N/A |


### Nový set


```python
muj_novy_set = set()
muj_druhy_set = {}
```


```python
print(type(muj_novy_set))
print(type(muj_druhy_set))
```

    <class 'set'>
    <class 'dict'>



```python
suda_cisla = {2, 4, 6, 8, 0}
pismena = {"a", "b", "c", "d"}
```


```python
print(type(suda_cisla))
print(type(pismena))
```

    <class 'set'>
    <class 'set'>



```python
pismena = set("abcdef")
print(pismena)
```

    {'b', 'e', 'f', 'd', 'a', 'c'}



```python
pismena = set(("a", "b", "c"))
print(pismena)
```

    {'b', 'c', 'a'}



```python
dalsi_pismena = set(["g", "h", "i", "j", "k", "l", "m"])
print(dalsi_pismena)
```

    {'l', 'j', 'h', 'k', 'm', 'g', 'i'}


### Setové operace


```python
muj_set_A = {"žena", "růže", "píseň", "kost", "Lucie", "Matouš"}
muj_set_B = {"žena", "růže", "píseň", "kost", "Lukáš"}
```

<img src="https://i.imgur.com/yhV0pvW.png" width="800">

##### Sjednocení ~ union


```python
print(muj_set_B.union(muj_set_A))
print(muj_set_A | muj_set_B)
```

    {'růže', 'píseň', 'žena', 'Lucie', 'Lukáš', 'Matouš', 'kost'}
    {'Lucie', 'růže', 'žena', 'píseň', 'Lukáš', 'Matouš', 'kost'}


<img src="https://i.imgur.com/Qgvr0Jz.png" width="800">

##### Průnik ~ intersection


```python
print(muj_set_B.intersection(muj_set_A))
print(muj_set_A & muj_set_B)
```

    {'žena', 'kost', 'růže', 'píseň'}
    {'žena', 'kost', 'růže', 'píseň'}


<img src="https://i.imgur.com/MYKRUqb.png" width="800">

##### Rozdíl ~ difference


```python
print(muj_set_A.difference(muj_set_B))
print(muj_set_A - muj_set_B)
```

    {'Matouš', 'Lucie'}
    {'Matouš', 'Lucie'}


<img src="https://i.imgur.com/frukWiG.png" width="800">


```python
print(muj_set_B.difference(muj_set_A))
print(muj_set_B - muj_set_A)
```

    {'Lukáš'}
    {'Lukáš'}


<img src="https://i.imgur.com/D3uPteB.png" width="800">

##### Symetrický rozdíl ~ symmetric difference


```python
print(muj_set_B.symmetric_difference(muj_set_A))
print(muj_set_A ^ muj_set_B)
```

    {'Matouš', 'Lucie', 'Lukáš'}
    {'Matouš', 'Lucie', 'Lukáš'}



```python
print(muj_set_B)
muj_set_B.symmetric_difference_update(muj_set_A)
print(muj_set_B)
```

    {'růže', 'píseň', 'žena', 'Lukáš', 'kost'}
    {'Lucie', 'Lukáš', 'Matouš'}


<img src="https://i.imgur.com/7XxiV1y.png" width="800">

### Manipulace s hodnotami, metody setů

Veškeré další úpravy setů probíhají pomocí **metod setů**.

Vytvořím si kopii ze orig. setu `muj_set_1`:


```python
muj_set_1 = {"žena", "růže", "píseň", "kost"}
muj_set_2 = muj_set_1.copy()
```


```python
print(id(muj_set_1))
print(id(muj_set_2))
```

    140659979226464
    140659979225344



```python
muj_set_2.add("Matouš")
muj_set_2.add("Lukáš")
```


```python
print(muj_set_2)
```

    {'růže', 'píseň', 'žena', 'Lukáš', 'Matouš', 'kost'}



```python
muj_set_2.add("Matouš")
```


```python
print(muj_set_2)
```

    {'růže', 'píseň', 'žena', 'Lukáš', 'Matouš', 'kost'}



```python
muj_set_2.discard("Lukáš")  # remove
```


```python
# help(set.pop)
```


```python
print(muj_set_2)
```

    {'růže', 'píseň', 'žena', 'Matouš', 'kost'}



```python
muj_set_2.pop() # odstraní náhodný prvek množiny
```


```python
# dir(set)
```

##### Obsahují sety pouze odlišné hodnoty


```python
print(muj_set_1)
print(muj_set_2)
```

    {'žena', 'kost', 'růže', 'píseň'}
    {'růže', 'píseň', 'žena', 'Matouš', 'kost'}



```python
muj_set_2.add("Matouš")
muj_set_2.discard("žena")
```


```python
print(muj_set_1)
print(muj_set_2)
```

    {'žena', 'kost', 'růže', 'píseň'}
    {'růže', 'píseň', 'Matouš', 'kost'}



```python
print(muj_set_2.isdisjoint(muj_set_1))
```

    False



```python
muj_set_3 = {"Lukáš"}
```


```python
print(muj_set_3.isdisjoint(muj_set_1))
```

    True



```python
l1 = ["a", "b", "c", "d"]
l2 = ["a", "b", "c", "e"]
```


```python
print(set(l1).symmetric_difference(set(l2)))
print(set(l1) ^ set(l2))
```

    {'d', 'e'}
    {'d', 'e'}


---
### 🧠 CVIČENÍ 🧠, Vyzkoušej si metody pro `set`:

Máš následující množiny obsahující různá zvířata:

```python
mnozina_1 = {"kočka", "pes", "králík", "had"}
mnozina_2 = {"pes", "papoušek", "had", "ryba"}
```

#### Zadání:

1. Zjisti, kolik různých zvířat obsahuje každá množina.

2. Vypiš všechna zvířata, která jsou v první množině, ale nejsou ve druhé.

3. Vypiš všechna zvířata, která jsou ve druhé množině, ale nejsou v první.

4. Vytvoř množinu, která obsahuje všechna zvířata, která jsou v obou množinách (průnik množin).

5. Vytvoř množinu, která obsahuje všechna zvířata z obou množin (sjednocení množin).

6. Přidej nové zvíře zadané uživatelem do první množiny.

7. Odstraň zvíře zadané uživatelem z druhé množiny a zobraz aktuální obsah obou množin.


<details>
  <summary>▶️  Klikni zde pro zobrazení řešení</summary>
   
```python
# Předem dané množiny
mnozina_1 = {"kočka", "pes", "králík", "had"}
mnozina_2 = {"pes", "papoušek", "had", "ryba"}

# 1. Zjištění, kolik různých zvířat obsahuje každá množina
pocet_mnozina_1 = len(mnozina_1)
pocet_mnozina_2 = len(mnozina_2)
print(f"Množina 1 obsahuje {pocet_mnozina_1} zvířat.")
print(f"Množina 2 obsahuje {pocet_mnozina_2} zvířat.")

# 2. Výpis zvířat, která jsou v první množině, ale nejsou ve druhé (rozdíl množin)
rozdil_1_2 = mnozina_1 - mnozina_2
print("Zvířata v první množině, ale ne ve druhé:", rozdil_1_2)

# 3. Výpis zvířat, která jsou ve druhé množině, ale nejsou v první
rozdil_2_1 = mnozina_2 - mnozina_1
print("Zvířata ve druhé množině, ale ne v první:", rozdil_2_1)

# 4. Průnik množin (zvířata, která jsou v obou množinách)
prunik = mnozina_1 & mnozina_2
print("Zvířata, která jsou v obou množinách:", prunik)

# 5. Sjednocení množin (všechna zvířata z obou množin)
sjednoceni = mnozina_1 | mnozina_2
print("Všechna zvířata z obou množin:", sjednoceni)

# 6. Přidání nového zvířete zadaného uživatelem do první množiny
nove_zvire = input("Zadej nové zvíře, které chceš přidat do první množiny: ")
mnozina_1.add(nove_zvire)
print("Aktualizovaná množina 1:", mnozina_1)

# 7. Odstranění zvířete zadaného uživatelem z druhé množiny
zvire_k_odstraneni = input("Zadej zvíře, které chceš odstranit z druhé množiny: ")
if zvire_k_odstraneni in mnozina_2:
    mnozina_2.remove(zvire_k_odstraneni)
    print(f"Zvíře '{zvire_k_odstraneni}' bylo odstraněno z druhé množiny.")
else:
    print(f"Zvíře '{zvire_k_odstraneni}' není ve druhé množině.")
    
print("Aktualizovaná množina 2:", mnozina_2)


```
</details>

---

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.ehRENB9fEmyfgOIMXpoaIwHaHa%26pid%3DApi&f=1&ipt=d0da0abed7f3fd494df3e5699a6c58658b8cebff1ffc07b87d0f5be9f549f9c7&ipo=images" width="200" />

## Datový typ `frozenset`

---

*Frozenset* a *set* jsou obdobná dvojice jako `list` a `tuple`:
* v Pythonu je standardní datový typ,
* tvořený unikatními hodnotami,
* nepracuje s jednotlivými údaji ale s daty jako celkem,
* hodnoty mohou být jak `str`, tak číselné hodnoty,
* nemá pořadí (podobné slovníkům),
* jakmile jej vytvoříš, nemůžeš jej změnit.


```python
nezm_fset = frozenset(('růže', 'žena', 'Jan', 'píseň', 'kost'))
```


```python
print(type(nezm_fset))
```

    <class 'frozenset'>


Stejně jako datový typ `tuple` bývá i `frozenset` opomíjený, ačkoliv nabízí tyto výhody:
* *Frozensety* potřebují méně paměti,
* hodnoty **není možné změnit** ani omylem,
* indikátor **pro ostatní programátory**.

### Práce s frozensety


```python
druhy_nezm_fset = frozenset("abcde")
```


```python
# dir(druhy_nezm_fset)
```


```python
print(type(druhy_nezm_fset))
print(druhy_nezm_fset)
```

    <class 'frozenset'>
    frozenset({'b', 'e', 'd', 'a', 'c'})



```python
druhy_nezm_fset.add("f")
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-103-cd54d8534cc0> in <module>
    ----> 1 druhy_nezm_fset.add("f")
    

    AttributeError: 'frozenset' object has no attribute 'add'



```python
druhy_nezm_fset.discard("a")
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    <ipython-input-104-f89fb40f47b6> in <module>
    ----> 1 druhy_nezm_fset.discard("a")
    

    AttributeError: 'frozenset' object has no attribute 'discard'



```python
treti_nezm_fset = druhy_nezm_fset.copy()
```


```python
print(type(druhy_nezm_fset))
print(type(treti_nezm_fset))
```

    <class 'frozenset'>
    <class 'frozenset'>



```python
print(id(druhy_nezm_fset))
print(id(treti_nezm_fset))
```

    140659979223552
    140659979223552



```python
print(druhy_nezm_fset.intersection(treti_nezm_fset))
```

    frozenset({'b', 'd', 'e', 'a', 'c'})



```python
del druhy_nezm_fset
```


```python
print(dir())
```

    ['In', 'Out', '_', '_100', '_32', '_51', '_80', '_92', '_93', '_94', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_i', '_i1', '_i10', '_i100', '_i101', '_i102', '_i103', '_i104', '_i105', '_i106', '_i107', '_i108', '_i109', '_i11', '_i110', '_i12', '_i13', '_i14', '_i15', '_i16', '_i17', '_i18', '_i19', '_i2', '_i20', '_i21', '_i22', '_i23', '_i24', '_i25', '_i26', '_i27', '_i28', '_i29', '_i3', '_i30', '_i31', '_i32', '_i33', '_i34', '_i35', '_i36', '_i37', '_i38', '_i39', '_i4', '_i40', '_i41', '_i42', '_i43', '_i44', '_i45', '_i46', '_i47', '_i48', '_i49', '_i5', '_i50', '_i51', '_i52', '_i53', '_i54', '_i55', '_i56', '_i57', '_i58', '_i59', '_i6', '_i60', '_i61', '_i62', '_i63', '_i64', '_i65', '_i66', '_i67', '_i68', '_i69', '_i7', '_i70', '_i71', '_i72', '_i73', '_i74', '_i75', '_i76', '_i77', '_i78', '_i79', '_i8', '_i80', '_i81', '_i82', '_i83', '_i84', '_i85', '_i86', '_i87', '_i88', '_i89', '_i9', '_i90', '_i91', '_i92', '_i93', '_i94', '_i95', '_i96', '_i97', '_i98', '_i99', '_ih', '_ii', '_iii', '_oh', 'dalsi_pismena', 'dalsi_uzivatel', 'exit', 'get_ipython', 'l1', 'l2', 'muj_druhy_set', 'muj_novy_set', 'muj_set_1', 'muj_set_2', 'muj_set_3', 'muj_set_A', 'muj_set_B', 'nezm_fset', 'novy_uzivatel_1', 'novy_uzivatel_2', 'pismena', 'prevedeny_tupl', 'quit', 'spec_objekt', 'suda_cisla', 'treti_nezm_fset', 'uzivatel', 'uzivatel_3', 'vek', 'zensky_rod']



```python
del treti_nezm_fset
```


```python
print(dir())
```

    ['In', 'Out', '_', '_100', '_32', '_51', '_80', '_92', '_93', '_94', '__', '___', '__builtin__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', '_dh', '_i', '_i1', '_i10', '_i100', '_i101', '_i102', '_i103', '_i104', '_i105', '_i106', '_i107', '_i108', '_i109', '_i11', '_i110', '_i111', '_i112', '_i12', '_i13', '_i14', '_i15', '_i16', '_i17', '_i18', '_i19', '_i2', '_i20', '_i21', '_i22', '_i23', '_i24', '_i25', '_i26', '_i27', '_i28', '_i29', '_i3', '_i30', '_i31', '_i32', '_i33', '_i34', '_i35', '_i36', '_i37', '_i38', '_i39', '_i4', '_i40', '_i41', '_i42', '_i43', '_i44', '_i45', '_i46', '_i47', '_i48', '_i49', '_i5', '_i50', '_i51', '_i52', '_i53', '_i54', '_i55', '_i56', '_i57', '_i58', '_i59', '_i6', '_i60', '_i61', '_i62', '_i63', '_i64', '_i65', '_i66', '_i67', '_i68', '_i69', '_i7', '_i70', '_i71', '_i72', '_i73', '_i74', '_i75', '_i76', '_i77', '_i78', '_i79', '_i8', '_i80', '_i81', '_i82', '_i83', '_i84', '_i85', '_i86', '_i87', '_i88', '_i89', '_i9', '_i90', '_i91', '_i92', '_i93', '_i94', '_i95', '_i96', '_i97', '_i98', '_i99', '_ih', '_ii', '_iii', '_oh', 'dalsi_pismena', 'dalsi_uzivatel', 'exit', 'get_ipython', 'l1', 'l2', 'muj_druhy_set', 'muj_novy_set', 'muj_set_1', 'muj_set_2', 'muj_set_3', 'muj_set_A', 'muj_set_B', 'nezm_fset', 'novy_uzivatel_1', 'novy_uzivatel_2', 'pismena', 'prevedeny_tupl', 'quit', 'spec_objekt', 'suda_cisla', 'uzivatel', 'uzivatel_3', 'vek', 'zensky_rod']



```python
print(treti_nezm_fset)
```


    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-113-4cb2e112917c> in <module>
    ----> 1 print(treti_nezm_fset)
    

    NameError: name 'treti_nezm_fset' is not defined


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOIP.DHBtCEfIYi3Xx7vPmh0wfwHaHa%26pid%3DApi&f=1&ipt=d366265927f55719e1b4dfb1e8134ce97a94bcfd98c450a472e94a5f9fb08818&ipo=images" width="250" />

## Volitelné argumenty

---

*Zabudované funkce* jsou velkými pomocníky, protože ti umožní zjednodušit různé procesy.

Navíc můžeš jejich použití **doplnit volitelnými argumenty**.

*Volitelný argument* je hodnota, kterou můžeš (ale nemusíš) zadávat.

Funkce **umí pracovat bez něj**, případně má dopředu nachystanou nějakou počáteční hodnotu.

Tyto *doplňující argumenty* ti mohou ještě víc pomoci v zjednodušení tvého zápisu:


```python
print("Matous", "Marek", "Lukas")
```

    Matous Marek Lukas


Pokud ji napíšeš **bez argumentů**, s několika různými hodnotami za sebou, tvůj výstup se **seřadí za sebe**.


```python
# print(help(print))  # zobrazit nápovědu pro funkci 'print'
```


```python
print("Matous", "Marek", "Lukas", sep="\n")  # volitelný (také nepovinný) argument 'sep'
```

    Matous
    Marek
    Lukas



```python
# help(dict.get)
```

**Volitené argumenty** můžeš používat téměř u všech *zabudovaných funkcí*. Je jich opravdu spousta.

Proto pokud budeš potřebovat pracovat s *zabudovanými funkcemi* vždy zkontroluj, jestli neobsahují nějaký nepovinný *volitelný argument*, který ti pomůže.

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.GMJvJ-GG0YS8H5JmHR3CbwHaHm%26pid%3DApi&f=1" width="200">

## Domácí úkol

---

Pracuj krok za krokem na novém filmovém slovníku.

### Zadané hodnoty


```python
sluzby = ("dostupné filmy", "detaily filmu", "seznam režisérů")
oddelovac = "=" * 62
```


```python
film_1 = {
    "jmeno": "Shawshank Redemption",
    "rating": "93/100",
    "rok": 1994,
    "reziser": "Frank Darabont",
    "stopaz": 144
}
```


```python
film_2 = {
    "jmeno": "The Godfather",
    "rating": "92/100",
    "rok": 1972,
    "reziser": "Francis Ford Coppola",
    "stopaz": 175
}
```


```python
film_3 = {
    "jmeno": "The Dark Knight",
    "rating": "90/100",
    "rok": 2008,
    "reziser": "Christopher Nolan",
    "stopaz": 152
}
```

### Sjednoť slovníky do jednoho objektu


```python
# sjednoť předchozí 3 slovníky do jednoho slovníku 'filmy'
# .. klíčem bude jméno filmu a samotný slovník následuje
# .. jako hodnota.
```

### Výpis pro uživatele

```
               VÍTEJ V NAŠEM FILMOVÉM SLOVNÍKU!               
==============================================================
        dostupné filmy | detaily filmu | doporuč film         
==============================================================
```

### Zobraz mi dostupné filmy

```
                       Dostupné filmy:                        
==============================================================
Shawshank Redemption, The Godfather, The Dark Knight
==============================================================
```


```python
# vyber z dostupné služby v nabídce a zobraz jména filmů
```

### Zobraz detaily o filmu

```
Detaily filmu: 
==============================================================
{'jmeno': 'The Dark Knight', 'rating': '90/100', 'rok': 2008, 'reziser': 'Christopher Nolan', 'stopaz': 152}
==============================================================
```

### Zobraz seznam režisérů

```
Všichni režiséři:
==============================================================
{'Frank Darabont', 'Christopher Nolan', 'Francis Ford Coppola'}
==============================================================
```

---
