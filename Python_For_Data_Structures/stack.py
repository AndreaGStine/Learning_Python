class Stack:
    def __init__(self, items = []):
        self.items = items



    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

if __name__ == "__main__":
    s = Stack()
    print(s.is_empty())
    s.push(3)
    s.push('3')
    s.push('que')
    print(s.pop())
    print(s.peek())
    print(s.size())
