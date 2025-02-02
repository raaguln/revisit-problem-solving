# ------------------------------------------------
# Singly Linked List
# ------------------------------------------------
class SinglyLinkedNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

head = SinglyLinkedNode(1)

A = SinglyLinkedNode(2)
head.next = A

B = SinglyLinkedNode(3)
A.next = B

# Traverse the linked list and print
# Time: O(n)
# Space: O(1)
curr = head
while curr:
    print(curr.val)
    curr = curr.next

# Search for node
# Time: O(n)
# Space: O(1)
target = 3
curr = head
while curr:
    if curr.val == target:
        print("Found")
        break
    curr = curr.next


# ------------------------------------------------
# Doubly Linked List
# ------------------------------------------------
class DoublyLinkedNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

head = DoublyLinkedNode(1)
tail = DoublyLinkedNode(2)

head.next = tail
tail.prev = head


# Insert at head, return new head node
# Time: O(1)
# Space: O(1)
def insertAtBeginning(head, val):
    newNode = DoublyLinkedNode(val)
    newNode.next = head
    head.prev = newNode
    return newNode

# Insert at tail, return new tail node
# Time: O(1)
# Space: O(1)
def insertAtEnd(tail, val):
    newNode = DoublyLinkedNode(val)
    newNode.prev = tail
    tail.next = newNode
    return newNode

head = insertAtBeginning(head, 0)
insertAtEnd(tail, 3)

# Traverse the linked list and print
# Time: O(n)
# Space: O(1)
curr = head
while curr:
    print(curr.val)
    curr = curr.next