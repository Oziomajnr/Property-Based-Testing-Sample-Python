from hypothesis import given, strategies as st


def sort_list(nums):
    # Implementation of a simple sorting function (bubble sort)
    for i in range(len(nums)):
        for j in range(0, len(nums) - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


def is_sorted(nums):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


# Property-based test

@given(st.lists(st.integers()))
def test_sort_list_property_based(nums):
    assert is_sorted(sort_list(nums))
