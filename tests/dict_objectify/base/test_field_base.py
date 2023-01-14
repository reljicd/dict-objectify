import pytest

from dict_objectify.base.constants import NONE_EQUIVALENT_VALUES
from tests.dict_objectify.fixture_models import TestModel

_STANDARD_TYPES_VALUES = [
    'Hello', 0, 1, True, {'A'}, {'a': 1}, [0], False
]


@pytest.fixture()
def model():
    return TestModel()


@pytest.mark.parametrize('standard_type_value', _STANDARD_TYPES_VALUES)
def test_field_base_with_standard_types_values(model, standard_type_value):
    model.base_field = standard_type_value
    with pytest.raises(ValueError, match=r".* unsupported \[type: .*"):
        _ = model.base_field


@pytest.mark.parametrize('standard_type_value', _STANDARD_TYPES_VALUES)
def test_nullable_field_base_with_standard_types_values(model,
                                                        standard_type_value):
    model.base_field_nullable = standard_type_value
    with pytest.raises(ValueError, match=r".* unsupported \[type: .*"):
        _ = model.base_field_nullable


@pytest.mark.parametrize('none_equivalent_value', NONE_EQUIVALENT_VALUES)
def test_field_base_with_null_values(model, none_equivalent_value):
    with pytest.raises(ValueError, match=r".* is not nullable. .*"):
        model.base_field = none_equivalent_value


@pytest.mark.parametrize('none_equivalent_value', NONE_EQUIVALENT_VALUES)
def test_nullable_field_base_with_null_values(model, none_equivalent_value):
    model.base_field_nullable = none_equivalent_value
    assert model.base_field_nullable in NONE_EQUIVALENT_VALUES
