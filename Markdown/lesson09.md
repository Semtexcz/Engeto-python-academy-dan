# Python akademie

---

<br>

## Obsah lekce
---


1. [Úvod do IO](#Úvod-do-IO),
2. [Spojení se souborem pomocí Pythonu](#Spojení-se-souborem-pomocí-Pythonu),
3. [Textové soubory](#Textové-soubory),
4. [Zápis s kontextovým manažerem](#Zápis-s-kontextovým-manažerem),
5. [Formátování řetězců (~string formatting)](#Formátování-řetězců-(~string-formatting)).


---

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOIP.BPYuvKj05Xo_oF_oXiL1yAHaHa%26pid%3DApi&f=1" width="250" style="margin-left:auto; margin-right:auto">

## Úvod do I/O (Input/Output)

---

Nyní pracuješ pouze s objekty **Pythonu vlastními** nebo **s jeho knihovnami**.

Všechny tyto *objekty* si vytvoříš a zpracováváš **v rámci paměti RAM** (*random access memory*).

<br>

*Paměť RAM* je **velmi rychlá**, ale současně náročná a vyžaduje **neustálý zdroj** (není elektřina, ztratíš data).

Takový **disk počítače** je o dost **pomalejší** než paměť *RAM*, ale umožňuje ti uchovávat tebou získaná, zpracovaná data.

<table>
  <thead>
    <tr>
      <th>Technologie</th>
      <th>Rychlost čtení/zápisu (přibližně)</th>
      <th>Latence</th>
      <th>Použití</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>RAM</td>
      <td>25–50+ GB/s</td>
      <td>Nanosekundy</td>
      <td>Dočasná data pro CPU</td>
    </tr>
    <tr>
      <td>SSD</td>
      <td>500 MB/s – 7 GB/s</td>
      <td>Mikrosekundy</td>
      <td>Úložiště OS a aplikací</td>
    </tr>
    <tr>
      <td>HD</td>
      <td>100–200 MB/s</td>
      <td>Milisekundy</td>
      <td>Archivace a zálohy dat</td>
    </tr>
  </tbody>
</table>



<br>

Proto je dobré osvojit si pravidla a postupy v Pythonu, jak vytvořit **persistentní data**.

<br>

### Co je soubor?

**Počítačový soubor**

- Základní jednotka ukládání dat v počítačích
- Obsahuje informace různých typů (text, obrázek, video, binární data)
- Struktura souboru usnadňuje interpretaci dat aplikacemi a operačním systémem

---

<img src="https://realpython.com/cdn-cgi/image/width=337,format=auto/https://files.realpython.com/media/FileFormat.02335d06829d.png">

**Struktura počítačového souboru**

1. **Header (záhlaví)**
   - První část souboru s metadaty
   - Obsahuje informace o typu souboru, formátu, délce souboru
   - Pomáhá aplikacím rozpoznat, jak soubor zpracovat

2. **Data (tělo)**
   - Hlavní obsah souboru
   - Například text, pixely obrázku nebo zvukové frekvence
   - Reprezentováno různými způsoby podle účelu souboru

3. **EOF (End of File)**
   - Značka nebo příznak konce souboru
   - Označuje, kde data končí
   - Někdy určeno explicitně, jindy pouze délkou souboru

---


**Reprezentace souboru**

- Sekvence bajtů v paměti nebo na disku
- Každý bajt = binární data (0 nebo 1)
- Na vyšší úrovni operační systém ukládá:
  - Název souboru
  - Umístění
  - Oprávnění
  - Datum vytvoření a další vlastnosti


### Adresa souboru

Každý soubor má v operačním systému svou adresu, podle které ho lze najít. Tato adresa je jedinečná a jednoznačně identifikuje umístění souboru ve stromové struktuře souborového systému.

Skládá se ze tří částí:

<ul>
    <li style="color:#28abed;font-weight:700">Adresa složky</li>
    <p>Označuje cestu k umístění souboru. V Linuxu cesta začíná od kořenového adresáře <code>/</code>, kdežto ve Windows od písmena jednotky (např. <code>C:\</code>). Cesta obsahuje názvy všech složek, které vedou k danému souboru.</p>

   <li style="color:#e00846;font-weight:700">Jméno souboru</li>
   <p>Jméno souboru je jedinečný název v rámci konkrétní složky. Soubor se tak odlišuje od ostatních souborů ve stejném adresáři. Jméno by mělo být výstižné a stručné, aby se dalo snadno rozpoznat.</p>

   <li style="color:#44ed8d;font-weight:700">Přípona souboru</li>
   <p>Přípona určuje typ souboru, například <code>.txt</code> pro textové dokumenty nebo <code>.jpg</code> pro obrázky. Operační systémy, zejména Windows, využívají příponu pro rozpoznání aplikace, kterou by měly použít k otevření souboru. V Linuxu není přípona striktně nutná pro identifikaci typu souboru, ale je užitečná pro uživatele.</p>
</ul>

### Stromová struktura

Souborový systém v Linuxu i Windows používá stromovou strukturu, kde každý soubor a složka mají své místo ve větvené hierarchii:

- **Kořenový adresář** je výchozím bodem stromu. V Linuxu je kořen označen <code>/</code>, zatímco ve Windows se používá písmeno jednotky s následným zpětným lomítkem (např `C:\`).
- **Adresáře a podadresáře** tvoří větve stromu, kde každý adresář může obsahovat další soubory a složky.
- **Soubory** jsou na koncích větví (listy stromu), kde každý soubor je přístupný přes konkrétní cestu, která sleduje hierarchii složek od kořene až po cílový soubor.


```python
!tree ..
```

**Porovnání souborových systémů Windows a Linux**

1. **Cesta k souboru**:
   - **Linux**: Používá dopředná lomítka `/` pro oddělení složek (např. <code><span style="color:#28abed">/home/user/documents/</span><span style="color:#e00846">file</span><span style="color:#44ed8d">.txt</span></code>).
   - **Windows**: Používá zpětná lomítka `\` a začíná písmenem jednotky (např. <code><span style="color:#28abed"> C:\Users\User\Documents&#92;</span><span style="color:#e00846">file</span><span style="color:#44ed8d">.txt</span><</code>).

2. **Jednotky a připojení disku**:
   - **Linux**: Jednotky a další zařízení (např. USB) jsou připojovány k určitému adresáři (např. `/media/usb`), což umožňuje jednotnou strukturu bez potřeby odlišných písmen.
   - **Windows**: Každý disk nebo oddíl je identifikován písmenem jednotky (např. `C:`, `D:`), což může působit méně sjednoceně.

3. **Oprávnění**:
   - **Linux**: Systém oprávnění je složitější a zahrnuje práva pro čtení, zápis a spouštění pro vlastníka, skupinu a ostatní uživatele.
   - **Windows**: Oprávnění jsou spravována pomocí systému ACL (Access Control List), což umožňuje detailnější nastavení, ale pro běžné uživatele je často obtížněji přístupné.

4. **Přípony souborů**:
   - **Linux**: Rozpoznává typ souboru podle obsahu, takže přípony nejsou nezbytné (např. binární soubory nemusí mít .exe). Přípony jsou však užitečné pro přehlednost.
   - **Windows**: Přípony jsou klíčové pro identifikaci a otevření souboru správnou aplikací, což je důležité zejména pro spustitelné soubory (.exe).

### Ukončení řádku

- **Historie**:
  - Původ ve zvyklostech z Morseovy abecedy, kde se používalo specifické značení konce řádku nebo přenosu.
  - Standardizováno pro telegrafy organizacemi ISO a ASA.

- **Standardizace znaků**:
  - **ASA standard**: Používá sekvenci Carriage Return (CR nebo `\r`) a Line Feed (LF nebo `\n`) pro konec řádku (CR+LF nebo `\r\n`).
  - **ISO standard**: Povolen buď CR+LF nebo pouze LF.

- **Operační systémy**:
  - **Windows**: Používá CR+LF (`\r\n`) pro nový řádek.
  - **Unix a novější verze MacOS**: Používají pouze LF (`\n`).

- **Problémy při zpracování souborů**:
  - Soubor vytvořený v jednom OS může mít jinou interpretaci na jiném OS.
  - Příklad: Soubor `windows.txt` vytvořený na Windows bude obsahovat řádky zakončené `\r\n`.
  - Na Unixových systémech bude stejný soubor interpretován takto:
    - Každá položka se rozdělí na `\r` a `\n`, což způsobí nečekané řádkování.
    ```
    Český jazyk je krásný a bohatý.\r\n
    Každé slovo má svůj význam.\r\n
    Jazyk nás spojuje i odlišuje.\r\n
    Příroda je plná inspirace.\r\n
    Díky ní objevujeme nové světy.\r\n
    ```

- **Důsledky**:
  - Při iteraci přes jednotlivé řádky může dojít k problémům.
  - Při práci s různými OS je potřeba ošetřit rozdíly v zakončení řádků.


### Kódování znaků

**ASCII kódování**

ASCII používá 7 bitů na znak, takže každý znak má přiřazený kód v rozsahu 0–127.

| Znak | ASCII Kód | Binární kódování (7 bitů) |
|------|-----------|--------------------------|
| `A`  | 65        | 01000001                 |
| `a`  | 97        | 01100001                 |
| `1`  | 49        | 00110001                 |
| `?`  | 63        | 00111111                 |

Příklad:
- Znak `A` má kód 65, což je v binárním zápisu `01000001`.
- Znak `a` má kód 97, což je v binárním zápisu `01100001`.

ASCII je omezený pouze na znaky základní latinské abecedy a několik speciálních znaků, takže třeba znak `č` v ASCII nelze reprezentovat.

**UTF-8 kódování**

UTF-8 je proměnlivě dlouhé kódování a umožňuje použít 1 až 4 byty na znak. Znaky odpovídající ASCII jsou zakódovány pomocí 1 bytu, zatímco znaky mimo ASCII používají více bytů.

| Znak | Unicode Kód (desítkově) | Unicode Kód (hexadecimálně) | Binární kódování (UTF-8)       |
|------|--------------------------|-----------------------------|--------------------------------|
| `A`  | 65                       | 0041                        | 01000001                       |
| `a`  | 97                       | 0061                        | 01100001                       |
| `č`  | 269                      | 010D                        | 11000101 10101101              |
| `😊` | 128522                   | 1F60A                       | 11110000 10011111 10011000 10101010 |

Příklad:
- Znak `A` má kód 65, což je v UTF-8 `01000001` (shodné s ASCII, protože UTF-8 je zpětně kompatibilní).
- Znak `č` má kód 269, což je v hexadecimálním zápisu `010D`. V UTF-8 se zakóduje jako dva byty: `11000101 10101101`.
- Emotikon `😊` má kód 128522, což je v hexadecimálním zápisu `1F60A`. V UTF-8 potřebuje 4 byty: `11110000 10011111 10011000 10101010`.

**Jak to funguje?**

UTF-8 používá specifický formát, který indikuje počet bytů potřebných pro znak podle předpony:

- 1 byte: `0xxxxxxx` (ASCII znak)
- 2 byty: `110xxxxx 10xxxxxx` (např. `č`)
- 3 byty: `1110xxxx 10xxxxxx 10xxxxxx`
- 4 byty: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx` (např. emotikon `😊`)

Díky této struktuře počítač rozpozná, kolik bytů má načíst, což zajišťuje efektivitu i kompatibilitu.

**Shrnutí příkladu**

Při kódování řetězce, např. `"Ač😊"` v UTF-8, by výsledek vypadal takto:
- `A` → `01000001`
- `č` → `11000101 10101101`
- `😊` → `11110000 10011111 10011000 10101010`

V bajtech tedy `Ač😊` bude reprezentováno jako:
```
01000001 11000101 10101101 11110000 10011111 10011000 10101010
``` 

Tento způsob kódování umožňuje, aby byly současně zastoupeny všechny možné znaky z různých písem, což činí UTF-8 univerzálním kódováním pro text na webu a ve většině moderních aplikací.

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.h0qswb-mu-Ay17g7L_gwYwHaHa%26pid%3DApi&f=1&ipt=88ac91ad4993d84f5f1996a1644d85f41dead53dc1526c82b95099dfc7e5a6b1&ipo=images" width="200" style="margin-left:auto; margin-right:auto">

### Spojení se souborem pomocí Pythonu

---

Klasickou cestou, jak vytvořit obyčejný soubor je poskládat údaje (bajty) za hlavičkou, tedy **jménem souboru**.

<br>

Než ale začneš se souborem pracovat, potřebuješ si v Pythonu vytvořit *pomocný objekt*, který jej bude **zastupovat** (nebo se na něj odkazovat):

```python
muj_soubor = open(jmeno_souboru, pravidla)  # pomocný objekt

# ... libovolná ohlášení

muj_soubor.close()
```

1. `muj_soubor`, je **Pythonovský objekt** odkazující na **soubor**,
2. `open()`, *zabudovaná funkce*, která **vytváří spojení** (*stream*) mezi objektem a souborem,
3. `jmeno_souboru`, jméno souboru (*relativní* cesta/*absolutní* cesta),
4. `pravidla`, výběr argumentů upřesňujících, **jak soubor otevřít**,
5. `muj_soubor.close`, způsob, kterým **ukončíš spojení** mezi objektem a souborem.

<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.JhMJc09m94e9V3oKtb_n3AHaHa%26pid%3DApi&f=1" width="200" style="margin-left:auto; margin-right:auto">

## Textové soubory

---

Nejlepším souborem na začátek bude prostý **textový soubor**.

Textovým souborem rozuměj jakýkoliv soubor, který má příponu `.txt`.

#### Demo: Ukázka textového souboru

**Vytvoření souboru**


```python
!echo -e "Ahoj, světe!\nToto je ukázkový textový soubor." > demo.txt
```

**Metadata souboru**


```python
!stat demo.txt
```

**Binární reprezentace**


```python
!xxd -b demo.txt
```

<br>

### Úvod k souborům

---

Základními procesy pro práci se soubory obecně jsou:
1. **Čtení** souborů,
2. **Zápis** do souborů.

### Čtení souborů

---

Otevřít a přečíst *textový soubor* pomocí *editorů* jistě ovládáš.

Teď se podívej, jak můžeš naučit otevírání a čtení souborů také **interpreta Pythonu**:


```python
muj_nacteny_txt_soubor = open(demo.txt)
```


```python
muj_nacteny_txt_soubor = open('demo.txt')
```


```python
!ls
```


```python
muj_nacteny_txt_soubor = open('maj.txt',
                              mode='r',
                              encoding='UTF-8')
```

<hr>

Dávej pozor, jakým způsobem **jméno souboru** používáš. Python potřebuje pracovat s takovým datovým typem, který dobře zná.


```python
print(muj_nacteny_txt_soubor)
```

Další kolizí může být **umístění** souboru.

<br>

*Interpret* pracuje **v aktuálním umístění**.

Takže buď soubor přesuneš, nebo na něj odkážeš pomocí:
1. **Relativní cesty** (tedy vzhledem k aktuálnímu umístění),
2. **absolutní cesty** (celá cesta od *roota* nebo *jména disku*).

<br>

#### Relativní cesta
```
"muj_textovy_soubor.txt"                # v aktuální složce
"../muj_textovy_soubor.txt"             # v rodičovské složce
"../shared/onsite/muj_textovy_soubor.txt"  # v dceřinné složce 'shared', v dceřinné složce 'onsite'
```

#### Absolutní cesta, Windows
```
"C:\users\admin\docs\muj_textovy_soubor.txt"
```

#### Absolutní cesta, unix
```
"/home/user/project/shared/onsite/muj_textovy_soubor.txt"
```


```python
print(muj_nacteny_txt_soubor)
```


```python
print(type(muj_nacteny_txt_soubor))
```

<br>

Metody **pro čtění obsahu** *TextIOWrapper* objektu (zabudovaná knihovna [io](https://docs.python.org/3/library/io.html)):

1. `read` - přečte celý soubor jako jeden string,
2. `readline` - přečte pouze první řádek jako string,
3. `readlines` - přečte celý soubor jako list (co řádek, to údaj)

<br>

<details>
  <summary>▶️ Poznámky ke knihovně io</summary>
   
https://www.remnote.com/a/io/67237016d73bd77515132c26
</details>


```python
obsah_txt = muj_nacteny_txt_soubor.read()
```


```python
print(obsah_txt,
      type(obsah_txt),
      sep='\n')
```


```python
print(obsah_txt.split())
```


```python
# muj_nacteny_txt_soubor.seek(0)
```


```python
obsah_txt_list = muj_nacteny_txt_soubor.readlines()
```


```python
print(obsah_txt_list)
```

<br>

Pokud čteš jednotlivé znaky, **pomyslný kurzor** je postupně prochází.

Jakmile s ním dojdeš nakonec, **musíš jej ručně vrátit na začátek**, pokud chceš obsah souboru znovu načíst:


```python
muj_nacteny_txt_soubor.seek(0)     # Nastaví kurzor na začátek .txt souboru
```


```python
muj_txt_soubor.seek(0, 1)  # Nastaví kurzor na konec .txt souboru
```


```python
obsah_txt_list = muj_nacteny_txt_soubor.readlines()
```


```python
print(obsah_txt_list)
```


```python
print(type(obsah_txt_list))
```

Jakmile tvoje práce s textovými souborem skončí, nezapomeň soubor zavřít.

<br>

Pokud si potřebuješ jen ověřit, jestli je spojení se souborem ukončené, použij metodu `closed`:


```python
muj_nacteny_txt_soubor.closed  # is_close --> bool
```


```python
muj_nacteny_txt_soubor.close()
```


```python
muj_nacteny_txt_soubor.closed  # --> bool
```

#### Rekapitulace

---


```python
muj_nacteny_txt_soubor = open(
    'maj.txt', mode='r'
)

obsah_txt = muj_nacteny_txt_soubor.readlines()

muj_nacteny_txt_soubor.close()
```


```python
def precti_txt_soubor(jmeno_souboru: str,
                      mod: str = 'r') -> list:
    muj_nacteny_txt_soubor = open(jmeno_souboru,
                                  mode=mod)

    obsah_txt = muj_nacteny_txt_soubor.readlines()
    
    muj_nacteny_txt_soubor.close()
    
    return obsah_txt
```


```python
obsah_txt_souboru = precti_txt_soubor(
    jmeno_souboru='maj.txt'
)
```


```python
print(obsah_txt_souboru)
```

<br>

### Zápis do souborů

---

Pokud žádný textový soubor nemáš, nebo jej chceš naopak **vytvořit**, musíš jej prvně **zapsat**:


```python
muj_string = "Toto je můj nový soubor^.^"
```

<br>

*String* `muj_txt` máš aktuálně k dispozici pouze jako nějaký objekt Pythonu.

Opět je potřeba nejprve spojit **objekt v Pythonu** se skutečným souborem na disku.


```python
muj_druhy_txt_soubor = open(
    "../muj_zapsany.txt",
    mode='w'
)
```

<br>

Soubor si následně můžeš otevřít, ale zjistíš, že je **v tento moment prázdný**.

Funkce `open` pouze vytvoří (*~iniciuje*) nový objekt `muj_druhy_txt_soubor`.

Příslušný text teprve musíme zapsat, pomocí vhodné *funkce* `write`:


```python
print(muj_string)
```


```python
muj_druhy_txt_soubor.write(muj_string)
```

<br>

Spojení se souborem je **pořád aktivní**.


```python
muj_druhy_txt_soubor.closed
```


```python
muj_druhy_txt_soubor.close()
```


```python
muj_druhy_txt_soubor.closed
```

<br>

Teprve nyní je soubor uzavřený a můžeme zkontrolovat jeho obsah.


```python
muj_druhy_string = "Očekávám text na druhém řádku!"
```


```python
muj_existujici_txt = open(
    "../muj_zapsany.txt",
    mode="w"
)
```


```python
muj_existujici_txt.write(muj_druhy_string)
```


```python
muj_existujici_txt.close()
```

Teprve po ukončení *streamu* (nebo také zápisu) objektu, můžeš soubor `muj_novy_soubor.txt` prozkoumat.


```python
muj_existujici_txt = open(
    "../muj_zapsany.txt",
    mode="w"
)
```


```python
muj_string  # \n
```


```python
muj_druhy_string
```


```python
muj_existujici_txt.write(muj_string)
muj_existujici_txt.write(muj_druhy_string)
```


```python
muj_existujici_txt.close()
```


```python
muj_existujici_txt_list = open(
    "../muj_zapsany.txt",
    mode="w"
)
```


```python
# Zapíšu několik řádků současně, pomocí sekvence
muj_existujici_txt_list.writelines((muj_string, f'\n{muj_druhy_string}'))
```


```python
# TOTO NE!
# for line in (muj_string, f'\n{muj_druhy_string}'):
#     muj_existujici_txt_list.write(line)
```


```python
muj_existujici_txt_list.close()
```

<br>

### 🧠 CVIČENÍ 🧠, Vyzkoušej si práci s *textovým souborem*:

1. Funkce `zapis_zpravu_do_txt_souboru` přijímá dva parametry `zprava` a `jmeno_souboru`,
2. Funkce otevře nový soubor, zapíše zprávu a spojení se souborem ukončí,
3. Vyzkoušej funkci spustit pro dva různé textové soubory.


```python

```


```python
zapis_zpravu_do_txt_souboru(
    zprava="Ahojte, toto je testovací zpráva!",
    jmeno_souboru='test_soubor.txt'
)
```

<details>
  <summary>▶️ Klikni zde pro zobrazení řešení</summary>
   
```python
def zapis_zpravu_do_txt_souboru(zprava: str, jmeno_souboru: str) -> None:
    muj_soubor = open(jmeno_souboru, mode='w')
    muj_soubor.write(zprava)
    muj_soubor.close()

zapis_zpravu_do_txt_souboru("Ahojte, toto je testovací zpráva!", 'test_soubor.txt')
```
</details>

<br>

### Opakovaný zápis do souboru

---

Máš situaci, kdy tebou vytvořený soubor existuje a ty jej chceš znovu otevřít a rozšířit:


```python
dalsi_string = "\nRád čtu a hraji na klavír"
```

<br>

Opět potřebuješ inicializovat **pomocný objekt**, jako v předchozích scénářích:


```python
muj_stavajici_soubor = open(
    "../muj_zapsany.txt",
    mode="w"
)
```


```python
muj_stavajici_soubor.write(dalsi_string)
```


```python
muj_stavajici_soubor.close()
```

Když zkontroluješ, jak vypadá **nově přidaný text**, bude vypadat zmateně.

<br>

Pokud opětovně načteš **stejný soubor** v režimu `w`, přesuneš "zapisovač" (*představ si jej jako blikající kurzor v editoru*) opět **na začátek souboru**.

*Interpret* zapisuje od místa, kde se zapisovač nachází, takže dojde **k přepsání původního obsahu**.

<br>

Pokud chceš automaticky zapisovat **od konce souboru**, otevři soubor s argumentem `mode="a"`, tedy v režimu `append`.


```python
prvni_radek = "Ahoj, ja jsem Matouš (:"
```


```python
druhy_radek = "\nToto je druhý řádek!"
```


```python
treti_radek = "\nRád čtu, hraji na klavír"
```

<br>

V kombinaci s novým režimem **append**:


```python
muj_soubor = open("../muj_zapsany.txt", mode="a")
```


```python
muj_soubor.write(prvni_radek)
```


```python
muj_soubor.close()
```


```python
muj_soubor = open("../muj_zapsany.txt", mode="a")
```


```python
muj_soubor.write(druhy_radek)
```


```python
muj_soubor.close()
```


```python
muj_soubor = open("../muj_zapsany.txt", mode="r+")
```


```python
muj_soubor.write(treti_radek)
```


```python
muj_soubor.close()
```

<br>

Pokud budeš někdy pracovat se stejným souborem tak, že jej budeš současně:
1. **číst** soubor,
2. **zapisovat** do něj.
    
Vyzkoušej režim `r+`.


```python
muj_soubor = open("../muj_zapsany.txt", mode="r+")
```


```python
obsah_pred_zapisem = muj_soubor.readlines()
```


```python
print(obsah_pred_zapisem)
```


```python
muj_soubor.tell()
```


```python
muj_soubor.write('\nA ještě poslední řádek')
```


```python
muj_soubor.close()
```

### Práce s binárními soubory

Pokud chceme pracovat s binárními soubory, tak musíme použít `mode=rb` pro čtení nebo `mode=wb` pro zápis.

V binárním módu můžeme číst a zapisovat i textové soubory.


```python
demo_binarne = open("demo.txt", mode="rb")
```


```python
print(type(demo_binarne))
```

    <class '_io.BufferedReader'>



```python
print(demo_binarne.readlines())
```

    [b'Ahoj, sv\xc4\x9bte!\n', b'Toto je uk\xc3\xa1zkov\xc3\xbd textov\xc3\xbd soubor.\n']


Číst text je nuda. Zkusme to s obrázkem.

<figure>
<img src="./Jack_Russell_Terrier_1.jpg" style="max-width: 200px">
<figcaption style="font-size:10px">CC BY 3.0 https://commons.wikimedia.org/wiki/File:Jack_Russell_Terrier_1.jpg</figcaption>
<figure>


```python
binary_dog = open('Jack_Russell_Terrier_1.jpg', 'rb')
print(binary_dog.read(1))
print(binary_dog.read(3))
print(binary_dog.read(2))
print(binary_dog.read(1))
print(binary_dog.read(1))

```

    b'\xff'
    b'\xd8\xff\xe0'
    b'\x00\x10'
    b'J'
    b'F'



```python
binary_dog.seek(0)
print(binary_dog.readline())
binary_dog.close()
```

    b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x02\x01\x01\n'


| Hodnota         | Význam                                                    |
|-----------------|-----------------------------------------------------------|
| 0x89            | „Magické“ číslo označující začátek PNG                    |
| 0x50 0x4E 0x47  | PNG v ASCII                                               |
| 0x0D 0x0A       | Konec řádku ve stylu DOS (`\r\n`)                         |
| 0x1A            | Znak konce souboru (EOF) ve stylu DOS                     |
| 0x0A            | Konec řádku ve stylu Unix (`\n`)                          |

<hr>
<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.eUy0yqtKrsDHeiUI1dWKggHaHa%26pid%3DApi&f=1&ipt=69ae33045a754823160a963754bc498c4c560ed92d3f57186fdc778816155ef9&ipo=images" width="200" style="margin-left:auto; margin-right:auto">

### Zápis s kontextovým manažerem

Zápis můžeš doplnit/rozšířit tzv. *kontextovým manažerem*.


```python
muj_soubor = open("demo.txt", mode="r")  # open
print(muj_soubor.readlines())            # process

# Nastane chyba! IndexError --> Vadí!

muj_soubor.close()                       # close
```

<br>

Opakování a hlídání 3 základních kroků se může zdát svazující.

V Pythonu existuje klíčový výraz `with`:


```python
with open("demo.txt", mode="r") as muj_soubor:  # open
    print(muj_soubor.readlines())               # process + close

print()
```


```python
muj_soubor.closed
```

**Alternativní zápis s blokem `try` a `finally`**


```python
muj_soubor = open("demo.txt", mode="r") 
try: 
      print(muj_soubor.readlines())  
finally:
     muj_soubor.close()        


print(muj_soubor.closed)                       # close
```

<br>

### 🧠 CVIČENÍ 2 🧠, práce s textovými souborem:
---

- Definuj funkci `precti_logy`, která splňuje:
    - parametr: `soubor` (string),
    - vrací: seznam záznamů z logovacího souboru,
    - popis: Tato funkce přečte obsah logovacích souboru. Kde každý řádek bude oddělený údaj sekvence.

- definuj funkci `vyber_pouze_typ`, která splňuje:
    - parametr: `obsah_souboru` (list),
    - vrací: tuple,
    - popis: Tato funkce ze zadaného seznamu logů rozdělí každý řádek a uloží pouze typ logovací zprávy (`INFO`, `WARN`, ...). Výsledný údaj vrať jako `tuple`.


```python
zaznamy = """\
INFO 2023-07-26 10:30:22 Aplikace úspěšně spuštěna
INFO 2023-07-26 10:31:12 Uživatel přihlášen
WARN 2023-07-26 10:35:05 Nedostatek místa na disku
INFO 2023-07-26 10:36:17 Data úspěšně uložena
ERROR 2023-07-26 10:40:44 Připojení k databázi selhalo
WARN 2023-07-26 10:45:30 Možná chyba v konfiguraci
ERROR 2023-07-26 10:50:01 Nelze odeslat e-mail
INFO 2023-07-26 10:55:12 Aplikace úspěšně ukončena
"""
```

<details>
    <summary>▶️ Řešení</summary>
    
```python
def precti_logy(soubor: str) -> list:
    muj_soubor = open(soubor, mode='w')
    obsah_souboru = muj_soubor.readlines()
    return obsah_souboru
    

def vyber_pouze_typ(obsah_souboru: list) -> tuple:
    return tuple(
        [log.split()[0] for log in obsah_souboru if len(log) > 3]
    )
```
</details>

## Práce se soubory a složkami

Rozepíšu jednotlivé případy užití s příklady kódu pomocí knihovny `pathlib`:

### 1. Manipulace se složkami


- **Vytváření složky**
 


```python
from pathlib import Path

# Vytvoření nové složky
folder = Path("new_directory")
folder.mkdir(parents=True, exist_ok=True)
```

- **Přejmenování složky**


```python
new_folder = folder.rename("renamed_directory")
```

- **Mazání složky**


```python

new_folder.rmdir()  # Smaže složku, pokud je prázdná
```

### 2. Kopírování, přesouvání a mazání souborů

Tyto operace jsou klíčové při práci s různými verzemi dat nebo zálohami.

- **Kopírování souborů**
  
   `pathlib` nemá přímou podporu pro kopírování, proto použijeme `shutil`.


```python
zdroj = Path("zdrojovy_soubor.txt")
zdroj.write_text("Ahoj")
```




    4




```python
import shutil

cilova_slozka = Path("destinace")
cilova_slozka.mkdir(parents=True, exist_ok=True)
shutil.copy(zdroj, cilova_slozka)  # Kopíruje soubor na novou cestu
```




    'destinace/zdrojovy_soubor.txt'



- **Přesouvání souborů**


```python
Path(cilova_slozka / zdroj.name).rename(cilova_slozka / "kopie.txt")  # Přesune soubor na novou cestu
```




    PosixPath('destinace/kopie.txt')



- **Mazání souborů**
  


```python
kopie = cilova_slozka / "kopie.txt"
if kopie.exists():
    kopie.unlink()  # Smaže soubor

```


```python
cilova_slozka.rmdir()
```

### 3. Hledání souborů podle vzorů

Vyhledání souborů podle specifických vzorů (např. všech `.txt` souborů) se často hodí při zpracování souborů stejného typu.

- **Vyhledání všech `.txt` souborů ve složce**


```python
folder = Path(".")
txt_files = list(folder.glob("*.txt"))  # Vrátí seznam všech .txt souborů v adresáři
print(txt_files)
```

    [PosixPath('demo.txt'), PosixPath('zdrojovy_soubor.txt')]


- **Rekurzivní hledání všech `.txt` souborů ve složce a podadresářích**


```python
txt_files_recursive = list(folder.rglob("*.txt"))
print(txt_files_recursive)
```

    [PosixPath('demo.txt'), PosixPath('zdrojovy_soubor.txt'), PosixPath('task/input/vstupni_data.txt'), PosixPath('task/output/output_0.txt')]


### 4. Kontrola existence a typu souboru nebo složky

Před čtením nebo zápisem je užitečné zkontrolovat, zda soubor existuje a jestli je to soubor nebo složka.

- **Kontrola existence**


```python
file = Path("demo.txt")
if file.exists():
    print("Soubor existuje")

```

    Soubor existuje


- **Kontrola, zda jde o soubor nebo složku**


```python
if file.is_file():
    print("Jedná se o soubor")
elif file.is_dir():
    print("Jedná se o složku")
```

    Jedná se o soubor


### 5. Získávání informací o souborech

Metadata souborů, jako je velikost, datum vytvoření nebo modifikace, mohou být užitečné pro správu dat.

- **Velikost souboru**


```python
size = file.stat().st_size  # Velikost v bytech
print(f"Velikost souboru: {size} bajtů")
```

    Velikost souboru: 50 bajtů


- **Datum modifikace**


```python
import arrow # better datetime

modification_time = arrow.get(file.stat().st_mtime)
print(f"Datum modifikace: {modification_time.format("dddd, D. MMMM YYYY", locale="cs")}")

```

    Datum modifikace: čtvrtek, 7. listopad 2024


### 7. Práce s cestami a formátování cest

Práce s cestami zahrnuje vytváření, úpravy a analýzu cest k souborům a složkám, což je zásadní pro zajištění přenositelnosti a robustnosti kódu.

- **Spojování cest**  
  `pathlib` umožňuje snadno kombinovat cesty pomocí `/` operátoru, což dělá kód čitelnější a zabraňuje chybám při vytváření cest.
  


```python
base_dir = Path("task")
sub_dir = base_dir / "sub_directory"
file_path = sub_dir / "file.txt"
print(file_path)  # Výstup: base_directory/sub_directory/file.txt

```

    task/sub_directory/file.txt


- **Získání absolutní cesty**
  Použití `.resolve()` vám umožní získat absolutní cestu k souboru nebo složce, což může být užitečné při práci s různými adresáři.


```python
absolute_path = file_path.resolve()
print(f"Absolutní cesta: {absolute_path}")
```

    Absolutní cesta: /mnt/Data/Drive/Projekty/Pracovní/Engeto/Materiály/Python/Engeto-python-academy-dan/Lekce 09/new_directory/sub_directory/file.txt


- **Rodičovské složky**  
  Pomocí `.parent` můžeme přistupovat k rodičovské složce souboru nebo složky, a `.parents` poskytuje přístup k vyšším úrovním v cestě.


```python
print(file_path.parent)  # Vrátí jednu úroveň nad file_path
print(file_path.parents[0])  # Taky jednu úroveň nad file_path
print(file_path.parents[1])  # Dvě úrovně nad file_path

```

    new_directory/sub_directory
    new_directory/sub_directory
    new_directory


- **Rozdělení cesty na části**  
  Pomocí atributu `.parts` lze rozdělit cestu na jednotlivé části, což se hodí při analýze cesty.


```python
parts = file_path.parts
print(parts)  # Výstup: ('base_directory', 'sub_directory', 'file.txt')
```

    ('new_directory', 'sub_directory', 'file.txt')


- **Název souboru a přípona**  
  Cesta může být rozdělena na samotný název souboru a jeho příponu. To se hodí při kontrole typu souboru nebo přejmenování.


```python
print(file_path.name)     # Výstup: 'file.txt' - název souboru s příponou
print(file_path.stem)     # Výstup: 'file' - pouze název bez přípony
print(file_path.suffix)   # Výstup: '.txt' - pouze přípona souboru

```

    file.txt
    file
    .txt


- **Změna přípony souboru**  
  `with_suffix()` umožňuje změnit příponu, což je užitečné, pokud pracujeme s různými formáty dat nebo potřebujeme ukládat kopie v jiném formátu.


```python
new_file_path = file_path.with_suffix(".md")
print(new_file_path)  # Výstup: base_directory/sub_directory/file.md

```

    new_directory/sub_directory/file.md


- **Kontrola, zda je cesta absolutní nebo relativní**  
  Cesty mohou být buď absolutní (od kořene souborového systému) nebo relativní (od aktuálního pracovního adresáře). `pathlib` umožňuje snadno zjistit, zda je cesta absolutní.
  


```python
print(file_path.is_absolute())  # Výstup: False, protože je relativní
print(file_path.resolve().is_absolute())  # Výstup: True

```

    False
    True


- **Iterace přes podadresáře a soubory**  
  Metoda `.iterdir()` umožňuje procházet adresář a získat všechny položky v něm.


```python
for item in base_dir.iterdir():
    print(item)  # Vypíše všechny soubory a složky v base_directory

```

    task/implementace.py
    task/implementace2.py
    task/input
    task/output
    task/vzor.py
    task/__pycache__


- **Normalizace cesty**  
  `pathlib` automaticky normalizuje cesty odstraněním nadbytečných lomítek a řešením zkratek jako `.` a `..`.


```python
normalized_path = Path("some_dir/../some_dir/file.txt").resolve()
print(normalized_path)  # Výstup: absolutní cesta k 'some_dir/file.txt'
```

    /mnt/Data/Drive/Projekty/Pracovní/Engeto/Materiály/Python/Engeto-python-academy-dan/Lekce 09/some_dir/file.txt


- **Kombinace s relativní cestou**  
  Můžeme kombinovat cesty pomocí `.relative_to()`, což nám umožňuje získat relativní cestu k určitému základnímu adresáři.


```python
relative_path = file_path.relative_to(base_dir)
print(relative_path)  # Výstup: sub_directory/file.txt

```

    sub_directory/file.txt


<br>

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.eIepNW0QqoKS0nHKxdHb_gHaHa%26pid%3DApi&f=1&ipt=f8fbd56c24a7f9c26b35553a95d220e93ce3bdce6bce019cdf455c712cd8e1b5&ipo=images" width="200" style="margin-left:auto; margin-right:auto">

## Formátování řetězců (~string formatting)

---

Jde o způsob, jakým efektivně zapisovat klasický string ve spojením se jmény proměnných, doplňujícím upravováním a dalšími variantami.

<br>

### Formátování řetězců

---

Povíme si více o těchto třech způsobech:
1. **Formátovací výraz** (`%`-formatting)
2. **Formátovací metoda** (`str.format()`)
3. **Formátovaný string** (`f""`)

<br>

### Formátovací výraz

---

Je to prapůvodní způsob formátování stringu v Pythonu už od uplného začátku:


```python
JMENO = "Lukas"
VEK = 27
"Ahoj, jmenuji se %s a je mi %d let" % (JMENO, VEK)
```

<br>

**Pozor!** dnes se již oficiálně nedoporučuje, jelikož často selhává, nesprávně zobrazuje tuple nebo slovníky. Vypisování není příliš praktické.

<br>

### Formátovací metoda

---

Od verze Pythonu 2.6 máme k dispozici další způsob pro formátování:


```python
JMENO = "Eliška"
VEK = 26
"Ahoj, jmenuji se {} a je mi {} let".format(JMENO, VEK)
```


```python
JMENO = "Eliška"
VEK = 26
"Ahoj, jmenuji se {} a je mi {} let".format(VEK, JMENO)
```


```python
JMENO = "Eliška"
VEK = 26
"Ahoj, jmenuji se {1} a je mi {0} let".format(VEK, JMENO)
```

<br>

**Pozor!** použití je pořád poměrně upovídaní např. při zápisu více proměnných. Má rozhodně široké možnosti formátování, ale vždy prakticky použitelné.

<br>

### 🔝 Formátovaný string (f-string)

---

Od verze Pythonu 3.6 máme k dispozici ještě třetí metodu pro formátování stringů.


```python
JMENO = "Lucie"
VEK = 28
f"Ahoj, jmenuji se {JMENO} a je mi {VEK} let"
```

<br>

Syntaxe je stručná přesto čitelná. Zvládá různé platné operace v Pythonu včetně volání funkcí. Opatrně při důsledném zapisování uvozovek.


```python
f"|{JMENO:^10}|{VEK:^10}|"
```

<br>

Vhodná také pro zaokrouhlování desetinných čísel a převádění číselných hodnot na procenta:


```python
value = 11.1234
print(f"value: {value:.2f}")
```


```python
data = {'name': 'Matouš'}
print(f"Ahoj, já jsem {data["name"]}")
```

<details>
    <summary>▶️ Více metod f-strings</summary>
    
[https://www.remnote.com/a/f-string/672a2e78334d7d91da25dabc](https://www.remnote.com/a/f-string/672a2e78334d7d91da25dabc)
</details>

[Formulář po deváté lekci](https://forms.gle/Py5UjJ8573DLLdCr8)

---


<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.GMJvJ-GG0YS8H5JmHR3CbwHaHm%26pid%3DApi&f=1" width="200" style="margin-left:auto; margin-right:auto" />


## Domácí úkol

---
