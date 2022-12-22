from datetime import datetime

import pytest

from dict_objectify.fixture_models import TestModel

DATETIME_LEGAL = [datetime(2000, 1, 1, 0, 0, 0, 0),
                  datetime(1, 1, 1),
                  '2020-01-01',
                  '2020-01-01T00:00:00Z']


@pytest.fixture()
def model():
    return TestModel()


@pytest.mark.parametrize('legal_value', DATETIME_LEGAL)
def test_datetime_field_with_legal_values(model, legal_value):
    model.datetime_field = legal_value
    if isinstance(legal_value, datetime):
        assert model.datetime_field == legal_value


@pytest.mark.parametrize('legal_value', DATETIME_LEGAL)
def test_nullable_datetime_field_with_legal_values(model, legal_value):
    model.datetime_field_nullable = legal_value
    if isinstance(legal_value, datetime):
        assert model.datetime_field_nullable == legal_value
