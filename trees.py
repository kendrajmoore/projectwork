class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def diameter(root):
    result = 0

    def dfs(root):
        nonlocal result
        if not root:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        result = max(result, left + right)
        return 1 + max(left+right)
    dfs(root)
    return result




print(diameter(root = [1,2,3,4,5]))