'''
Given a singly linked list, group all odd nodes together followed by the even nodes. 
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example:
Given 1->2->3->4->5->NULL,
return 1->3->5->2->4->NULL.

Note:
The relative order inside both the even and odd groups should remain as it was in the input. 
The first node is considered odd, the second node even and so on ...

Credits:
Special thanks to @DjangoUnchained for adding this problem and creating all test cases.
'''
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if not head.next:
            return head
        odd = head
        even = head.next
        odd_head = odd
        even_head = even
        while odd and even:
            odd.next = even.next
            if odd.next:
                odd = odd.next
            else:
                break
            if odd:
                even.next = odd.next
                even = even.next

        odd.next = even_head
        return odd_head

node = ListNode(-1)
head = node
for i in range(10):
   node.next = ListNode(i)
   node = node.next


#print node.val, head.val

obj = Solution()
new_head = obj.oddEvenList(head.next)

while new_head:
    print new_head.val
    new_head = new_head.next

