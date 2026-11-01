import pytest
from gpa import calculate_gpa, is_passed


def test_gpa_weighted_average():
    assert calculate_gpa([(18, 3), (14, 2)]) == 16.4


def test_gpa_empty_list_raises():
    with pytest.raises(ValueError):
        calculate_gpa([])


def test_is_passed_boundary():
    assert is_passed(10) is True
    assert is_passed(9.99) is False
    