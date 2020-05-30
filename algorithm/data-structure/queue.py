class Queue(list):
    def enqueue(self, element):
        self.append(element)

    def dequeue(self):
        self.pop(0)

    def is_empty(self):
        return not self

if __name__ == '__main__':
    q = Queue()

    q.enqueue(1)
    print(q)
    q.enqueue(2)
    print(q)
    q.enqueue(3)
    print(q)
    q.enqueue(4)
    print(q)

    q.dequeue()
    print(q)

