## Slovníky a množiny

1. **Datový typ `dict` (slovník)**:
   - Vytváření slovníků (`{key: value}`).
   - Přístup k hodnotám pomocí klíče (`dict[key]`).
   - Vytváření slovníků pomocí `dict()` nebo `{}`.
   - Přidávání a modifikace klíčů a hodnot (`dict[key] = value`).
   - Vnořené slovníky (slovníky obsahující jiné slovníky).
   - Metody pro práci se slovníky (`get()`, `keys()`, `values()`, `items()`, `update()`, `pop()`, `clear()`, `copy()`, `setdefault()`, `fromkeys()`).
   - Mělká vs. hluboká kopie slovníku.
   - Testování existence klíče (`in`).

2. **Datový typ `set` (množina)**:
   - Vytváření množin (`{value1, value2}` nebo `set()`).
   - Přidávání a odebírání prvků (`add()`, `remove()`, `discard()`, `pop()`).
   - Množinové operace: sjednocení (`|`), průnik (`&`), rozdíl (`-`), symetrický rozdíl (`^`).
   - Metody množin (`union()`, `intersection()`, `difference()`, `symmetric_difference()`, `issubset()`, `issuperset()`, `isdisjoint()`).
   - Kopírování množin (`copy()`).
   - Testování existence prvků v množině (`in`).

3. **Datový typ `frozenset` (neměnitelná množina)**:
   - Vytváření `frozenset()`.
   - Vlastnosti `frozenset` (neměnitelnost).
   - Použití množinových operací s `frozenset`.

4. **Volitelné argumenty v zabudovaných funkcích**:
   - Použití volitelných argumentů v `print()`, `dict.get()`, atd.
   - Princip práce s volitelnými argumenty v různých funkcích.

5. **Praktické použití slovníků a množin**:
   - Vytváření aplikací na základě slovníků a množin (např. filmový slovník).
   - Manipulace s daty pomocí metod a operátorů.
   - Testování existence klíčů a hodnot.