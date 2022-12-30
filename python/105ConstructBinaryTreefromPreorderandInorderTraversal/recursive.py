class Solution:
    def buildTree(self, preorder:List[int], inorder:List[int]) ->
    Optional[TreeNode]:
        if not preorder or not inorder:
            return 
        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        preorder.pop(0)
        root.left = self.buildTree(preorder, inorder[:idx]
        root.right = self.buildTree(preorder, inorder[idx+1:]
        return root
