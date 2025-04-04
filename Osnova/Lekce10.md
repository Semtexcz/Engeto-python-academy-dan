### 📁 Chyby a výjimky v Pythonu

1. **Traceback**:
   - Co je to **traceback** a jak ho číst (cesta k chybě, typ chyby, popis chyby).
   - Význam tracebacku pro identifikaci místa a příčiny chyby.

2. **Druhy chyb**:
   - **Syntaktické chyby** – chyby při psaní kódu.
   - **Běhové chyby** – chyby při spuštění programu (např. TypeError, NameError).
   - **Logické chyby** – kód se spustí, ale nefunguje správně.

3. **Běhové chyby a jejich druhy**:
   - `NameError`
   - `TypeError`
   - `ValueError`
   - `IndexError`
   - `KeyError`
   - `AttributeError`
   - `ZeroDivisionError`
   - `ImportError`
   - `FileNotFoundError`
   - `OverflowError`
   - `MemoryError`
   - `RecursionError`

4. **Odchytávání výjimek (try-except)**:
   - Použití `try-except` pro ošetření výjimek.
   - Použití `try-except-else-finally` pro komplexní odchytávání chyb.
   - Specifikace typu výjimky (`except TypeError:`).
   - Použití `except Exception as error` pro získání informací o chybě.

5. **Testování kódu a kontrola chyb**:
   - Použití knihovny `mypy` pro kontrolu typů.
   - Testování pomocí `pytest` – psaní testů, spouštění testů, využití dekorátorů `@pytest.mark.parametrize`.

6. **Debugování**:
   - Použití funkcí `print()`, `type()`, `dir()`, `vars()`, `locals()`, `globals()` při hledání chyb.
   - Debugování pomocí `pdb` (Python debugger).
   - Debugování v prostředí IDE (např. PyCharm).

7. **Logování chyb**:
   - Použití modulu `logging` pro záznam chyb a událostí.
   - Výhody logování oproti `print()`.
   - Záznamy do souborů, nastavení úrovní (`DEBUG`, `INFO`, `WARNING`, `ERROR`, `CRITICAL`).
   - Použití knihovny `loguru` pro uživatelsky přívětivé logování.

8. **Úprava a refaktoring kódu na základě chyb**:
   - Vylepšování kódu na základě výpisu tracebacku.
   - Přepis kódu tak, aby byl čitelnější a jednodušší na debugování.