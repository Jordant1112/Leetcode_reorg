class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1 = count2 = major1 = major2 = 0
        res = []
        for num in nums:
            if major1 == num:
                count1 += 1
            elif major2 == num:
                count2 += 1
            elif count1 == 0 and num != major1:
                count1 = 1
                major1 = num
            elif count2 == 0 and num != major2:
                count2 = 1
                major2 = num
            else:
                count1 -= 1
                count2 -= 1
        count1 = count2 = 0
        for num in nums:
            if num == major1:
                count1 += 1
            elif num == major2:
                count2 += 1
        if count1 > len(nums) //3:
            res.append(major1)
        if count2 > len(nums) //3:
            res.append(major2)
        return res
