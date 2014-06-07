# -*- coding: utf-8 -*-

import sys
import struct

PY2 = sys.version_info[0] == 2

_BYTES = '7FF80000000000007FF0000000000000'
def _floatconstants():
    if PY2:
        _bytes = _BYTES.decode('hex')
    else:
        import codecs
        _bytes = codecs.decode(_BYTES, 'hex_codec')
    if sys.byteorder != 'big':
        _bytes = _bytes[:8][::-1] + _bytes[8:][::-1]
    nan, inf = struct.unpack('dd', _bytes)
    return nan, inf, -inf

NaN, PosInf, NegInf = _floatconstants()

    # 'unicode' is undefined, must be Python 3
if PY2:
    str = str
    unicode = unicode
    bytes = str
    basestring = basestring
    long = long
    iteritems = lambda x: x.iteritems()
else:
    str = str
    unicode = str
    bytes = bytes
    basestring = (str,bytes)
    long = int
    iteritems = lambda x: iter(x.items())
