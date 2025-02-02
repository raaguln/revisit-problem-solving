'''
Store addresses
Time: O(n)
Space: O(n)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        uniqueReferences = set()
        nodesCount = 0
        curr = head
        while curr:
            uniqueReferences.add(curr)
            nodesCount += 1
            if len(uniqueReferences) != nodesCount:
                return True
            curr = curr.next
        return False


'''
Fast and slow pointers
Time: O(n)
Space: O(1)
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while slow and fast:
            slow = slow.next
            fast = fast.next
            if not fast:
                return False
            fast = fast.next
            if slow == fast:
                return True
        return False