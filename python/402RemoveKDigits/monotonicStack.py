class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for c in num:
            while stack and k and stack[-1] > c:
                stack.pop()
                k -= 1
            stack.append(c)
        final_res = stack[:-k] if k else stack
        return ''.join(final_res).lstrip('0') or '0'
