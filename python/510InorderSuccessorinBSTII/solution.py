"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right:
            root = node.right
            while root and root.val < node.val:
                root = root.left
            return root
        else:
            curr = node.parent
            while curr and curr.val < node.val:
                curr = curr.parent
            return curr
