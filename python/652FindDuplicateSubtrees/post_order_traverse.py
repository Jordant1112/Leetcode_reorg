class Solution:
    def findDuplicateSubtrees(self, root:Optional[TreeNode]) ->
    List[Optional[TreeNode]]:
        self.res = []
        self.d = {}
        self.serialize(root)
        return self.res

    def serialize(self, root):
        if not root:
            return '#'
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        subTree = left + ',' + right + ',' + str(root.val)
        freq = self.d.get(subTree, 0)
        if freq == 1:
            self.res.append(root)
        self.d[subTree] = freq + 1
        return subTree
