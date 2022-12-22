import pytest

from dict_objectify.fixture_models import TestModel

INTEGER_LEGAL = [-2 ** 65, -100, -1, 0, 1, 100, 2 ** 65]

LEGAL_VALUES = [*INTEGER_LEGAL,
                *[str(i) for i in INTEGER_LEGAL],
                *[float(i + 0.1) for i in INTEGER_LEGAL]]


@pytest.fixture()
def model():
    return TestModel()


@pytest.mark.parametrize('legal_value', LEGAL_VALUES)
def test_integer_field_with_legal_values(model, legal_value):
    model.integer_field = legal_value
    assert model.integer_field == int(legal_value)


@pytest.mark.parametrize('legal_value', LEGAL_VALUES)
def test_nullable_integer_field_with_legal_values(model, legal_value):
    model.integer_field_nullable = legal_value
    assert model.integer_field_nullable == int(legal_value)
