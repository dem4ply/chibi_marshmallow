import datetime
from marshmallow import fields
from marshmallow.utils import missing as missing_
from marshmallow.experimental.context import Context as Marsh_context


class String_lower( fields.String ):
    """
    Este campo siempre regresa en minuscalas la cadena
    """

    def _deserialize( self, value, attr, data, **kw ):
        value = super()._deserialize( value, attr, data, **kw )
        return value.lower()


class Timestamp( fields.Field ):
    """
    transforma un timestamp a datetime
    """

    def _deserialize( self, value, attr, data, **kw ):
        return datetime.datetime.fromtimestamp( float( value ) )


class Context( fields.Field ):
    """
    regresa el valor del context siendo el nombre del field la key a buscar
    en el contexto
    """

    def __init__( self, key=None, load_default=None, **kw ):
        super().__init__( **kw )
        self._key = key

    def deserialize( self, value, attr, data, **kw, ):
        """
        Deserialize el value.

        Parameters
        ----------
        value: any
            si es algo entonces no se usara el context
        attr: str
            attribute or key en el objeto a deserializar
        data: obj
            objeto que se mando al load
        kw: dict
            otros parametros que se mandaron al field
        """
        # Validate required fields, deserialize, then validate
        # deserialized value
        self._validate_missing(value)
        if value is missing_:
            try:
                return Marsh_context.get()[ self._key or attr ]
            except LookupError as e:
                raise LookupError(
                    "no se encontro el contexto para el serializador" ) from e
        output = self._deserialize( value, attr, data, **kw )
        self._validate(output)
        return output
