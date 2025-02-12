# Time: O(n)
# Space: O(n)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Skip reordering if under 4 nodes
        if not head or not head.next or not head.next.next:
            return
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        dummy = ListNode()
        prev = dummy

        n = len(nodes)
        left, right = 0, n-1

        while left <= right:
            # 0 -> 1
            prev.next = nodes[left]
            # sets prev as 1
            prev = nodes[left]
            left += 1
            
            if left <= right:
                # 1 -> 2
                prev.next = nodes[right]
                # sets prev as 2
                prev = nodes[right]
                right -= 1
        prev.next = None
            

 

# Time: O(n)
# Space: O(1)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # even = slow at end. odd -> slow at middle.
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse links for second half

        # Move to 3 (even) / 4 (odd)
        second = slow.next
        prev = None
        slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
            

 

        