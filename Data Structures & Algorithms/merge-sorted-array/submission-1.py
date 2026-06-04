class Solution:
    def merge(self, nums1: List[int], m: int,
              nums2: List[int], n: int) -> None:
        """
        Modify nums1 in-place so that it contains all
        elements from nums1 and nums2 in sorted order.
        """

        # Last valid element in nums1
        i = m - 1

        # Last element in nums2
        j = n - 1

        # Last position in nums1 where we can write
        k = m + n - 1

        # Merge from the back
        while i >= 0 and j >= 0:

            # Place the larger element at position k
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # If nums2 still has elements left,
        # copy them into nums1.
        #
        # We only need this loop because if nums1
        # has remaining elements, they are already
        # in the correct positions.
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1