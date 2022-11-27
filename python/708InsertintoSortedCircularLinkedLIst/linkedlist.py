class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head:
            tmp = Node(insertVal,None)
            tmp.next = tmp
            return tmp
        prev = head
        curr = head.next
        toInsert = False
        while True:
            if curr.val >= insertVal >= prev.val:
                toInsert = True
            elif prev.val > curr.val:
                if insertVal >= prev.val or insertVal <= curr.val:
                    toInsert = True
            if toInsert:
                prev.next = Node(insertVal, curr)
                return head
            prev = prev.next
            curr = curr.next
            if prev == head:
                break
        prev.next = Node(insertVal, curr)
        return head
