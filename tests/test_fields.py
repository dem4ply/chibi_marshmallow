import datetime
import unittest

from chibi_marshmallow import fields
from marshmallow import Schema
from marshmallow.experimental.context import Context


class Schema_lower_test( Schema ):
    test = fields.String_lower()


class Schema_timestamp_test( Schema ):
    test = fields.Timestamp()


class Schema_context_test( Schema ):
    test = fields.Context()


class Schema_context_test_2( Schema ):
    test = fields.Context( "other" )


class Test_string_lower( unittest.TestCase ):
    def test_should_return_the_lower_value( self ):
        result = Schema_lower_test().load( { 'test': 'ASDFGHJKL' } )
        self.assertEqual( result[ 'test' ], 'asdfghjkl' )


class Test_timestamp( unittest.TestCase ):
    def test_when_is_string_should_return_the_datetime( self ):
        expected = datetime.datetime( 1990, 1, 1 )
        result = Schema_timestamp_test().load( { 'test': '631173600' } )
        self.assertEqual( result[ 'test' ], expected )

    def test_when_is_int_should_return_the_dateime( self ):
        expected = datetime.datetime( 1990, 1, 1 )
        result = Schema_timestamp_test().load( { 'test': 631173600 } )
        self.assertEqual( result[ 'test' ], expected )


class Test_context( unittest.TestCase ):
    def test_default_key_context_should_work( self ):
        expected = "Hello my little context!!!"
        with Context( { "test": expected } ):
            result = Schema_context_test().load( {} )
        self.assertEqual( result[ 'test' ], expected )

    def test_no_default_key_context_should_work( self ):
        expected = "Hello my little context!!!"
        with Context( { "other": expected } ):
            result = Schema_context_test_2().load( {} )
        self.assertEqual( result[ 'test' ], expected )
