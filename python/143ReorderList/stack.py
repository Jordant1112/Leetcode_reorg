class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        p = head
        stack = []
        while p:
            stack.append(p)
            p = p.next

        p = head
        while p:
            lastNode = stack.pop()
            next = p.next
            if lastNode == next or lastNode.next == next:
                lastNode.next = None
                break
            p.next = lastNode
            lastNode.next = next
            p = next
        return head
