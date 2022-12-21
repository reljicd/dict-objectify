from typing import Any

import pytest

from dict_objectify.base.base import Base
from dict_objectify.base.constants import NONE_EQUIVALENT_VALUES
from dict_objectify.hash import __int_hash, dict_base_hash

RESEARCHER_DICT_VER_1 = {'first_name': 'Test',
                         'identifiers': [
                             {"name": "fris",
                              "value": "94275885-8345-461e-8507-f866c968ebd5"},
                             {"name": "fris",
                              "value": "ed9226cc-7cb2-40f8-95f6-1b0d39695900"}],
                         'country': {'name': 'belgium',
                                     'code': 'be'},
                         'keywords': ['keyword_1', 'keyword_2'],
                         'experiences': [
                             {'title': 'Title',
                              'organisation': {'name': 'Name',
                                               'country': {'code': 'be',
                                                           'name': 'belgium'}}}]
                         }

RESEARCHER_DICT_VER_2 = {'first_name': 'Test',
                         'experiences': [
                             {'organisation': {'country': {'code': 'be',
                                                           'name': 'belgium'},
                                               'name': 'Name'},
                              'title': 'Title'}],
                         'keywords': ['keyword_2', 'keyword_1'],
                         'country': {'code': 'be',
                                     'name': 'belgium'},
                         'identifiers': [
                             {"name": "fris",
                              "value": "ed9226cc-7cb2-40f8-95f6-1b0d39695900"},
                             {"name": "fris",
                              "value": "94275885-8345-461e-8507-f866c968ebd5"}]}

RESEARCHER_DICT_VER_3 = {'first_name': 'Test',
                         'created_at': '2019-03-16T13:33:17Z',
                         'updated_at': '2019-03-17T15:11:21Z',
                         'experiences': [],
                         'keywords': ['keyword_2', 'keyword_1'],
                         'country': {'code': 'be',
                                     'name': 'belgium'},
                         'identifiers': [
                             {"name": "orcid",
                              "value": "94275885-8345-461e-8507"}]}


@pytest.mark.parametrize('value,length,expected_hash',
                         [('test_1',
                           20,
                           45036590271683491959),
                          ('test_2',
                           20,
                           17739181516819817863)])
def test_int_hash(value: str, length: int, expected_hash: int):
    calculated_hash = __int_hash(value)
    assert expected_hash == calculated_hash
    assert len(str(calculated_hash)) == length


@pytest.mark.parametrize('value_1,value_2',
                         [('100',
                           100),
                          ('True',
                           True),
                          (['1', 'True'],
                           [True, 1]),
                          (RESEARCHER_DICT_VER_1,
                           RESEARCHER_DICT_VER_2),
                          (RESEARCHER_DICT_VER_1['identifiers'],
                           RESEARCHER_DICT_VER_2['identifiers'])])
def test_dict_base_hash_equal(value_1: Any, value_2: Any):
    assert dict_base_hash(value_1) == dict_base_hash(value_2)


def test_hashing_function_false_values():
    none_hash = dict_base_hash(None)

    # NOT None-equivalent falsies
    assert dict_base_hash(0) != none_hash
    assert dict_base_hash(0.) != none_hash
    assert dict_base_hash('') != none_hash
    assert dict_base_hash(False) != none_hash

    # None-equivalents falsies
    for none_equivalent in NONE_EQUIVALENT_VALUES:
        assert dict_base_hash(none_equivalent) == none_hash


@pytest.mark.parametrize('none_equivalent_value', NONE_EQUIVALENT_VALUES)
def test_hashing_function_dicts(none_equivalent_value):
    absent_hash = dict_base_hash({'a': 'b'})
    none_equivalent_hash = dict_base_hash({'a': 'b',
                                           'c': none_equivalent_value})
    assert absent_hash == none_equivalent_hash


def test_nested():
    dict_1 = {'a': [{'aa': 5, 'ab': [5, 6, {'aaa': [4, 5, 6]}]},
                    {'aa': 7, 'ab': [1, 2, 3]}]}
    dict_2 = {'a': [{'aa': 7, 'ab': [1, 2, 3]},
                    {'aa': 5, 'ab': [5, 6, {'aaa': [6, 5, 4]}]}]}
    assert dict_base_hash(dict_1) == dict_base_hash(dict_2)


def test_duplicates():
    dict_1 = {'a': [1, 2, 3]}
    dict_2 = {'a': [3, 2, 1]}
    assert dict_base_hash(dict_1) == dict_base_hash(dict_2)


def test_empty_obj():
    assert hash(Base()) == 0
    assert hash(Base(data_dict={})) == 0


def test_different_hashes():
    assert dict_base_hash(RESEARCHER_DICT_VER_2) != dict_base_hash(
        RESEARCHER_DICT_VER_3)
