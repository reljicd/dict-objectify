import pytest

from dict_objectify.fields.test_float import FLOAT_LEGAL
from dict_objectify.fields.test_integer import INTEGER_LEGAL
from dict_objectify.fixture_models import TestModel

TEXT_LEGAL = ['', 'a', 'Some value']


@pytest.mark.parametrize('legal_value',
                         [*TEXT_LEGAL,
                          *[str(i) for i in INTEGER_LEGAL],
                          *[str(i) for i in FLOAT_LEGAL]])
def test_text_field_with_legal_values(legal_value):
    model = TestModel()

    model.text_field = legal_value
    assert model.text_field == legal_value

    model.text_field_nullable = legal_value
    assert model.text_field_nullable == legal_value
