class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        sign = ['+', '-', '*', '/']
        for i in tokens:
            if i not in sign:
                stack.append(i)
            else:
                tmp1 = int(stack.pop())
                tmp2 = int(stack.pop())
                if i == '+':
                    stack.append((str(tmp1+tmp2)))
                elif i == '-':
                    
                    stack.append((str(tmp2-tmp1)))
                elif i == '*':
                    
                    stack.append((str(tmp2*tmp1)))
                elif i == '/':
                    stack.append((str(int(tmp2/tmp1))))
        return int(stack[-1])
