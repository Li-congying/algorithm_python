'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. 
This path may or may not pass through the root.
Note: The length of path between two nodes is represented by the number of edges between them.
Example 1:
Input:
              5
             / \
            4   5
           / \   \
          1   1   5
Output:
2

Example 2:
Input:
              1
             / \
            4   5
           / \   \
          4   4   5
Output:
2
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

'''
class Solution {  
    int re = 0;  
    public int longestUnivaluePath(TreeNode root) {  
        help(root, 0);  
        return re;  
    }  
  
    public int help(TreeNode root, int n) {  
        if (root == null)  
            return 0;  
        int left = help(root.left, root.val);  
        int right = help(root.right, root.val);  
        re = Math.max(re, left + right);  
        return root.val == n ? Math.max(left, right) + 1 : 0;  
    }  
}  
'''

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.max = 0
        def helper(root, last_val):
            if not root:
                return 0
            left = helper(root.left, root.val)
            right = helper(root.right, root.val)
            self.max = max(self.max, left + right)
            return max(left, right)+1 if root.val == last_val else 0

        helper(root, None)
        print self.max




root = TreeNode(0)
root.left = TreeNode(1)
root.left.left = TreeNode(1)
root.right = TreeNode(2)

obj = Solution()
obj.longestUnivaluePath(root)
