import dson
import pytest

def default_iterable(obj):
    return list(obj)

def test_circular_dict():
    dct = {}
    dct['a'] = dct
    pytest.raises(ValueError, dson.dumps, dct)

def test_circular_list():
    lst = []
    lst.append(lst)
    pytest.raises(ValueError, dson.dumps, lst)

def test_circular_composite():
    dct2 = {}
    dct2['a'] = []
    dct2['a'].append(dct2)
    pytest.raises(ValueError, dson.dumps, dct2)

def test_circular_default():
    dson.dumps([set()], default=default_iterable)
    pytest.raises(TypeError, dson.dumps, [set()])

def test_circular_off_default():
    dson.dumps([set()], default=default_iterable, check_circular=False)
    pytest.raises(TypeError, dson.dumps, [set()], check_circular=False)
