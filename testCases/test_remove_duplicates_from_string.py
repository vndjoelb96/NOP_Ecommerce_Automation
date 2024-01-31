import pytest


def remove_duplicates(input_str):
    result = ''
    for char in input_str:
        if char not in result:
            result += char
    return result


@pytest.mark.parametrize("input_str, expected_output", [
    ('aabbccccd', 'abcd'),
    ('abcde', 'abcde'),
    ('aaaabbbb', 'ab'),
    ('', ''),
    ('abcdabcd', 'abcd')
])
def test_remove_duplicates(input_str, expected_output):
    result = remove_duplicates(input_str)
    assert result == expected_output
