class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        self.g = defaultdict(list)
        tmp = {}
        self.visited = {}
        for i in range(n):
            tmp[i] = 1
        for i in range(n):
            if leftChild[i] != -1:
                self.g[i].append(leftChild[i])
                if leftChild[i] in tmp:
                    del tmp[leftChild[i]]
            if rightChild[i] != -1:
                self.g[i].append(rightChild[i])
                if rightChild[i] in tmp:
                    del tmp[rightChild[i]]
        if len(tmp) != 1:
            return False
        for key in tmp.keys():
            root = key
        ans = self.dfs(root)
        if ans and len(self.visited) == n:
            return True
        return False
    
    def dfs(self, node):
        if node in self.visited:
            return False
        ans = True
        self.visited[node] = 1
        for child in self.g[node]:
            ans = ans and self.dfs(child)
        return ans
