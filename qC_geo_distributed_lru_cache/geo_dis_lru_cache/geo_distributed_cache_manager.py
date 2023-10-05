from geo_dis_lru_cache import lru_cache
from math import radians, sin, cos, sqrt, atan2
import geocoder 
import random

class GeoDistributedCacheManager:
    def __init__(self, server_coordinates, data_storage, capacity, expiration_time):
        self.server_coordinates = server_coordinates
        self.caches = {server: lru_cache.LRUCache(capacity=capacity, expiration_time=expiration_time) for server in server_coordinates}
        self.data_storage = data_storage
    
    # Handle a user request for their desired key based on their IP address
    def handle_user_request(self, user_ip, key):
        closest_server = self.determine_closest_server(user_ip)

        # Check if the data is in the cache, or fetch it from the database
        if key in self.caches[closest_server].cache:
            data = self.caches[closest_server].get(key)
        else:
            data = self.fetch_data_from_database(key, closest_server)
            self.caches[closest_server].put(key, data)

        return data

    # Determine the closest server based on user's IP
    def determine_closest_server(self, user_ip):
        user_location = geocoder.ip(user_ip).latlng
        if not user_location:
            print("User location not available. Using default server.")
            return 'Server1'
        else:
            closest_server = min(self.server_coordinates, key=lambda server: self.haversine(user_location, self.server_coordinates[server]))
        return closest_server

    # Haversine formula to calculate distance between two coordinates
    def haversine(self, coord1, coord2):
        earth_radius = 6371.0

        lat1 = radians(coord1[0])
        lon1 = radians(coord1[1])
        lat2 = radians(coord2[0])
        lon2 = radians(coord2[1])

        dlon = lon2 - lon1
        dlat = lat2 - lat1

        # Haversine formula
        a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = earth_radius * c
        return distance

    # Fetch data from data store if there is no data in cache
    def fetch_data_from_database(self, key, server):
        if key in self.data_storage[server]:
            return self.data_storage[server][key]
        else:
            # If data doesn't exist in the database, generate some data
            data = self.generate_data(key)
            self.data_storage[server][key] = data
            return data
        
    # Generate random data for a given key
    def generate_data(key):
        random_integer = random.randint(1, 100)
        random_data = 'RandomValue'.join(random_integer)
        return f"{key}: {random_data}"
