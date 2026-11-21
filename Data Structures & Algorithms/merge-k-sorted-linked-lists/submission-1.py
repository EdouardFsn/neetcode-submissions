# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two_lists(list1: Optional[ListNode] , list2: Optional[ListNode]) -> Optional[ListNode]:
            newlist = ListNode()
            dummy = newlist
            while (list1 and list2):
                if (list1.val <= list2.val):
                    dummy.next = list1
                    list1 = list1.next
                    dummy = dummy.next
                else:
                    dummy.next = list2
                    list2 = list2.next
                    dummy = dummy.next
            while (list1):
                dummy.next = list1
                list1 = list1.next
                dummy = dummy.next
            while (list2):
                dummy.next = list2
                list2 = list2.next
                dummy = dummy.next
            if(newlist.next):
                return newlist.next
            else:
                return None

        new_lists = []
        for i in range(0,len(lists),2):
            if i+1 < len(lists):
                new_lists.append(merge_two_lists(lists[i],lists[i+1]))  
            else:
                new_lists.append(lists[i])
        if len(new_lists) > 1:
            return self.mergeKLists(new_lists)
        if len(new_lists) == 1:
            return new_lists[0]
        if len(new_lists) == 0:
            return None

        







            

        