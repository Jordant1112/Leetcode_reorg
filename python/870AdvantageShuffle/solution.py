class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums2_new = [(val, idx) for idx, val in enumerate(nums2)]
        nums2_new.sort(key=lambda x: x[0], reverse=True)

        nums1_sorted = sorted(nums1)

        left = 0
        right = n-1
        res = [0]* n
        for val, idx in nums2_new:
            if nums1_sorted[right] > val:
                res[idx] = nums1_sorted[right]
                right -= 1
            else:
                res[idx] = nums1_sorted[left]
                left += 1
        return res
