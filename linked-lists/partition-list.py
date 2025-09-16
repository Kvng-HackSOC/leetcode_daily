class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def partition(self, head, x):
        before_head = ListNode(0)
        after_head = ListNode(0)

        before = before_head
        after = after_head

        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next


# --- Helpers for testing ---
def build_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# --- Example Test Cases ---
if __name__ == "__main__":
    s = Solution()

    head = build_linked_list([1, 4, 3, 2, 5, 2])
    x = 3
    new_head = s.partition(head, x)
    print(linked_list_to_list(new_head))  # [1, 2, 2, 4, 3, 5]

    head = build_linked_list([2, 1])
    x = 2
    new_head = s.partition(head, x)
    print(linked_list_to_list(new_head))  # [1, 2]
