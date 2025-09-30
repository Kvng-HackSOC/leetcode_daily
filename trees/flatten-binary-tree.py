class Solution:
    def flatten(self, root):
        def helper(node):
            if not node:
                return None
            # Flatten left and right subtrees
            left_tail = helper(node.left)
            right_tail = helper(node.right)

            # If there is a left subtree, attach it between node and node.right
            if left_tail:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # Return the tail of the flattened tree
            return right_tail or left_tail or node

        helper(root)
