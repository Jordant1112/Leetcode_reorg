class Solution:
    def isPreorder(self, nodes: List[List[int]]) -> bool:
        preorder = []
        d = defaultdict(list)
        for i, j in nodes:
            d[j].append(i)
        self.dfs(root, parent, preorder, d)
        return preorder == nodes

    def dfs(self, root, parent, preorder, d):
        preorder.append([root, parent])
        for nei in d[root]:
            self.dfs(nei, root, preorder, d)
