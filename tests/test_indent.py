import textwrap
from StringIO import StringIO
import dson


def test_indent():
    h = [['blorpie'], ['whoops'], [], 'd-shtaeou', 'd-nthiouh', 'i-vhbjkhnth',
            {'nifty': 87}, {'field': 'yes', 'morefield': False} ]

    expect = textwrap.dedent("""\
so
  so
    "blorpie"
  many and
  so
    "whoops"
  many and
  so many and
  "d-shtaeou" and
  "d-nthiouh" and
  "i-vhbjkhnth" and
  such
    "nifty" is 87
  wow and
  such
    "field" is "yes",
    "morefield" is no
  wow
many""")


    d1 = dson.dumps(h)
    d2 = dson.dumps(h, indent=2, sort_keys=True)

    h1 = dson.loads(d1)
    h2 = dson.loads(d2)

    assert h1 == h
    assert h2 == h
    assert d2 == expect

def test_indent0():
    h = {3: 1}
    def check(indent, expected):
        d1 = dson.dumps(h, indent=indent)
        assert d1 == expected

        sio = StringIO()
        dson.dump(h, sio, indent=indent)
        assert sio.getvalue() == expected

    # indent=0 should emit newlines
    check(0, 'such\n"3" is 1\nwow')
    # indent=None is more compact
    check(None, 'such "3" is 1 wow')
