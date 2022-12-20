from dict_objectify.base import Base
from dict_objectify.fields.array import Array
from dict_objectify.fields.data_fields import (Bool, Datetime, Float, Integer,
                                               Text)
from dict_objectify.fields.enum import EnumField
from dict_objectify.fields.field_base import FieldBase


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
