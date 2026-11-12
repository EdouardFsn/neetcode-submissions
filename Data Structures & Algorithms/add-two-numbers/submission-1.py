# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        temp = 0

        while (l1 or l2):
            v1 = l1.val if l1 else 0    
            v2 = l2.val if l2 else 0 
            v3 = v1 + v2 + temp
            temp = 0
            if ( v3 >= 10):
                temp = 1
                v3 -= 10
            cur.next = ListNode(v3)
            cur = cur.next
            if l1: l1 = l1.next 
            if l2: l2 = l2.next 
        if ( temp == 1):
            cur.next = ListNode(1)


        return dummy.next




        