# Definition for a binary tree node.
# class Node(object):
#     def __init__(self, val=" ", left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEquivalence(self, root1: 'Node', root2: 'Node') -> bool:
        count1 = {} 
        count2 = {}
        self.traverse(root1, count1)
        self.traverse(root2, count2)
        return True if count1 == count2 else False
    


    def traverse(self, root, count):
        if not root:
            return
        if root.val not in count:
            count[root.val] = 1
        else:
            count[root.val] += 1
        if root.left:
            self.traverse(root.left, count)
        if root.right:
            self.traverse(root.right, count)
