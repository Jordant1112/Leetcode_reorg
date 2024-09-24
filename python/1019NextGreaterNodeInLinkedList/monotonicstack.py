class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = []
        while head:
            res.append(head.val)
            head = head.next
        n = len(res)
        result = [0] * n
        for i in range(n-1, -1, -1):
            while stack and stack[-1] <= res[i]:
                stack.pop()
            result[i] = stack[-1] if stack else 0
            stack.append(res[i]
        return result
