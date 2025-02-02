'''
Note - Mistakes you made -
1. you used while list1 and while list2. That threw errors. If is enough because it has the pointers for the remaining list.
2. You did not return head.next. You returned curr.next. That threw errors.
3. You did not create a pointer to the head node and tried to use the head node directly. That threw errors.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        curr = head
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        if list2:
            curr.next = list2
        return head.next
