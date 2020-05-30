class Stack(list):
    def push(self, element):
        self.append(element)

    def is_empty(self):
        return not self

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    print(s)
    s.push(2)
    print(s)
    s.push(3)
    print(s)
    s.push(4)
    print(s)
    s.pop()
    print(s)
    s.pop()
    print(s)
    s.pop()
    print(s)
    s.pop()
    print(s)
