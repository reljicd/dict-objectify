from dict_objectify.base.base import Base
from dict_objectify.base.field_base import FieldBase
from dict_objectify.fields.array import Array
from dict_objectify.fields.bool import Bool
from dict_objectify.fields.date import Datetime
from dict_objectify.fields.enum import EnumField
from dict_objectify.fields.float import Float
from dict_objectify.fields.integer import Integer
from dict_objectify.fields.text import Text


class NestedTestModel(Base):
    text_field = Text(nullable=False)
    text_field_nullable = Text()


class TestModel(Base):
    base_field = FieldBase(nullable=False)
    text_field = Text(nullable=False)
    integer_field = Integer(nullable=False)
    datetime_field = Datetime(nullable=False)
    float_field = Float(nullable=False)
    bool_field = Bool(nullable=False)
    string_array_field = Array(str, nullable=False)
    nested_array_field = Array(NestedTestModel, nullable=False)
    enum_field = EnumField(['a', 'b', 'c'], nullable=False)
    nested_field = NestedTestModel(nullable=False)

    base_field_nullable = FieldBase()
    text_field_nullable = Text()
    integer_field_nullable = Integer()
    datetime_field_nullable = Datetime()
    float_field_nullable = Float()
    bool_field_nullable = Bool()
    string_array_field_nullable = Array(str)
    nested_array_field_nullable = Array(NestedTestModel)
    enum_field_nullable = EnumField(['a', 'b', 'c'])
    nested_field_nullable = NestedTestModel()

    enum_field_nullable_not_strict = EnumField(['a', 'b', 'c'], strict=False)
