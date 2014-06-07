import dson
def test_default():
    assert dson.dumps(type, default=repr) == dson.dumps(repr(type))
