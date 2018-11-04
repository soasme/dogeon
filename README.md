dogeon
======

DSON encoder/decoder for Python

![PYPI](http://img.shields.io/pypi/v/Dogeon.svg)
![Build status](http://img.shields.io/travis/soasme/dogeon.svg)
![Download](http://img.shields.io/pypi/dm/Dogeon.svg)

![Doge](http://dogeon.org/doge.gif)


### What is Dogeon?

`Dogeon` is a simple, fast, complete, correct and extensible DSON <https://dogeon.xyz/>
encoder and decoder for Python.  It is pure Python code with no dependencies.

The encoder can be specialized to provide serialization in any kind of situation,
without any special support by the objects to be serialized (somewhat like pickle).
This is best done with the `default` kwarg to the `dson.dumps()` function.

The decoder can handle incoming DSON strings of any specified encoding
(UTF-8 by default). It can also be specialized to post-process DSON objects with
the `object_hook` or `object_pairs_hook` kwargs.

`Dogeon` Support:

* Python 2.7
* Python 3.3
* Python 3.4
* PyPy

### How to install `Dogeon`?

    $ pip install Dogeon

### How to use `Dogeon`?

It uses the exact same API as the standard `json` library.

```python
In [1]: import dson

In [2]: dson.loads('such "foo" is "bar". "doge" is "shibe" wow')
Out[2]: {u'doge': u'shibe', u'foo': u'bar'}

In [3]: dson.dumps({"foo": "bar", "doge": "shibe"})
Out[3]: 'such "doge" is "shibe", "foo" is "bar" wow'
```

### How to contribute?

Running tests:

    py.test tests

### Note

While DSON allows `,.!?` as member separators, `Dogeon` by default uses `,` as
a member seperator for dumps.

Also, while DSON allows `and`, `also` as object element separators, `Dogeon` by
default uses `and` as an element separator.
