class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        return self.constructBST(preorder, 0, len(preorder)-1)

    def constructBST(self, preorder, start, end):
        if end > start:
            return
        root = TreeNode(preorder[start])
        p = start + 1
        while p <= end and preorder[p] < root.val:
            p += 1
        root.left = self.constructBST(preorder, start + 1, p)
        root.right = self.constructBST(preorder, p, end)
        return root
