class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        ans = [0]* n
        for log in logs:
            id, action, ts = log.split(':')
            id = int(id)
            ts = int(ts)
            if action == 'start':
                if stack:
                    ans[stack[-1][0]] += ts - stack[-1][1]
                stack.append([id, ts])
            else:
                ans[stack[-1][0]] += ts - stack.pop()[1] + 1
                if stack:
                    stack[-1][1] = ts +1
        return ans
