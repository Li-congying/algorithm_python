'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
    \
    1
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        max_v = float('-inf')
        max_id = -1
        for i in range(len(nums)):
            if nums[i] > max_v:
                max_id = i
                max_v = nums[i]
        root = TreeNode(max_v)
        root.left = self.constructMaximumBinaryTree(nums[0:max_id])
        root.right = self.constructMaximumBinaryTree(nums[max_id+1:])
        return root

        '''
        st = []
        for num in nums:
            cur = TreeNode(num)
            while st and st[-1].val < num:
                cur.left = st.pop()
            if st: st[-1].right = cur
            st.append(cur)
        return st[0] if st else None
        '''
