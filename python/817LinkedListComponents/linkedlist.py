class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        res = 0
        s = set(nums)
        isConnected = False
        while head:
            if head.val in s:
                isConnected = True
            if head.val not in s and isConnected:
                isConnected = False
                res += 1
            head = head.next
        if isConnected:
            res += 1
        return res
