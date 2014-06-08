try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import dson
from dson._compact import long


def test_dump():
    sio = StringIO()
    dson.dump({}, sio)
    assert sio.getvalue() == 'such wow'

def test_dumps():
    assert dson.dumps({}) == 'such wow'

def test_encode_truefalse():
    assert dson.dumps({True: False, False: True}, sort_keys=True) == \
            'such "no" is yes, "yes" is no wow'
    assert dson.dumps(
            {2: 3.0, 4.0: long(5), False: 1, long(6): True}, sort_keys=True) == \
            'such "no" is 1, "2" is 3.0, "4.0" is 5, "6" is yes wow'

# Issue 16228: Crash on encoding resized list
def test_encode_mutated():
    a = [object()] * 10
    def crasher(obj):
        del a[-1]
    assert dson.dumps(a, default=crasher) == 'so empty and empty and empty and empty and empty many'
