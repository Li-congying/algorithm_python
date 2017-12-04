'''
Given a binary tree, write a function to get the maximum width of the given tree. 
The width of a tree is the maximum width among all levels. The binary tree has the same structure as a full binary tree, 
but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in the level, 
where the null nodes between the end-nodes are also counted into the length calculation.

Example 1:
Input: 
           1
         /   \
        3     2
       / \     \  
      5   3     9 

Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:
Input: 

          1
         /  
        3    
       / \       
      5   3     

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:
Input: 

          1
         / \
        3   2 
       /        
      5      

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:
Input: 

          1
         / \
        3   2
       /     \  
      5       9 
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        max_length = 1

        queue = [(0, 0, root)]
        last_l = -1
        id_start = id_end = 0
        while queue:
            level, l_id, node = queue.pop(0)
            if level != last_l:
                max_length = max(id_end-id_start+1, max_length)
                last_l = level
                id_start = l_id if node else None
                id_end = id_start
            else:
                if node:
                    if not id_start:
                        id_start = l_id
                        id_end = l_id
                    else:
                        id_end = l_id

            if node:
                queue.append((level+1, 2*l_id + 1, node.left))
                queue.append((level+1, 2*l_id + 2, node.right))

        return max_length


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
#root.right.left = TreeNode(6)
root.right.right = TreeNode(5)
root.left.left.left = TreeNode(7)
#root.right.left.right = TreeNode(8)
root.right.right.right = TreeNode(10)


#[1,1,1,1,null,null,1,1,null,null,1]
obj = Solution()
print obj.widthOfBinaryTree(root)
