from hypothesis import given, strategies as st, settings, Verbosity


def sort_list(nums):
    # Implementation of a simple sorting function (bubble sort)
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


# Example-based test

def test_sort_list_example_based():
    assert sort_list([3, -1, 4, -5, 2]) == [-5, -1, 2, 3, 4]
    assert sort_list([1, 2, 3, 4, 5, 6, 7]) == [1, 2, 3, 4, 5, 6, 7]
    assert sort_list([-1, -100, 15, -19, 0, 0]) == [-100, -19, -1, 0, 0, 15]


def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def test_sort_list_example_based_improved():
    # create a list of lists
    for item in [[3, -1, 4, -5, 2], [1, 2, 4, 5, 6, 7], [-1, -100, 15, -19, 0, 0], []]:
        assert is_sorted(sort_list(item))


# Property-based test

@given(st.lists(st.integers()))
def test_sort_list_property_based(nums):
    assert is_sorted(sort_list(nums))
