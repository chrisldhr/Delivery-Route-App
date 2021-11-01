# Hash Map that stores data from csv files.

class HashMap:
    # Constructor initialization
    # Space-time complexity: O(1)
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    # Hash key creation
    # Space-time complexity: O(1)
    def _get_hash(self, key):
        return int(key) % self.size

    # Insertion of package data in to hash map
    # Space-time complexity: O(N)
    def add(self, key, value):
        key_hash = self._get_hash(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                 pair[1] = value
                 return True
            self.map[key_hash].append(key_value)
            return True

    # Look up of a single package
    # Space-time complexity: O(N)
    def get(self, key):
        key_hash = self._get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    # Update data of a single package
    # Space-time complexity: O(N)
    def update(self, key, value):
        key_hash = self._get_hash(key)
        if self.map[key_hash] != None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = value

    # Remove data of a single package
    # Space-time complexity: O(N)
    def delete(self, key):
        key_hash = self._get_hash(key)

        if self.map[key_hash] is None:
            return False
        for i in range (0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True
        return False


