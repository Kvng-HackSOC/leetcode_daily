class Solution:
    def mergeKLists(self, lists):
        import heapq
        heap = []
        for i, l in enumerate(lists):
            while l:
                heapq.heappush(heap, l.val)
                l = l.next
        
        dummy = ListNode(0)
        curr = dummy
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        return dummy.next
