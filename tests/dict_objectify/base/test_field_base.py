import pytest

from dict_objectify.base.constants import NONE_EQUIVALENT_VALUES
from dict_objectify.fixture_models import TestModel

_STANDARD_TYPES_VALUES = [
    'Hello', 0, 1, True, {'A'}, {'a': 1}, [0], False
]


@pytest.mark.parametrize('standard_type_value', _STANDARD_TYPES_VALUES)
def test_field_base_with_standard_types_values(standard_type_value):
    model = TestModel()

    model.base_field = standard_type_value
    with pytest.raises(ValueError, match=r".* unsupported \[type: .*"):
        _ = model.base_field

    model.base_field_nullable = standard_type_value
    with pytest.raises(ValueError, match=r".* unsupported \[type: .*"):
        _ = model.base_field_nullable


@pytest.mark.parametrize('none_equivalent_value', NONE_EQUIVALENT_VALUES)
def test_field_base_with_illegal_values(none_equivalent_value):
    model = TestModel()

    with pytest.raises(ValueError, match=r".* is not nullable. .*"):
        model.base_field = none_equivalent_value

    model.base_field_nullable = none_equivalent_value
    assert 'base_field_nullable' not in model.data_dict
    assert model.base_field_nullable is None
