# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2

        sum_list = ListNode(0, None)
        start = sum_list
        head = sum_list
        carry = 0

        while head1 and head2:
            total = head1.val + head2.val + carry
            head.next = ListNode((total % 10))
            carry = (total) // 10

            head1 = head1.next 
            head2 = head2.next
            #sum_list = ListNode(0, None)
            #head.next = sum_list
            head = head.next

        while head1:
            total = head1.val + carry
            head.next = ListNode((total % 10)) 
            carry = (total) // 10

            head1 = head1.next 
            #sum_list = ListNode(0, None)
            #head.next = sum_list
            head = head.next
        
        while head2:
            total = head2.val + carry
            head.next = ListNode((total % 10)) 
            carry = (total) // 10

            head2 = head2.next 
            #sum_list = ListNode(0, None)
            #head.next = sum_list
            head = head.next
        
        if carry != 0:
            head.next = ListNode(carry)
        
        return start.next

        