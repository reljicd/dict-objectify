import pytest
from str2bool import str2bool

from dict_objectify.fixture_models import TestModel

BOOL_LEGAL = ['True', 'False', True, False]


@pytest.mark.parametrize('legal_value', BOOL_LEGAL)
def test_bool_field_with_legal_values(legal_value):
    model = TestModel()

    model.bool_field = legal_value
    if isinstance(legal_value, str):
        assert model.bool_field == str2bool(legal_value)
    else:
        assert model.bool_field == legal_value

    model.bool_field_nullable = legal_value
    if isinstance(legal_value, str):
        assert model.bool_field_nullable == str2bool(legal_value)
    else:
        assert model.bool_field_nullable == legal_value
