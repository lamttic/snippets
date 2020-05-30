class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head:
            current_node = self.head

            while current_node.next:
                current_node = current_node.next

            current_node.next = Node(data)
        else:
            self.head = Node(data)

    def display(self):
        current_node = self.head
        print(current_node.data)

        while current_node.next:
            current_node = current_node.next
            print(current_node.data)

    def delete(self, data):
        current_node = self.head

        if current_node.data == data:
            next_node = self.head.next

            if next_node:
                self.head = next_node

            del current_node
        else:
            while current_node.next:
                next_node = current_node.next

                if next_node.data == data:
                    if next_node.next:
                        current_node.next = next_node.next
                    else:
                        current_node.next = None
                    break

                current_node = current_node.next


if __name__ == '__main__':
    l = LinkedList(1)
    l.display()
    l.add(2)
    l.display()
    l.add(3)
    l.display()
    l.delete(3)
    l.display()
