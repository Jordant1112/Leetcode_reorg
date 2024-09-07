class Solution:
    def connect(self, root):
         if not root:
             return None
         node = root
         queue = deque([root])
         while queue:
             size = len(queue)
             for i in range(size):
                 n = queue.popleft()
                 if not n:
                     continue
                 if i < size -1:
                     n.next = queue[0]
                 if n.left:
                     queue.append(n.left)
                 if n.right:
                     queue.append(n.right)
        return node

