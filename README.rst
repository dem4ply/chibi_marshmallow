=================
chibi_marshmallow
=================


.. image:: https://img.shields.io/pypi/v/chibi_marshmallow.svg
        :target: https://pypi.python.org/pypi/chibi_marshmallow

.. image:: https://img.shields.io/travis/dem4ply/chibi_marshmallow.svg
        :target: https://travis-ci.org/dem4ply/chibi_marshmallow

.. image:: https://readthedocs.org/projects/chibi-marshmallow/badge/?version=latest
        :target: https://chibi-marshmallow.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


fields and snippets for marshmallow


* Free software: WTFPL
* Documentation: https://chibi-marshmallow.readthedocs.io.


Features
--------

* campo de String_lower
	convierto los string a minusculas
* campo de Timestamp
	convierte los integers de timestamp a datetime
* campo de Context
	usa los valores que se manden al context de marshmallow

example
-------

.. code-block:: python

	from chibi_marshmallow import fields
	from marshmallow.experimental.context import Context

	class Example( Schema ):
		string_lower = fields.String_lower()
		timestamp = fields.Timestamp()
		context = fields.Context()

	with Context( { "context": "hello" } )
		result = Example().load( {
			'string_lower': 'SoMe_StRiNg',
			'timestamp': '631173600',
		} )
	assert result[ "string_lower" ] == "some_string"
	assert result[ "timestamp" ] == datetime.datetime( 1990, 1, 1 )
	assert result[ "context" ] == "hello"

