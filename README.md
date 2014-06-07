dogeon
======

DSON encoder/decoder for Python

![Doge](http://dogeon.org/doge.gif)


### What is Dogeon?

Dogeon is a simple, fast, complete, correct and extensible DSON <http://dogeon.org>
encoder and decoder for Python 2.5+ and Python 3.3+.
It is pure Python code with no dependencies.

The encoder can be specialized to provide serialization in any kind of situation,
without any special support by the objects to be serialized (somewhat like pickle).
This is best done with the default kwarg to dumps.

The decoder can handle incoming DSON strings of any specified encoding
(UTF-8 by default). It can also be specialized to post-process DSON objects with
the object_hook or object_pairs_hook kwargs.

### How to use `Dogeon`?

It has completely the same API with standard `json` library.


    In [1]: import dson

    In [2]: dson.loads('such "foo" is "bar". "doge" is "shibe" wow')
    Out[2]: {u'doge': u'shibe', u'foo': u'bar'}

    In [3]: dson.dumps({"foo": "bar", "doge": "shibe"})
    Out[3]: 'such "doge" is "shibe", "foo" is "bar" wow'


### How to contribute?

Running tests:

    py.test tests

### Note

Since DSON allow `,.!?` as member separators, `Dogeon` default use `,` as member
seperator when dumps.
Since DSON allow `and`, `also` as object element separators, `Dogeon` default use
`and` as element separators.
