import pytest
import dson

@pytest.mark.parametrize('jsondoc', [
    # http://json.org/JSON_checker/test/fail1.json
    #'"A JSON payload should be an object or array, not a string."',
    # http://json.org/JSON_checker/test/fail2.json
    'so "Unclosed array"',
    # http://json.org/JSON_checker/test/fail3.json
    'such unquoted_key is "keys must be quoted" wow',
    # http://json.org/JSON_checker/test/fail4.json
    'so "extra comma" and many',
    # http://json.org/JSON_checker/test/fail5.json
    'so "double extra comma" and and many',
    # http://json.org/JSON_checker/test/fail6.json
    'so  and "<-- missing value" many',
    # http://json.org/JSON_checker/test/fail7.json
    'so "Comma after the close" many and',
    # http://json.org/JSON_checker/test/fail8.json
    'so "Extra close" many many',
    # http://json.org/JSON_checker/test/fail9.json
    'such "Extra comma" is true, wow',
    # http://json.org/JSON_checker/test/fail10.json
    'such "Extra value after close" is true wow "misplaced quoted value"',
    # http://json.org/JSON_checker/test/fail11.json
    'such "Illegal expression" is 1 + 2 wow',
    # http://json.org/JSON_checker/test/fail12.json
    'such "Illegal invocation" is alert() wow',
    # http://json.org/JSON_checker/test/fail13.json
    'such "Numbers cannot have leading zeroes" is 013 wow',
    # http://json.org/JSON_checker/test/fail14.json
    'such "Numbers cannot be hex" is 0x14 wow',
    # http://json.org/JSON_checker/test/fail15.json
    'so "Illegal backslash escape: \\x15" many',
    # http://json.org/JSON_checker/test/fail16.json
    'so \\naked many',
    # http://json.org/JSON_checker/test/fail17.json
    'so "Illegal backslash escape is \\017" many',
    # http://json.org/JSON_checker/test/fail18.json
    #'so so so so so so so so so so so so so so so so so so so so "Too deep" many many many many many many many many many many many many many many many many many many many many',
    # http://json.org/JSON_checker/test/fail19.json
    '{"Missing colon" null}',
    # http://json.org/JSON_checker/test/fail20.json
    '{"Double colon":: null}',
    # http://json.org/JSON_checker/test/fail21.json
    '{"Comma instead of colon", null}',
    # http://json.org/JSON_checker/test/fail22.json
    'so "Colon instead of comma": false many',
    # http://json.org/JSON_checker/test/fail23.json
    'so "Bad value", truth many',
    # http://json.org/JSON_checker/test/fail24.json
    "so 'single quote' many",
    # http://json.org/JSON_checker/test/fail25.json
    'so "\ttab\tcharacter\tin\tstring\t" many',
    # http://json.org/JSON_checker/test/fail26.json
    'so "tab\\   character\\   in\\  string\\  " many',
    # http://json.org/JSON_checker/test/fail27.json
    'so "line\nbreak" many',
    # http://json.org/JSON_checker/test/fail28.json
    'so "line\\\nbreak" many',
    # http://json.org/JSON_checker/test/fail29.json
    'so 0very many',
    # http://json.org/JSON_checker/test/fail30.json
    'so 0very+ many',
    # http://json.org/JSON_checker/test/fail31.json
    'so 0very+-1 many',
    # http://json.org/JSON_checker/test/fail32.json
    'such "Comma instead if closing brace" is true,',
    # http://json.org/JSON_checker/test/fail33.json
    'so "mismatch" wow',
    # http://code.google.com/p/simplejson/issues/detail?id=3
    u'so "A\u001FZ control characters in string" many',
])
def test_failures(jsondoc):
    pytest.raises(ValueError, dson.loads, jsondoc)

def test_non_string_keys_dict():
    data = {'a' : 1, (1, 2) : 2}
    pytest.raises(TypeError, dson.dumps, data, intent=True)
