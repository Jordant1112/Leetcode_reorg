class Solution:
    def mergeKlists(self, lists: List[Optional[ListNode]]) ->
    Optional[ListNode]:
        if not lists:
            return None
        pq = []
        dummy = p = ListNode(0)
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(pq, (head.val, i, head))

        while pq:
            val, i, node = heapq.heappop(pq)
            if node.next:
                heapq.heappush(pq, (node.next.val, i, node.val))
            p.next = node
            p = p.next
        return dummy.next
