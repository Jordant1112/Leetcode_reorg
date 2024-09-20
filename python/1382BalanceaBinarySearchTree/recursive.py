class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.res = []
        self.inorder(root)
        return self.construct(float('-inf', float('inf'), self.res)


    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        self.res.append(root.val)
        self.inorder(root.right)

    def construct(self, left, right, res):
        if not res:
            return 
        mid = len(res)//2
        root = TreeNode(res[mid])
        root.left = self.construct(left, root.val, res[:mid])
        root.right = self.construct(root.val, right, res[mid+1:])
        return root

