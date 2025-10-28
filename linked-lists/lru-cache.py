# Day 67: LRU Cache
# Problem Link: https://leetcode.com/problems/lru-cache/

from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        # Initialize an ordered dictionary to store key-value pairs
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        # If key not in cache, return -1
        if key not in self.cache:
            return -1
        # Move accessed key to the end (mark as most recently used)
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        # If key exists, move it to end and update
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        # If capacity exceeded, remove least recently used (first item)
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
