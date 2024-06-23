import pytest
from string_utils import StringUtils


"""capitalize"""


def test_capitilize():
    utils1 = StringUtils()
    resultat = utils1.capitilize("skypro")
    assert resultat == "Skypro"


@pytest.mark.xfail
def test_capitilize2():
    utils1 = StringUtils()
    resultat = utils1.capitilize("hello friends")
    assert resultat == "Hello friend"


def test_capitilize3():
    utils1 = StringUtils()
    resultat = utils1.capitilize("123")
    assert resultat == "123"


def test_capitilize4():
    utils1 = StringUtils()
    resultat = utils1.capitilize("")
    assert resultat == ""


def test_capitilize5():
    utils1 = StringUtils()
    resultat = utils1.capitilize(" ")
    assert resultat == " "


def test_capitilize6():
    utils1 = StringUtils()
    resultat = utils1.capitilize("None")
    assert resultat == "None"


"""trim"""


def test_trim():
    utils1 = StringUtils()
    resultat = utils1.trim("   skypro")
    assert resultat == "skypro"


def test_trim1():
    utils1 = StringUtils()
    resultat = utils1.trim("   Hello friends ")
    assert resultat == "Hello friends "


def test_trim2():
    utils1 = StringUtils()
    resultat = utils1.trim(" Hello ")
    assert resultat == "Hello "


@pytest.mark.xfail
def test_trim3():
    utils1 = StringUtils()
    resultat = utils1.trim("Hello")
    assert resultat == "Hello"


"""to_list"""


def test_to_list():
    utils1 = StringUtils()
    resultat = utils1.to_list("a,b,c,d")
    assert resultat == ["a", "b", "c", "d"]


@pytest.mark.xfail
def test_to_list1():
    utils1 = StringUtils()
    resultat = utils1.to_list("1:2:3", ":")
    assert resultat == "1:2:3", ":"


@pytest.mark.xfail
def test_to_list2():
    utils1 = StringUtils()
    resultat = utils1.to_list("None")
    assert resultat == []


@pytest.mark.xfail
def test_to_list3():
    utils1 = StringUtils()
    resultat = utils1.to_list("1, 2, 3 4", None)
    assert resultat == ["1", "2", "3 4"]


"""contains"""


@pytest.mark.parametrize("input_str, char, expected_result", [
    ("SkyPro", "S", True),
    ("Hello", "o", True),
    ("Python", "X", False)
])
def test_contains(input_str, char, expected_result):
    utils = StringUtils()
    assert utils.contains(input_str, char) == expected_result


"""delete_symbol"""


@pytest.mark.parametrize("string, symbol, result", [
    ("Боль", "Б", "оль"),
    ("Койот", "К", "ойот"),
    ("SkyPro", "S", "kyPro"),
    ("Hello", "H", "ello")
])
def test_delete_symbol(string, symbol, result):
    utils1 = StringUtils()
    assert utils1.delete_symbol(string, symbol)


def test_delete_symbol1():
    utils1 = StringUtils()
    resultat = utils1.delete_symbol("Боль", "Б")
    assert resultat == "оль"


def test_delete_symbol2():
    utils1 = StringUtils()
    resultat = utils1.delete_symbol("Койот", "К")
    assert resultat == "ойот"


def test_delete_symbol3():
    utils1 = StringUtils()
    resultat = utils1.delete_symbol("SkyPro", "S")
    assert resultat == "kyPro"


def test_delete_symbol4():
    utils1 = StringUtils()
    resultat = utils1.delete_symbol("Hello", "H")
    assert resultat == "ello"


@pytest.mark.xfail
def test_delete_symbol5():
    utils1 = StringUtils()
    resultat = utils1.delete_symbol("Койот", "П")
    assert resultat == "Койот"


"""starts_with"""


@pytest.mark.parametrize("string, symbol, result", [
    ("Боль", "Б", True),
    ("Койот", "К", True),
    ("SkyPro", "S", True),
    ("Hello", "h", False)
])
def test_starts_with(string, symbol, result):
    utils1 = StringUtils()
    res = utils1.starts_with(string, symbol)
    assert res == result


"""end_with"""


@pytest.mark.parametrize("string, symbol, result", [
    ("Боль", "ь", True),
    ("Койот", "т", True),
    ("SkyPro", "o", True),
    ("Hello", "h", False)
])
def test_end_with(string, symbol, result):
    utils1 = StringUtils()
    res = utils1.end_with(string, symbol)
    assert res == result


"""is_empty"""


@pytest.mark.parametrize("string, result", [
    ("", True),
    (" ", True),
    ("  ", True),
    ("Hello", False),
    (" hello friends ", False)
])
def test_is_empty(string, result):
    utils1 = StringUtils()
    res = utils1.is_empty(string)
    assert res == result


"""list_to_string"""


@pytest.mark.parametrize("lst, joiner, result", [
    (["s", "o", "s"], ",", "s,o,s"),
    ([1, 2, 3, 4, 5], None, "1, 2, 3, 4, 5"),
    (["Sky", "Pro"], "-", "Sky-Pro"),
    (["Г", "а", "з"], "", "Газ"),

    ([], None, ""),
    ([], ",", ""),
    ([], "код", "")
])
def test_list_to_string(lst, joiner, result):
    utils1 = StringUtils()
    if joiner is None:
        res = utils1.list_to_string(lst)
    else:
        res = utils1.list_to_string(lst, joiner)
    assert res == result
