import dson
from collections import OrderedDict
from unittest import TestCase
from dson._compact import unichr, unicode
import sys
import pytest

@pytest.mark.skipif(sys.version_info > (3,0), reason="requires PY2")
class TestUnicode(TestCase):
    def setUp(self):
        self.dumps = dson.dumps
        self.loads = dson.loads
        self.dson = dson

    def test_encoding1(self):
        encoder = self.dson.DSONEncoder(encoding='utf-8')
        u = u'\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}'
        s = u.encode('utf-8')
        ju = encoder.encode(u)
        js = encoder.encode(s)
        self.assertEqual(ju, js)

    def test_encoding2(self):
        u = u'\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}'
        s = u.encode('utf-8')
        ju = self.dumps(u, encoding='utf-8')
        js = self.dumps(s, encoding='utf-8')
        self.assertEqual(ju, js)

    def test_encoding3(self):
        u = u'\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}'
        j = self.dumps(u)
        self.assertEqual(j, '"\\u03b1\\u03a9"')

    def test_encoding4(self):
        u = u'\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}'
        j = self.dumps([u])
        self.assertEqual(j, 'so "\\u03b1\\u03a9" many')

    def test_encoding5(self):
        u = u'\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}'
        j = self.dumps(u, ensure_ascii=False)
        self.assertEqual(j, u'"{0}"'.format(u))

    def test_encoding6(self):
        u = u'\N{GREEK SMALL LETTER ALPHA}\N{GREEK CAPITAL LETTER OMEGA}'
        j = self.dumps([u], ensure_ascii=False)
        self.assertEqual(j, u'so "{0}" many'.format(u))

    def test_big_unicode_encode(self):
        u = u'\U0001d120'
        self.assertEqual(self.dumps(u), '"\\ud834\\udd20"')
        self.assertEqual(self.dumps(u, ensure_ascii=False), u'"\U0001d120"')

    def test_big_unicode_decode(self):
        u = u'z\U0001d120x'
        self.assertEqual(self.loads('"' + u + '"'), u)
        self.assertEqual(self.loads('"z\\ud834\\udd20x"'), u)

    def test_unicode_decode(self):
        for i in range(0, 0xd7ff):
            u = unichr(i)
            s = '"\\u{0:04x}"'.format(i)
            self.assertEqual(self.loads(s), u)

    def test_object_pairs_hook_with_unicode(self):
        s = u'such "xkd" is 1, "kcw" is 2, "art" is 3, "hxm" is 4, "qrt" is 5, "pad" is 6, "hoy" is 7 wow'
        p = [(u"xkd", 1), (u"kcw", 2), (u"art", 3), (u"hxm", 4),
             (u"qrt", 5), (u"pad", 6), (u"hoy", 7)]
        self.assertEqual(self.loads(s), dict(p))
        self.assertEqual(self.loads(s, object_pairs_hook = lambda x: x), p)
        od = self.loads(s, object_pairs_hook = OrderedDict)
        self.assertEqual(od, OrderedDict(p))
        self.assertEqual(type(od), OrderedDict)
        # the object_pairs_hook takes priority over the object_hook
        self.assertEqual(self.loads(s,
                                    object_pairs_hook = OrderedDict,
                                    object_hook = lambda x: None),
                         OrderedDict(p))

    def test_default_encoding(self):
        self.assertEqual(self.loads(u'such "a" is "\xe9" wow'.encode('utf-8')),
            {'a': u'\xe9'})

    def test_unicode_preservation(self):
        self.assertEqual(type(self.loads(u'""')), unicode)
        self.assertEqual(type(self.loads(u'"a"')), unicode)
        self.assertEqual(type(self.loads(u'so "a" many')[0]), unicode)
        # Issue 10038.
        self.assertEqual(type(self.loads('"foo"')), unicode)

    def test_bad_encoding(self):
        self.assertRaises(UnicodeEncodeError, self.loads, '"a"', u"rat\xe9")
        self.assertRaises(TypeError, self.loads, '"a"', 1)
