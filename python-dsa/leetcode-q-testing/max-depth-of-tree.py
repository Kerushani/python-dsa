from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        countLeft = 0

        if root == None:
            return
        
        self.maxDepth(root.left)
        print(root.val)

        self.maxDepth(root.right)

        return root

# Example usage
if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    depth = solution.maxDepth(root)
    print("Max depth:", depth)
