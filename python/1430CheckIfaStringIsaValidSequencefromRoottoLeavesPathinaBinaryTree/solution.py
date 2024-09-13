class Solution:
    def isValidSequence(self, root: Optional[TreeNode], arr: List[int]) ->
    bool:
        return self.helper(root, arr, 0)

    def helper(self, root, arr, idx):
        if not root or idx == len(arr):
            return False
        if not root.left and not root.right:
            return arr[idx]== root.val and idx == len(arr)-1
        return self.helper(root.left, arr, idx+1) ir self.helper(root.right,
                arr, idx+1)
