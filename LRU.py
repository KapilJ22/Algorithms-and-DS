class LRU_Cache(object):
    def __init__(self, capacity):
        # Initialize class variables
        self.cap = capacity

        #two dummy nodes created dummy and tail
        self.dummy = Node(None, None)
        self.dict = {}
        self.tail = Node(None, None)
        self.dummy.next = self.tail
        self.tail.prev = self.dummy

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.dict:
            return -1
        node = self.dict[key]

        # remove this node and insert back at front
        node.prev.next = node.next
        node.next.prev = node.prev
        val = node.val
        self.dict.pop(node.key, None)
        self.set(key, val)
        return val

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.

        # if key is present in the dict, remove this node from LL and dictionary (we will insert it later at front with the updated value)
        if key in self.dict:
            node = self.dict[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            val = node.val
            self.dict.pop(node.key, None)

        # remove node just before dummy tail from LL if capacity reached
        if len(self.dict) >= self.cap:
            self.dict.pop(self.tail.prev.key, None)
            self.tail.prev.prev.next = self.tail
            self.tail.prev = self.tail.prev.prev

        # insert node at front, after dummy head
        temp = self.dummy.next
        self.dummy.next = Node(key, value)
        self.dummy.next.prev = self.dummy
        self.dummy.next.next = temp
        temp.prev = self.dummy.next
        self.dict[key] = self.dummy.next


# declare node for double LL
class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None


our_cache = LRU_Cache(1)

our_cache.set(1, 2)
our_cache.set(2, 3)
our_cache.set(3, 4)
our_cache.set(4, 5)

print(our_cache.get(4)) 
our_cache.set(4, 8)
print(our_cache.get(4))  
print(our_cache.get(3))  
