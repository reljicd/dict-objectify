import pytest
from str2bool import str2bool

from tests.dict_objectify.fixture_models import TestModel

BOOL_LEGAL = ['True', 'False', True, False]


@pytest.fixture()
def model():
    return TestModel()


@pytest.mark.parametrize('legal_value', BOOL_LEGAL)
def test_bool_field_with_legal_values(model, legal_value):
    model.bool_field = legal_value
    if isinstance(legal_value, str):
        assert model.bool_field == str2bool(legal_value)
    else:
        assert model.bool_field == legal_value


@pytest.mark.parametrize('legal_value', BOOL_LEGAL)
def test_nullable_bool_field_with_legal_values(model, legal_value):
    model.bool_field_nullable = legal_value
    if isinstance(legal_value, str):
        assert model.bool_field_nullable == str2bool(legal_value)
    else:
        assert model.bool_field_nullable == legal_value
