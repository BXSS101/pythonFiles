"""
class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return (999999999, 0)
    def size(self):
        return len(self.items)
    def count(self, c):
        return self.items.count(c)
"""
text = input('Enter Input : ').split(',')
tree = []
for i in range(len(text)):
    if len(text[i].split()) == 2:
        sp = text[i].split()
        h = int(sp[1])
        tree.append(h)
    else: 
        count = 0
        highest = -1
        for j in range(len(tree)-1, -1, -1):
            if tree[j] > highest:
                highest = tree[j]
                count += 1
        print(count)