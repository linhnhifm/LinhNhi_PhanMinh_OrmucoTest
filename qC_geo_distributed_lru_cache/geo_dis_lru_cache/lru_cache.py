from geo_dis_lru_cache import node
import time

class LRUCache:
    def __init__(self, capacity, expiration_time):
        self.cap = capacity
        self.cache = {}

        # left is Least Recently Used and right is Most Recently Used
        self.left, self.right = node.Node(0, 0), node.Node(0, 0)
        self.left.next, self.right.prev = self.right, self.left

        self.expiration_time = expiration_time

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev
    
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            if self.has_expired(node, self.expiration_time):
                self.remove(node)
                del self.cache[key]
                return -1
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = node.Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]

    def removeExpiredNodes(self):
        for key in list(self.cache.keys()):
            node = self.cache[key]
            if self.has_expired(node, self.expiration_time):
                self.remove(node)
                del self.cache[key]

    def has_expired(self, node, expiration_time):
        return time.time() - node.time_created > expiration_time
    
    def cache_size(self):
        return len(self.cache) 
    
    def getHead(self):
        return self.right.prev

    def getTail(self):
        return self.left.next