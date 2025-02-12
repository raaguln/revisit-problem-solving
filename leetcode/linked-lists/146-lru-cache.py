class DoublyLinkedNode:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.leastRecent = DoublyLinkedNode(-1, -1)
        self.mostRecent = DoublyLinkedNode(-1, -1)
        self.leastRecent.right = self.mostRecent
        self.mostRecent.left = self.leastRecent
    
    def remove(self, node):
        prev, nextt = node.left, node.right
        prev.right = nextt
        nextt.left = prev
    
    def insert(self, node):
        prev, nextt = self.mostRecent.left, self.mostRecent

        prev.right = node
        node.left = prev

        self.mostRecent.left = node
        node.right = nextt

    def get(self, key: int) -> int:
        if key in self.cache:
            current = self.cache[key]
            self.remove(current)
            self.insert(current)
            return current.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        newNode = DoublyLinkedNode(key, value)
        self.cache[key] = newNode
        self.insert(newNode)
        if len(self.cache) > self.capacity:
            lru = self.leastRecent.right
            self.remove(lru)
            del self.cache[lru.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)