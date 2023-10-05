from geo_dis_lru_cache import lru_cache
import unittest

class TestCache(unittest.TestCase):
    def test_lru_cache(self):
        cacheMemoryMaxSize = 5
        expiration_time = 60
        myCache = lru_cache.LRUCache(cacheMemoryMaxSize, expiration_time)

        # Insert key-value pairs into the cache
        myCache.put(1, "Value1")
        myCache.put(2, "Value2")
        myCache.put(3, "Value3")
        myCache.put(4, "Value4")
        myCache.put(5, "Value5")

        # Retrieve values from the cache
        value1 = myCache.get(1)
        value2 = myCache.get(2)
        self.assertEqual(value1, "Value1")
        self.assertEqual(value2, "Value2")

        # Check the cache size
        self.assertEqual(myCache.cache_size(), 5)

        # Check the cache order
        cache_order = []
        current_node = myCache.getTail()
        for i in range(myCache.cache_size()):
            cache_order.append(current_node.key)
            current_node = current_node.next
        
        # Left = Least recently used & Right = Most recently used
        self.assertEqual(cache_order, [3, 4, 5, 1, 2])
        self.assertEqual(myCache.getHead().val, 'Value2')
        self.assertEqual(myCache.getTail().val, 'Value3')

        # Remove expired nodes
        myCache.removeExpiredNodes()

if __name__ == '__main__':
    unittest.main()
