# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1, temp2 = list1, list2
        res = ListNode()
        temp = res

        while temp1 is not None and temp2 is not None:
            if temp1.val < temp2.val:
                temp.next = ListNode(temp1.val)
                temp1 = temp1.next
            else:
                temp.next = ListNode(temp2.val)
                temp2 = temp2.next

            temp = temp.next

        if temp1 is not None:
            temp.next = temp1
        if temp2 is not None:
            temp.next = temp2

        return res.next