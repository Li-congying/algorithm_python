'''
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such 
that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if not root:
            return False
        hash_table = {}
        stack = []
        node = root
        while node:
            hash_table[node.val] = hash_table.get(node.val, 0) + 1
            if node.right:
                stack.append(node.right)
            node = node.left
            if not node and stack:
                node = stack.pop()

        for i in hash_table:
            if k - i in hash_table:
                if k - i != i or hash_table[k-i] >=2:
                    return True
        else:
            return False


root = TreeNode(5)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(4)

obj = Solution()
print obj.findTarget(root, 10)