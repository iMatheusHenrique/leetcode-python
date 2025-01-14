import pytest
from palindrome_number import app as palindrome_number_solution_obj 

@pytest.fixture
def fixture_palindrome_number_solution_obj():
    return palindrome_number_solution_obj.Solution()

@pytest.mark.parametrize(
    "input, expected_result",
    [
        (121, True),
        (10, False),
        (-121,False),
    ]
)
def test_group_anagrams_output(
    fixture_palindrome_number_solution_obj,
    input,
    expected_result
    ):
    result = fixture_palindrome_number_solution_obj.isPalindrome(input)
    assert result == expected_result

