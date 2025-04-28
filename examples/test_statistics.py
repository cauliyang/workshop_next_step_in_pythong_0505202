import pytest

# This is our test file for statistics calculation
# Following TDD principles: write tests first, then implement the functionality


def test_calculate_statistics_basic():
    """Test basic statistics calculation with positive numbers."""
    # This test assumes the function doesn't exist yet or is incomplete
    # According to TDD, we write the test first

    numbers = [1, 2, 3, 4, 5]
    stats = calculate_statistics(numbers)

    assert stats["min"] == 1
    assert stats["max"] == 5
    assert stats["average"] == 3.0


def test_calculate_statistics_negative():
    """Test statistics calculation with negative numbers."""
    numbers = [-5, -3, -1, 0, 2]
    stats = calculate_statistics(numbers)

    assert stats["min"] == -5
    assert stats["max"] == 2
    assert stats["average"] == -1.4


def test_calculate_statistics_single_value():
    """Test statistics calculation with a single value."""
    numbers = [42]
    stats = calculate_statistics(numbers)

    assert stats["min"] == 42
    assert stats["max"] == 42
    assert stats["average"] == 42.0


def test_calculate_statistics_empty_list():
    """Test that an empty list raises a ValueError."""
    with pytest.raises(ValueError) as excinfo:
        calculate_statistics([])

    assert "empty list" in str(excinfo.value)


# Once the tests are written, participants will implement the function
# to make these tests pass during the workshop
