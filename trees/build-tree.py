def serialize(root):
    """Convert tree to list (level-order) for testing."""
    from collections import deque
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            res.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            res.append(None)
    # remove trailing None values
    while res and res[-1] is None:
        res.pop()
    return res
