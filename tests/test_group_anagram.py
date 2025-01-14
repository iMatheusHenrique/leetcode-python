import pytest
from group_anagrams import app as group_anagrams_solution_obj 

@pytest.fixture
def fixture_group_anagrams_solution_obj():
    return group_anagrams_solution_obj.Solution()

@pytest.mark.parametrize(
    "input, expected_result",
    [
        (["eat", "tea", "tan", "ate", "nat", "bat"],[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]),
        (["a"],[["a"]]),
        ([""],[[""]]),
    ]
)
def test_group_anagrams_output(
    fixture_group_anagrams_solution_obj,
    input,
    expected_result
    ):
    result = fixture_group_anagrams_solution_obj.groupAnagrams(input)
    assert result == expected_result


@pytest.mark.parametrize(
    "input",
    [
        1,
        [1, "abc"],
        None,
    ]
)
def test_group_anagrams_invalid_input(fixture_group_anagrams_solution_obj, input):
    with pytest.raises(Exception):
        fixture_group_anagrams_solution_obj.groupAnagrams(input)
