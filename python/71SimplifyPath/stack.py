class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        data = path.split('/')
        for word in data:
            if word == '' or word == ' ' or word == '.':
                continue
            elif word == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(word)
        return '/' + '/'.join(stack)
