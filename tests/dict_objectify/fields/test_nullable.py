import pytest

from dict_objectify.base.hash import NONE_EQUIVALENT_VALUES
from tests.dict_objectify.fixture_models import TestModel


@pytest.fixture()
def model():
    return TestModel()


@pytest.mark.parametrize('none_equivalent_value',
                         NONE_EQUIVALENT_VALUES)
def test_non_nullable_fields(model, none_equivalent_value):
    non_nullable_fields = ['base_field', 'text_field', 'integer_field',
                           'datetime_field', 'float_field', 'bool_field',
                           'enum_field', 'nested_field', 'string_array_field',
                           'nested_array_field']

    for non_nullable_field in non_nullable_fields:
        with pytest.raises(AttributeError, match=r"Missing dict key .*"):
            _ = getattr(model, non_nullable_field)

        with pytest.raises(ValueError):
            setattr(model, non_nullable_field, none_equivalent_value)


@pytest.mark.parametrize('none_equivalent_value',
                         NONE_EQUIVALENT_VALUES)
def test_nullable_fields(model, none_equivalent_value):
    nullable_fields = ['base_field_nullable', 'text_field_nullable',
                       'integer_field_nullable', 'datetime_field_nullable',
                       'float_field_nullable', 'bool_field_nullable',
                       'string_array_field_nullable',
                       'nested_array_field_nullable', 'enum_field_nullable',
                       'nested_field_nullable']

    for nullable_field in nullable_fields:
        with pytest.raises(AttributeError, match=r"Missing dict key .*"):
            _ = getattr(model, nullable_field)

        setattr(model, nullable_field, none_equivalent_value)

        assert getattr(model, nullable_field) in NONE_EQUIVALENT_VALUES
