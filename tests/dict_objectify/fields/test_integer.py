import pytest

from dict_objectify.fixture_models import TestModel

INTEGER_LEGAL = [-2 ** 65, -100, -1, 0, 1, 100, 2 ** 65]


@pytest.mark.parametrize('legal_value',
                         [*INTEGER_LEGAL,
                          *[str(i) for i in INTEGER_LEGAL],
                          *[float(i + 0.1) for i in INTEGER_LEGAL]])
def test_integer_field_with_legal_values(legal_value):
    model = TestModel()

    model.integer_field = legal_value
    assert model.integer_field == int(legal_value)

    model.integer_field_nullable = legal_value
    assert model.integer_field_nullable == int(legal_value)
