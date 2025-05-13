from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1  # Last valid element in nums1
        p2 = n - 1  # Last element in nums2
        p3 = m + n - 1  # Last position in nums1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p3] = nums2[p2]
                p2 -= 1
                p3 -= 1
            elif nums1[p1] > nums2[p2]:
                nums1[p3] = nums1[p1]
                p1 -= 1
                p3 -= 1
            else:  # nums1[p1] == nums2[p2]
                nums1[p3] = nums2[p2]
                p2 -= 1  # Decrement p2
                p3 -= 1  # Decrement p3
                # Leave p1 untouched

        # Copy remaining elements from nums2 into nums1 (if any)
        while p2 >= 0:
            nums1[p3] = nums2[p2]
            p2 -= 1
            p3 -= 1
