import time

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None
        self.time_created = time.time()