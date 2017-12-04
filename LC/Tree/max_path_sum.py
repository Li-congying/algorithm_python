'''
Given a binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node 
to any node in the tree along the parent-child connections. The path must contain at least one node and does 
not need to go through the root.

For example:
Given the below binary tree,

       1
      / \
     2   3
Return 6.
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max = float('-inf')

        def helper(node):
            if not node:
                return 0

            left = helper(node.left)
            right = helper(node.right)
            cur_sum = node.val + left + right
            self.max = max(cur_sum, self.max)
            return max(node.val+left, node.val + right)

        helper(root)
        return self.max


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(9)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

obj = Solution()
print obj.maxPathSum(root)



