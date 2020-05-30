class FIFO:
    def __init__(self, cache_size):
        self.cache_size = cache_size
        self.cache = [None] * cache_size

    def insert(self, process):
        # 이미 해당 프로세스가 캐시에 존재하지 않는 경우만 처리
        if process not in self.cache:
            # 캐시에 프로세스가 가득차면 가장 처음에 삽입된 프로세스 제거
            if len(self.cache) == self.cache_size:
                self.cache.pop()

            # 프로세스 추가
            self.cache.insert(0, process)

        print(self.cache)


if __name__ == '__main__':
    F = FIFO(4)
    F.insert(1)
    F.insert(2)
    F.insert(3)
    F.insert(1)
    F.insert(4)
    F.insert(5)
