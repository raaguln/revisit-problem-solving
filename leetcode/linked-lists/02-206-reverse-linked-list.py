# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
Store values in list and then update the linked list
Time: O(n)
Space: O(n)
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next
        
        i, n = -1, len(values)
        curr = head
        while curr:
            curr.val = values[i]
            curr = curr.next
            i -= 1
        return head


'''
Using pointers
Time: O(n)
Space: O(1)
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        return prev
