# Definition for a Node.
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root):
        if not root:
            return None

        # Start from the leftmost node of the current level
        leftmost = root

        # Since it's a perfect binary tree, we only need to check left children
        while leftmost.left:
            head = leftmost
            while head:
                # Connect left -> right
                head.left.next = head.right

                # Connect right -> next left if possible
                if head.next:
                    head.right.next = head.next.left

                # Move to the next node in the current level
                head = head.next

            # Move to the leftmost node of the next level
            leftmost = leftmost.left

        return root
