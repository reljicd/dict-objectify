import pytest

from dict_objectify.fields.test_float import FLOAT_LEGAL
from dict_objectify.fields.test_integer import INTEGER_LEGAL
from dict_objectify.fixture_models import TestModel

TEXT_LEGAL = ['', 'a', 'Some value']

LEGAL_VALUES = [*TEXT_LEGAL,
                *[str(i) for i in INTEGER_LEGAL],
                *[str(i) for i in FLOAT_LEGAL]]


@pytest.fixture()
def model():
    return TestModel()


@pytest.mark.parametrize('legal_value', LEGAL_VALUES)
def test_text_field_with_legal_values(model, legal_value):
    model.text_field = legal_value
    assert model.text_field == legal_value


@pytest.mark.parametrize('legal_value', LEGAL_VALUES)
def test_nullable_text_field_with_legal_values(model, legal_value):
    model.text_field_nullable = legal_value
    assert model.text_field_nullable == legal_value
