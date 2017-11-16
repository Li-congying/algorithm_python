'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        self.result = []
        def helper(node, cur_sum, total, path, result):

            cur_sum = cur_sum + node.val
            path.append(node.val)
            if cur_sum == total and not node.left and not node.right:
                result.append(path)

            if node.left and node.left.val + cur_sum <= total:
                helper(node.left, cur_sum, total, path[:], result)
            if node.right and node.right.val + cur_sum <= total:
                helper(node.right, cur_sum, total, path[:], result)


        helper(root, 0, sum, [], self.result)
        return self.result


node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.left = node_2
node_1.right = node_3

obj = Solution()
print obj.pathSum(node_1, 5)




