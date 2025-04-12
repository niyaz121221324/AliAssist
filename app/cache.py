import time

class SimpleCache:
    def __init__(self, ttl=300):
        self.store = {}
        self.ttl = ttl

    def get(self, key):
        entry = self.store.get(key)
        if not entry:
            return None
        if time.time() - entry['time'] > self.ttl:
            del self.store[key]
            return None
        return entry['value']

    def set(self, key, value):
        self.store[key] = {
            'value': value,
            'time': time.time()
        }

cache = SimpleCache()
