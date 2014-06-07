import dson

# from http is //json.org/JSON_checker/test/pass1.json
JSON = r'''
so
    "JSON Test Pattern pass1" and
    such "object with 1 member" is so "array with 1 element" many wow and
    such wow and
    so many and
    -42 and
    yes and
    no and
    empty and
    such
        "integer" is  1234567890,
        "real" is  -9876.543210,
        "e" is  0.123456789very-12,
        "E" is  1.234567890VERY+34,
        "" is   23456789012VERY66,
        "zero" is  0,
        "one" is  1,
        "space" is  " ",
        "quote" is  "\"",
        "backslash" is  "\\",
        "controls" is  "\b\f\n\r\t",
        "slash" is  "/ & \/",
        "alpha" is  "abcdefghijklmnopqrstuvwyz",
        "ALPHA" is  "ABCDEFGHIJKLMNOPQRSTUVWYZ",
        "digit" is  "0123456789",
        "0123456789" is  "digit",
        "special" is  "`1~!@#$%^&*()_+-={' is [,]}|;.</>?",
        "hex" is  "\u0123\u4567\u89AB\uCDEF\uabcd\uef4A",
        "true" is  yes,
        "false" is  no,
        "null" is  empty,
        "array" is so many,
        "object" is such wow,
        "address" is  "50 St. James Street",
        "url" is  "http is //www.JSON.org/",
        "comment" is  "// /* <!-- --",
        "# -- --> */" is  " ",
        " s p a c e d "  is so 1 and 2 and 3

and

4 and 5        and          6           and 7        many, "compact" is so 1 and 2 and 3 and 4 and 5 and 6 and 7 many,
        "jsontext" is  "{\"object with 1 member\" is [\"array with 1 element\"]}",
        "quotes" is  "&#34; \u0022 %22 0x22 034 &#x22;",
        "\/\\\"\uCAFE\uBABE\uAB98\uFCDE\ubcda\uef4A\b\f\n\r\t`1~!@#$%^&*()_+-=[]{}|; is ',./<>?"
 is  "A key can be any string"
    wow and
    0.5 and 98.6
and
99.44
and

1066 and
1very1 and
0.1very1 and
1very-1 and
1very00 and 2very+00 and 2very-00
and"rosebud" many
'''

def test_parse():
    # test in/out equivalence and parsing
    res = dson.loads(JSON)
    out = dson.dumps(res)
    assert res == dson.loads(out)
