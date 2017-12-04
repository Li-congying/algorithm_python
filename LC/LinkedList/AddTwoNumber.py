'''
You are given two non-empty linked lists representing two non-negative integers. 
The most significant digit comes first and each of their nodes contain a single digit. 
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        stack_1 = []
        stack_2 = []
        node = l1
        while node:
            stack_1.append(node)
            node = node.next
        node = l2
        while node:
            stack_2.append(node)
            node = node.next

        nxt = None
        base = 0
        while stack_1 and stack_2:
            val = stack_1.pop().val + stack_2.pop().val + base
            node = ListNode(val%10)
            node.next = nxt
            nxt = node
            base = val / 10

        left = stack_1 if stack_1 else stack_2 if stack_2 else None
        while left:
            val = left.pop().val + base
            node = ListNode(val % 10)
            node.next = nxt
            nxt = node
            base = val/10

        #print base
        if base:
            head = ListNode(1)
            head.next = node
            return head
        else:
            return node

obj = Solution()

head_1 = None
node = head_1
for i in [2,3,9]:
    if not node:
        head_1 = ListNode(i)
        node = head_1
    else:
        node.next = ListNode(i)
        node = node.next

head_2 = None
node_2 = head_2
for i in [9]:
    if not node_2:
        head_2 = ListNode(i)
        node_2 = head_2
    else:
        node_2.next = ListNode(i)
        node_2 = node_2.next

new_head = obj.addTwoNumbers(head_1, head_2)

while new_head:
    print new_head.val
    new_head = new_head.next
