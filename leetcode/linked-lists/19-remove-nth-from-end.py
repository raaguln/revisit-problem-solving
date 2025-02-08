'''
Time: O(n)
Space: O(1)
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        nodeToRemove = size - n + 1

        if nodeToRemove == 1:
            return head.next
        
        curr = head
        for i in range(1, nodeToRemove):
            if i == nodeToRemove-1:
                curr.next = curr.next.next
                break
            curr = curr.next
        return head
