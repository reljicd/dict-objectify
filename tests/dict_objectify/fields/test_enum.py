import pytest

from tests.dict_objectify.fixture_models import TestModel

ENUM_LEGAL = [
    'a', 'b', 'c',
]
ENUM_ILLEGAL = [
    'Some value', 0, False, 0.0
]


@pytest.fixture()
def model():
    return TestModel()


@pytest.mark.parametrize('legal_value', ENUM_LEGAL)
def test_enum_field_with_legal_values(model, legal_value):
    model.enum_field = legal_value
    assert model.enum_field == legal_value


@pytest.mark.parametrize('legal_value', ENUM_LEGAL)
def test_nullable_enum_field_with_legal_values(model, legal_value):
    model.enum_field_nullable = legal_value
    assert model.enum_field_nullable == legal_value


@pytest.mark.parametrize('illegal_value', ENUM_ILLEGAL)
def test_enum_field_with_illegal_values(model, illegal_value):
    with pytest.raises(ValueError):
        model.enum_field = illegal_value

    with pytest.raises(AttributeError, match=r"Missing dict key .*"):
        _ = model.enum_field
    assert 'enum_field' not in model.data_dict


@pytest.mark.parametrize('illegal_value', ENUM_ILLEGAL)
def test_nullable_enum_field_with_illegal_values(model, illegal_value):
    with pytest.raises(ValueError):
        model.enum_field_nullable = illegal_value

    with pytest.raises(AttributeError, match=r"Missing dict key .*"):
        _ = model.enum_field_nullable
    assert 'enum_field_nullable' not in model.data_dict
