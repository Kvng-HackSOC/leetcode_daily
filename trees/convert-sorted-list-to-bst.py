class Solution:
    def sortedListToBST(self, head):
        # Convert linked list to array
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        # Recursive helper to build BST
        def buildBST(left, right):
            if left > right:
                return None
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = buildBST(left, mid - 1)
            root.right = buildBST(mid + 1, right)
            return root

        return buildBST(0, len(nums) - 1)
