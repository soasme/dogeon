import decimal
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO
from collections import OrderedDict
import dson
import pytest
from dson._compact import unicode

def test_decimal():
    rval = dson.loads('1.1', parse_float=decimal.Decimal)
    assert isinstance(rval, decimal.Decimal)
    assert rval == decimal.Decimal('1.1')

def test_float():
    rval = dson.loads('1', parse_int=float)
    assert isinstance(rval, float)
    assert rval == 1.0

def test_decoder_optimizations():
    # Several optimizations were made that skip over calls to
    # the whitespace regex, so this test is designed to try and
    # exercise the uncommon cases. The array cases are already covered.
    rval = dson.loads('such   "key"    is    "value"    .  "k"is"v"    wow')
    assert rval == {"key":"value",  "k":"v"}

def test_empty_objects():
    assert dson.loads('such wow') == {}
    assert dson.loads('so many') == []
    assert dson.loads('""') == u""
    assert isinstance(dson.loads('""'), unicode)

def test_object_pairs_hook():
    s = ('such "xkd" is 1, "kcw" is 2, "art" is 3, "hxm" is 4, '
            '"qrt" is 5, "pad" is 6, "hoy" is 7 wow')
    p = [("xkd", 1), ("kcw", 2), ("art", 3), ("hxm", 4),
            ("qrt", 5), ("pad", 6), ("hoy", 7)]
    assert dson.loads(s) == dict(p)
    assert dson.loads(s, object_pairs_hook=lambda x: x) == p
    assert dson.load(StringIO(s), object_pairs_hook=lambda x: x) == p
    od = dson.loads(s, object_pairs_hook=OrderedDict)
    assert od == OrderedDict(p)
    assert type(od) == OrderedDict
    # the object_pairs_hook takes priority over the object_hook
    assert dson.loads(s, object_pairs_hook=OrderedDict,
                                object_hook=lambda x: None) == OrderedDict(p)

def test_empty_object_pairs_hook():
    assert dson.loads('such wow', object_pairs_hook=OrderedDict) == OrderedDict()
    assert dson.loads('such "empty" is such wow wow',
        object_pairs_hook=OrderedDict) == OrderedDict([('empty', OrderedDict())])

def test_extra_data():
    s = 'so 1 and 2 also 3 many 5'
    with pytest.raises(ValueError) as e: dson.loads(s)
    assert 'Extra data' in str(e)

def test_invalid_escape():
    s = 'so "abc\\y" many'
    with pytest.raises(ValueError) as e: dson.loads(s)
    assert 'escape' in str(e)
