import math

import pytest

from dict_objectify.fields.test_integer import INTEGER_LEGAL
from dict_objectify.fixture_models import TestModel

FLOAT_LEGAL = [-math.inf, -float('inf'), -2. ** 65, -100., -1.,
               0.,
               1., 100., 2. ** 65, float('inf'), math.inf,
               -(1 / 3), (1 / 3), math.pi, (1 / 3) ** math.pi, 1.2]

LEGAL_VALUES = [*INTEGER_LEGAL,
                *[str(i) for i in INTEGER_LEGAL],
                *[float(i + 0.1) for i in INTEGER_LEGAL],
                *FLOAT_LEGAL,
                *[str(i) for i in FLOAT_LEGAL]]


@pytest.fixture()
def model():
    return TestModel()


@pytest.mark.parametrize('legal_value', LEGAL_VALUES)
def test_float_field_with_legal_values(model, legal_value):
    model.float_field = legal_value
    assert model.float_field == float(legal_value)


@pytest.mark.parametrize('legal_value', LEGAL_VALUES)
def test_nullable_float_field_with_legal_values(model, legal_value):
    model.float_field_nullable = legal_value
    assert model.float_field_nullable == float(legal_value)
