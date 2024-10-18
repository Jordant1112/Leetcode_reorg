class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')
        first_when_second_registered = None
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
                first_when_second_registered = first
            else:
                print(first_when_second_registered, second, n)
                return True
        return False
