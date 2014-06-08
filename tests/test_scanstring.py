import sys
import pytest
import dson


def test_scanstring():
    scanstring = dson.decoder.scanstring
    assert \
        scanstring('"z\\ud834\\udd20x"', 1, None, True) == \
        (u'z\U0001d120x', 16)

    if sys.maxunicode == 65535:
        assert \
            scanstring(u'"z\U0001d120x"', 1, None, True) == \
            (u'z\U0001d120x', 6)
    else:
        assert \
            scanstring(u'"z\U0001d120x"', 1, None, True) == \
            (u'z\U0001d120x', 5)

    assert \
        scanstring('"\\u007b"', 1, None, True) == \
        (u'{', 8)

    assert \
        scanstring('"A JSON payload should be an object or array, not a string."', 1, None, True) == \
        (u'A JSON payload should be an object or array, not a string.', 60)

    assert \
        scanstring('["Unclosed array"', 2, None, True) == \
        (u'Unclosed array', 17)

    assert \
        scanstring('["extra comma",]', 2, None, True) == \
        (u'extra comma', 14)

    assert \
        scanstring('["double extra comma",,]', 2, None, True) == \
        (u'double extra comma', 21)

    assert \
        scanstring('["Comma after the close"],', 2, None, True) == \
        (u'Comma after the close', 24)

    assert \
        scanstring('["Extra close"]]', 2, None, True) == \
        (u'Extra close', 14)

    assert \
        scanstring('{"Extra comma": true,}', 2, None, True) == \
        (u'Extra comma', 14)

    assert \
        scanstring('{"Extra value after close": true} "misplaced quoted value"', 2, None, True) == \
        (u'Extra value after close', 26)

    assert \
        scanstring('{"Illegal expression": 1 + 2}', 2, None, True) == \
        (u'Illegal expression', 21)

    assert \
        scanstring('{"Illegal invocation": alert()}', 2, None, True) == \
        (u'Illegal invocation', 21)

    assert \
        scanstring('{"Numbers cannot have leading zeroes": 013}', 2, None, True) == \
        (u'Numbers cannot have leading zeroes', 37)

    assert \
        scanstring('{"Numbers cannot be hex": 0x14}', 2, None, True) == \
        (u'Numbers cannot be hex', 24)

    assert \
        scanstring('[[[[[[[[[[[[[[[[[[[["Too deep"]]]]]]]]]]]]]]]]]]]]', 21, None, True) == \
        (u'Too deep', 30)

    assert \
        scanstring('{"Missing colon" null}', 2, None, True) == \
        (u'Missing colon', 16)

    assert \
        scanstring('{"Double colon":: null}', 2, None, True) == \
        (u'Double colon', 15)

    assert \
        scanstring('{"Comma instead of colon", null}', 2, None, True) == \
        (u'Comma instead of colon', 25)

    assert \
        scanstring('["Colon instead of comma": false]', 2, None, True) == \
        (u'Colon instead of comma', 25)

    assert \
        scanstring('["Bad value", truth]', 2, None, True) == \
        (u'Bad value', 12)


@pytest.mark.skipif(sys.version_info > (3,0), reason="requires PY2")
def test_issue3623():
    pytest.raises(ValueError, dson.decoder.scanstring, b"xxx", 1 == \
                        "xxx")
    pytest.raises(UnicodeDecodeError,
                        dson.encoder.encode_basestring_ascii, b"xx\xff")

def test_overflow():
    with pytest.raises(OverflowError):
        dson.decoder.scanstring(b"xxx",  sys.maxsize+1)
