from builtins import *
from pprint import pprint

jmeno = "Matouš"

# print("\n\n\n")
# print(globals())
# print("\n\n\n")

def ukaz_ramec(): # CO je ve funkci tam zůstává
    print(jmeno)

    print("\n\n\n")
    pprint(globals())
    print("\n\n\n")

    PI = 3.14
    return f"Ukazuji rámec konstanty PI, {PI}"

print(ukaz_ramec())
# print(PI)