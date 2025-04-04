1. **Obecně ke knihovnám**:
   - Co je to knihovna v Pythonu (soubory `.py` obsahující opakovaně použitelný kód).
   - Dělení knihoven na **moduly** (jednotlivé `.py` soubory) a **balíčky** (složky obsahující více modulů).

2. **Proč používat knihovny**:
   - Opakované využití kódu.
   - Snížení množství psaného kódu.
   - Možnost využívat práci jiných programátorů.

3. **Nahrávání knihoven (importování)**:
   - `import <knihovna>` (standardní způsob).
   - `from <knihovna> import *` (nahrává všechny objekty z knihovny, nebezpečné kvůli možným konfliktům názvů).
   - `from <knihovna> import <objekt>` (nahrání pouze konkrétního objektu, např. funkce nebo proměnné).
   - `from <knihovna> import <objekt> as <alias>` (přidělení aliasu pro objekt).
   - `import <knihovna> as <alias>` (přidělení aliasu pro knihovnu).

4. **Použití knihoven v Pythonu**:
   - Příklady použití vestavěných knihoven: `random`, `os`, `sys`, `collections`.
   - Metody `dir()` a `help()` pro zjišťování obsahu knihoven a jejich dokumentace.

5. **Moduly**:
   - Co je to modul (`.py` soubor).
   - Importování vlastních modulů.
   - Rozdíl mezi moduly a balíčky.

6. **Vlastní moduly**:
   - Jak vytvořit a importovat vlastní modul.
   - Použití `help()` k dokumentaci modulů.

7. **Balíčky**:
   - Co je to balíček (složka obsahující více `.py` souborů).
   - Speciální soubory v balíčku: `__init__.py`, `__pycache__`.
   - Jak vytvořit a importovat vlastní balíček.

8. **Knihovny třetích stran**:
   - Rozdíl mezi standardními a externími knihovnami.
   - Použití `pip` pro instalaci balíčků.
   - Virtuální prostředí (`venv`) a jeho používání.
   - Jak vytvořit `requirements.txt` pro správu závislostí.

9. **Praktické cvičení s knihovnami a moduly**:
   - Práce s externími knihovnami (např. `statistics`, `random`).
   - Vytvoření a import vlastních modulů.
   - Tvorba vlastního balíčku s více moduly.