class LRU:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache = [None] * cache_size

    def insert(self, process):
        # 캐시에 해당 프로세스가 이미 존재하는 경우, 프로세스 제거 후 다시 삽입
        if process in self.cache:
            self.cache.remove(process)
        # 캐시에 해당 프로세스가 없고 캐시에 다른 프로세스가 꽉 차있다면, 가장 나중에 참조된 프로세스 제거
        elif len(self.cache) == self.cache_size:
            self.cache.pop()

        # 프로세스 추가
        self.cache.insert(0, process)

        print(self.cache)


if __name__ == '__main__':
    L = LRU(4)
    L.insert(1)
    L.insert(2)
    L.insert(3)
    L.insert(1)
    L.insert(4)
    L.insert(5)
