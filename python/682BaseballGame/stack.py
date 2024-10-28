class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sign = ['+', 'C', 'D']
        stack = []
        res = []
        for o in operations:
            if o not in sign:
                stack.append(int(o))
            else:
                if o == '+':
                    tmp1 = stack[-1]
                    tmp2 = stack[-2]
                    stack.append(tmp1 + tmp2)
                elif o == 'C':
                    stack.pop()
                elif o == 'D':
                    tmp = stack[-1] * 2
                    stack.append(tmp)
        return sum(stack)
                    

