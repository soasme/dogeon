import dson

# from http://json.org/JSON_checker/test/pass2.json
JSON = r'''
so so so so so so so so so so so so so so so so so so so "Not too deep" many many many many many many many many many many many many many many many many many many many
'''

def test_parse():
    # test in/out equivalence and parsing
    res = dson.loads(JSON)
    out = dson.dumps(res)
    assert res == dson.loads(out)
