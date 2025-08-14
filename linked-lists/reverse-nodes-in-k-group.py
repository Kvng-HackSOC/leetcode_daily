class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        
        while True:
            # Find the kth node
            kth = self.get_kth(group_prev, k)
            if not kth:
                break  # Less than k nodes remain
            group_next = kth.next
            
            # Reverse the group
            prev, curr = kth.next, group_prev.next
            while curr != group_next:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            # Adjust connections
            tmp = group_prev.next
            group_prev.next = kth
            group_prev = tmp
        
        return dummy.next
    
    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
