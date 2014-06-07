dogeon
======

DSON encoder/decoder for Python


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

### How to contribute?

* Test

    py.test tests
