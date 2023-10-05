from geo_dis_lru_cache import lru_cache, geo_distributed_cache_manager
import unittest

class TestCacheManager(unittest.TestCase):
    def test_data_handling(self):
        # Some mock server coordinates
        server_coordinates = {
            'Server1': (37.7749, -122.4194), # San Francisco, USA
            'Server2': (51.5074, -0.1278), # London, UK
            'Server3': (48.8566, 2.3522), # Paris, France
            'Server4': (40.7128, -74.0060), # New York City, USA
            'Server5': (35.682839, 139.759455) # Tokyo, Japan
        }

        # Some mock data for users to request in data store
        data_store = {
            'Server1': {
                'Key1': 'Value1Server1',
                'Key2': 'Value2Server1',
                'Key3': 'Value3Server1',
            },
            'Server2': {
                'Key1': 'Value1Server2',
                'Key2': 'Value2Server2',
                'Key5': 'Value5Server2',
                'Key6': 'Value6Server2',
            },
            'Server3': {
                'Key1': 'Value1Server3',
                'Key2': 'Value2Server3',
                'Key3': 'Value3Server3',
            },
            'Server4': {
                'Key1': 'Value1Server4',
                'Key2': 'Value2Server4',
                'Key4': 'Value4Server4',
                'Key8': 'Value8Server4',
            },
            'Server5': {
                'Key1': 'Value1Server5',
                'Key2': 'Value2Server5',
            }
        }
        #Define LRU cache capacity and expiration time
        cache_capacity = 10
        cache_expiration_time = 60

        # Instantiate the GeoDistributedCacheManager 
        cache_manager = geo_distributed_cache_manager.GeoDistributedCacheManager(server_coordinates, data_store, cache_capacity, cache_expiration_time)

        # Mock user1's ip address and desired key to fetch
        user_ip_1 = '147.229.2.90' 
        key1 = 'Key1'  

        # Mock user2's ip address and desired key to fetch
        user_ip_2 = '192.168.0.1'
        key2 = 'Key2'

        # Handle user1's request
        data1 = cache_manager.handle_user_request(user_ip_1, key1)
        self.assertEqual(data1, 'Value1Server3')

        # Handle user2's request
        data2 = cache_manager.handle_user_request(user_ip_2, key2)
        self.assertEqual(data2, 'Value2Server1')

if __name__ == '__main__':
    unittest.main()