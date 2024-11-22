
# test_mypy_errors.py

from typing import List, Dict, Tuple, Optional, Union, Any, Callable

# 1. Nesprávný návratový typ
def add(a: int, b: int) -> int:
    return str(a + b)  # Chyba: Funkce má vracet int, ale vrací str

# 2. Chybná anotace proměnné
age: str = 25  # Chyba: Typ age je anotován jako str, ale přiřazeno je int

# 3. Špatné typy v seznamu
names: List[int] = ["Alice", "Bob", "Charlie"]  # Chyba: Seznam int, ale přiřazen je seznam str

# 4. Volitelný typ s nevhodnou kontrolou
def greet(name: Optional[str]) -> str:
    return "Hello, " + name  # Chyba: name může být None, což nelze konkatenovat se str

# 5. Nesprávné typy ve slovníku
user_data: Dict[str, int] = {"name": "Daniel", "age": "30"}  # Chyba: age má být int, ale je str

# 6. Sjednocení typů s chybou
def process_data(value: Union[int, str]) -> int:
    return value + 10  # Chyba: Union neumožňuje automatickou konverzi str na int

# 7. Volání funkce s chybnými typy argumentů
def multiply(a: int, b: int) -> int:
    return a * b

result = multiply("5", 10)  # Chyba: Argument a má být int, ale je str

# 8. Callable s nesprávnými typy
def operate(func: Callable[[int, int], int], x: int, y: int) -> int:
    return func(x, y)

def invalid_func(a: str, b: str) -> str:
    return a + b

operate(invalid_func, 5, 10)  # Chyba: invalid_func má špatné typy argumentů i návratový typ

# 9. Použití `Any` bez jasného určení typu
data: Any = "Hello"
number: int = data  # Chyba: mypy odhalí, že data může být libovolného typu

# 10. Typový alias s chybným přiřazením
UserData = Dict[str, str]
user: UserData = {"id": 1, "name": "Alice"}  # Chyba: id má být str, ale je int

# 11. Typový alias pro n-tice s nesprávným typem
Point = Tuple[int, int]
location: Point = (1.5, 2.5)  # Chyba: Tuple má mít int, ale má float

# 12. Zanedbání typu None u návratového typu Optional
def find_user(user_id: int) -> Optional[str]:
    return None

user = find_user(1) + " found"  # Chyba: find_user může vracet None, nelze přidat k str

# 13. Typy přiřazené špatně u parametrů funkce
def divide(a: int, b: int) -> float:
    return a / b

result = divide(10, "2")  # Chyba: b má být int, ale je str

# 14. Nesprávné volání funkce s Optional
def process_name(name: Optional[str]) -> str:
    return name.upper()  # Chyba: name může být None

# 15. Chybný typový alias se seznamem
IntList = List[int]
numbers: IntList = [1, 2, "3", 4]  # Chyba: Seznam má obsahovat pouze int, ale obsahuje str

# 16. Funkce s chybným návratovým typem
def get_number() -> int:
    return "42"  # Chyba: Funkce má vracet int, ale vrací str

# 17. Chybný typ při inicializaci třídy
class Car:
    def __init__(self, speed: int) -> None:
        self.speed = speed

my_car = Car("fast")  # Chyba: speed má být int, ale je str

# 18. Kombinace Optional a Union s nevhodným typem
def get_age(age: Union[int, None]) -> int:
    return age  # Chyba: age může být None, což nelze přiřadit k int

# 19. Nesprávné volání Callable s typem návratu
def apply_operation(func: Callable[[int, int], str], x: int, y: int) -> str:
    return func(x, y)

def add_ints(a: int, b: int) -> int:
    return a + b

result = apply_operation(add_ints, 5, 10)  # Chyba: add_ints má špatný návratový typ

# # 20. Kombinace typů s chybou
# def concatenate(x: Union[int, str], y: Union[int, str]) -> str:b
#     return x + y  # Chyba: mypy neví, jak provést součet pro int + str

