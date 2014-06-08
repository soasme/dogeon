import dson
import pytest
from dson._compact import xrange


class DSONTestObject(object):
    pass


def test_listrecursion():
    x = []
    x.append(x)
    pytest.raises(ValueError, dson.dumps, x)

    x = []
    y = [x]
    x.append(y)
    pytest.raises(ValueError, dson.dumps, x)

    y = []
    x = [y, y]
    # ensure that the marker is cleared
    dson.dumps(x)

def test_dictrecursion():
    x = {}
    x["test"] = x
    pytest.raises(ValueError, dson.dumps, x)

    x = {}
    y = {"a": x, "b": x}
    # ensure that the marker is cleared
    dson.dumps(x)

def test_defaultrecursion():
    class RecursiveJSONEncoder(dson.DSONEncoder):
        recurse = False
        def default(self, o):
            if o is DSONTestObject:
                if self.recurse:
                    return [DSONTestObject]
                else:
                    return 'DSONTestObject'
            return dson.DSONEncoder.default(o)

    enc = RecursiveJSONEncoder()
    assert enc.encode(DSONTestObject) == '"DSONTestObject"'
    enc.recurse = True
    pytest.raises(ValueError, enc.encode, DSONTestObject)


def test_highly_nested_objects_decoding():
    # test that loading highly-nested objects doesn't segfault when C
    # accelerations are used. See #12017
    # str
    with pytest.raises(RuntimeError):
        dson.loads('such "a" is ' * 100000 + ' 1 ' + ' wow ' * 100000)
    with pytest.raises(RuntimeError):
        dson.loads('such "a" is ' * 100000 + ' so 1 many ' + ' wow ' * 100000)
    with pytest.raises(RuntimeError):
        dson.loads('so ' * 100000 + ' 1 ' + ' many ' * 100000)
    # unicode
    with pytest.raises(RuntimeError):
        dson.loads(u'such "a" is ' * 100000 + u' 1 ' + u' wow ' * 100000)
    with pytest.raises(RuntimeError):
        dson.loads(u'such "a" is ' * 100000 + u' so 1 many' + u' wow ' * 100000)
    with pytest.raises(RuntimeError):
        dson.loads(u'so ' * 100000 + u' 1 ' + u' many ' * 100000)

def test_highly_nested_objects_encoding():
    # See #12051
    l, d = [], {}
    for x in xrange(100000):
        l, d = [l], {'k':d}
    with pytest.raises(RuntimeError):
        dson.dumps(l)
    with pytest.raises(RuntimeError):
        dson.dumps(d)

def test_endless_recursion():
    # See #12051
    class EndlessJSONEncoder(dson.DSONEncoder):
        def default(self, o):
            """If check_circular is False, this will keep adding another list."""
            return [o]

    with pytest.raises(RuntimeError):
        EndlessJSONEncoder(check_circular=False).encode(5j)
