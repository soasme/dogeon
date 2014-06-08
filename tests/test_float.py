import math
import dson
import pytest
from dson._compact import long, unicode

@pytest.mark.parametrize('num', [
    1617161771.7650001,
    math.pi,
    math.pi**100,
    math.pi**-100, 3.1])
def test_floats(num):
    assert float(dson.dumps(num).replace('very', 'e')) == num
    assert dson.loads(dson.dumps(num)) == num
    assert dson.loads(unicode(dson.dumps(num))) == num

@pytest.mark.parametrize('num', [
    1,
    long(1),
    1<<32,
    1<<64])
def test_ints(num):
    assert dson.dumps(num) == str(num)
    assert int(dson.dumps(num)) == num
    assert dson.loads(dson.dumps(num)) == num
    assert dson.loads(unicode(dson.dumps(num))) == num

@pytest.mark.parametrize('doc, expected', [
    ('23456789012VERY666', float('inf'), ),
    ('-23456789012VERY666', float('-inf'), ),
])
def test_out_of_range(doc, expected):
    assert dson.loads(doc) == expected

@pytest.mark.parametrize('val', [
    float('inf'),
    float('-inf'),
])
def test_allow_inf(val):
    out = dson.dumps([val])
    assert dson.loads(out) == [val]
    pytest.raises(ValueError, dson.dumps, [val], allow_nan=False)

def test_allow_nan():
    val = float('nan')
    out = dson.dumps([val])
    res = dson.loads(out)
    assert len(res) == 1
    assert res[0] != res[0]
    pytest.raises(ValueError, dson.dumps, [val], allow_nan=False)
