# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Create a mapping from old nodes to new nodes
        old_to_new = {}

        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next

        # Step 2: Assign next and random pointers using the mapping
        current = head
        while current:
            if current.next:
                old_to_new[current].next = old_to_new[current.next]
            if current.random:
                old_to_new[current].random = old_to_new[current.random]
            current = current.next

        # Step 3: Return the copied head node
        return old_to_new[head]
