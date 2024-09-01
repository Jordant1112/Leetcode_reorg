class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int)
    -> List[int]:
        self.res = []
        sel, target: float, k: int) -> List[int]:
            self.res = []
            self.inorder(root)
            return self.find_closest_element(target, k)


    def inorder(self, root):
        if not root:
            return
        if root.left:
            self.inorder(root.left)
        self.res.append(root)
        if root.right:
            self.inorder(root.right)

    def find_closest_element(tagret, k ):
        l = 0
        r = len(self.res)-1
        while r - l >= k:
            if abs(self.res[r]-target) >= abs(self.res[l] - target):
                r -= 1
            else:
                l += 1
        return self.res[l:l+k]
