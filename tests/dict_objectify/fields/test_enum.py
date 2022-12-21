import pytest

from dict_objectify.fixture_models import TestModel

ENUM_LEGAL = [
    'a', 'b', 'c',
]
ENUM_ILLEGAL = [
    'Some value', 0, False, 0.0
]


@pytest.mark.parametrize('legal_value', ENUM_LEGAL)
def test_enum_field_with_legal_values(legal_value):
    model = TestModel()

    model.enum_field = legal_value
    assert model.enum_field == legal_value

    model.enum_field_nullable = legal_value
    assert model.enum_field_nullable == legal_value


@pytest.mark.parametrize('illegal_value', ENUM_ILLEGAL)
def test_enum_field_with_illegal_values(illegal_value):
    model = TestModel()

    with pytest.raises(ValueError):
        model.enum_field = illegal_value

    with pytest.raises(ValueError):
        model.enum_field_nullable = illegal_value

    assert model.enum_field_nullable is None
    assert 'enum_field_nullable' not in model.data_dict
