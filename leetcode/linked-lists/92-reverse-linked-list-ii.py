# https://leetcode.com/problems/reverse-linked-list-ii/description/
'''
Need to look into it again
'''
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        

        dummy = ListNode(0)
        dummy.next = head
        prevTemp = dummy

        # Move prevTemp to the node before left
        for _ in range(left - 1):
            prevTemp = prevTemp.next

        # Reverse the sublist
        curr = prevTemp.next
        prev = None
        for _ in range(right - left + 1):
            # Store next node
            nextt = curr.next
            # Reverse current link
            curr.next = prev
            # Move pointers
            prev = curr
            curr = nextt

        # Debugging
        print(prevTemp.val)
        print(prev.val)

        # Connect reversed part with the rest of the list
        prevTemp.next.next = curr
        prevTemp.next = prev

        return dummy.next