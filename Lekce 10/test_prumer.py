import pytest

from prumer import vypocti_prumer_dvou_cisel

# Parametrizace s několika testovacími případy
@pytest.mark.parametrize("a, b, expected", [
    (3, 5, 4),      # průměr z 3 a 5 je 4
    (10, 20, 15),   # průměr z 10 a 20 je 15
    (0, 0, 0),      # průměr z 0 a 0 je 0
    (-4, 4, 0),     # průměr z -4 a 4 je 0
    (7, 3, 5)       # průměr z 7 a 3 je 5
])
def test_vypocti_prumer_dvou_cisel(a, b, expected):
    assert vypocti_prumer_dvou_cisel(a, b) == expected
