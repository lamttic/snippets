class HashTable:
    def __init__(self, hash_size=8):
        self.hash_size = hash_size
        self.hash_table = [[] for _ in range(hash_size)]

    def hash_function(self, key):
        return key % self.hash_size

    def put(self, key, value):
        hash_value = self.hash_function(hash(key))
        bucket = self.hash_table[hash_value]

        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])

    def delete(self, key):
        hash_value = self.hash_function(hash(key))
        bucket = self.hash_table[hash_value]

        for idx in range(len(bucket)):
            if bucket[idx][0] == key:
                bucket.pop(idx)
                break

    def get(self, key):
        hash_value = self.hash_function(hash(key))
        bucket = self.hash_table[hash_value]

        for pair in bucket:
            if pair[0] == key:
                return pair[1]

        return None


if __name__ == '__main__':
    h = HashTable(4)
    print(h.hash_table)
    h.put('nike', '나이키')
    print(h.hash_table)
    h.put('adidas', '아디다스')
    print(h.hash_table)
    h.put('decente', '데상트')
    print(h.hash_table)
    print('조회', h.get('decente'))
    h.delete('decente')
    print(h.hash_table)
