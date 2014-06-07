import dson

# from http://json.org/JSON_checker/test/pass3.json
JSON = r'''
such
    "JSON Test Pattern pass3" is such
        "The outermost value" is "must be an object or array.",
        "In this test" is "It is an object."
    wow
wow
'''


def test_parse():
    # test in/out equivalence and parsing
    res = dson.loads(JSON)
    out = dson.dumps(res)
    assert res == dson.loads(out)
