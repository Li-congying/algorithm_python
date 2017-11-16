# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [[root, 0]]
        result = {}
        while queue:
            q = queue[0]
            del (queue[0])
            if q[1] not in result:
                result[q[1]] = []
            result[q[1]].append(q[0].val)
            if q[0].left:
                queue.append([q[0].left, q[1]+1])
            if q[0].right:
                queue.append([q[0].right, q[1]+1])
        return result.values()

s = Solution()
node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_1.left = node_2
node_1.right = node_3

result = s.levelOrder(node_1)
print result
