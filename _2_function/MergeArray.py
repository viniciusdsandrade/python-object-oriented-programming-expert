from typing import List


# 88. Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order,
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
#
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
#
# The final sorted array should not be returned by the function,
# but instead be stored inside the array nums1.
# To accommodate this, nums1 has a length of m + n,
# the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length of n.


# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

# Example 2:
# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].

# Example 3:
# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1.
# The 0 is only there to ensure the merge result can fit in nums1.

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    # 1. Create a copy of nums1
    nums1_copy = nums1[:m]
    nums1[:] = []

    # 2. Initialize the pointers for nums1_copy and nums2
    p1 = 0
    p2 = 0

    # 3. Compare elements from nums1_copy and nums2
    while p1 < m and p2 < n:
        if nums1_copy[p1] < nums2[p2]:
            nums1.append(nums1_copy[p1])
            p1 += 1
        else:
            nums1.append(nums2[p2])
            p2 += 1

    # 4. If there are still elements in nums1_copy, append them to nums1
    if p1 < m:
        nums1[p1 + p2:] = nums1_copy[p1:]
    # 5. If there are still elements in nums2, append them to nums1
    if p2 < n:
        nums1[p1 + p2:] = nums2[p2:]


def test():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    print("nums1:", nums1)
    print("m:", m)
    print("nums2:", nums2)
    print("n:", n)

    merge(nums1, m, nums2, n)
    print("Output:", nums1)


def main():
    test()


if __name__ == "__main__":
    main()
