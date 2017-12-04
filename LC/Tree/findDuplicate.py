'''
Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees,
 you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1: 
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
The following are two duplicate subtrees:
      2
     /
    4
and
    4
Therefore, you need to return above trees' root in the form of a list.

'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if not root:
            return []
        self.hash_ = {}
        self.result = []
        def helper(node):
            if not node.left and not node.right:
                if node.val in self.hash_:
                    self.result.append(node)
                self.hash_[node.val] = 1
                return str(node.val)

            left = right = ""
            if node.left:
                left = helper(node.left)
            if node.right:
                right = helper(node.right)
            str_ = left + str(node.val) + right
            if str_ in self.hash_:
                print str_
                self.result.append(node)
            self.hash_[str_] = 1
            return str_

        helper(root)
        return self.result



root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

obj = Solution()
list =  obj.findDuplicateSubtrees(root)



