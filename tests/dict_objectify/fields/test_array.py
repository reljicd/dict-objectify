from datetime import datetime

import pytest

from dict_objectify.fixture_models import NestedTestModel, TestModel

LEGAL_STRING_VALUES = [
    ['Hello'],
    [0, 1, 2], ['1', 2, 3.0],
    {'Hello'}, {0, 1, 2}, {'1', 2, 3.0}
]
ILLEGAL_STRING_VALUES = [
    {'hello': 'there'}, datetime(2020, 1, 1), 0, 'hello there!'
]


@pytest.mark.parametrize('legal_value', LEGAL_STRING_VALUES)
def test_str_array_field_with_legal_values(legal_value):
    model = TestModel()

    model.string_array_field = legal_value
    assert model.string_array_field == [str(el) for el in legal_value]

    model.string_array_field_nullable = legal_value
    assert model.string_array_field_nullable == [str(el) for el in legal_value]


@pytest.mark.parametrize('illegal_value', ILLEGAL_STRING_VALUES)
def test_str_array_field_with_illegal_values(illegal_value):
    model = TestModel()

    with pytest.raises(ValueError, match=r".* unsupported \[type: .*"):
        model.string_array_field = illegal_value

    assert model.string_array_field == []
    assert 'string_array_field' not in model.data_dict

    with pytest.raises(ValueError, match=r".* unsupported \[type: .*"):
        model.string_array_field_nullable = illegal_value

    assert model.string_array_field_nullable == []
    assert 'string_array_field_nullable' not in model.data_dict


LEGAL_OBJ_VALUES = [
    {'text_field': 'Something', 'text_field_nullable': 'Something else'},
    {'text_field': '', 'text_field_nullable': None},
    {'text_field': 'Something', 'text_field_nullable': []},
    {'text_field': 'Something'},
]


@pytest.mark.parametrize('legal_value', LEGAL_OBJ_VALUES)
def test_obj_array_field_with_legal_values(legal_value):
    model = TestModel()
    nested_model = NestedTestModel(data_dict=legal_value)

    model.nested_array_field = [nested_model]
    assert model.nested_array_field[0] == nested_model

    model.nested_array_field_nullable = [nested_model]
    assert model.nested_array_field_nullable[0] == nested_model
