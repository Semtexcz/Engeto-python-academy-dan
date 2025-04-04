### 📁 Práce se soubory a adresáři

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
