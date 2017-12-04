'''
Print a binary tree in an m*n 2D string array following these rules:
Example 1:
Input:
     1
    /
   2
Output:
[["", "1", ""],
 ["2", "", ""]]
Example 2:
Input:
     1
    / \
   2   3
    \
     4
Output:
[["", "", "", "1", "", "", ""],
 ["", "2", "", "", "", "3", ""],
 ["", "", "4", "", "", "", ""]]
Example 3:
Input:
      1
     / \
    2   5
   / 
  3 
 / 
4 
Output:

[["",  "",  "", "",  "", "", "", "1", "",  "",  "",  "",  "", "", ""]
 ["",  "",  "", "2", "", "", "", "",  "",  "",  "",  "5", "", "", ""]
 ["",  "3", "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]
 ["4", "",  "", "",  "", "", "", "",  "",  "",  "",  "",  "", "", ""]]
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root:
            return []
        self.height = 0
        def getHeight(root, height):
            height += 1
            self.height = max(self.height, height)
            if root.left:
                getHeight(root.left, height)
            if root.right:
                getHeight(root.right, height)
        getHeight(root, 0)

        result = [[""] * (2**self.height-1) for _ in range(self.height)]


        queue = [(0, root, 0, 2**self.height-2)]
        while queue:
            row, node, start, end = queue.pop(0)
            index = start + (end - start)/2
            result[row][index] = node.val
            if node.left:
                queue.append((row+1, node.left, start, index-1))
            if node.right:
                queue.append((row+1, node.right, index+1, end))

        print result


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.right.right = TreeNode(4)

obj = Solution()
obj.printTree(root)