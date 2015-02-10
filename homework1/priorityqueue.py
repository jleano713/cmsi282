class PriorityQueue:

# credit to Ray Toal for original Ruby implementation:
# http://cs.lmu.edu/~ray/notes/pqueues/

    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

    def is_empty(self):
        return len(self) == 0
    
    def peek(self):
        if self.is_empty():
            raise RunTimeError("Empty queue")
        return self.items[0]

    def sift_up(self, index):
        parent = (index - 1) / 2
        if parent >= 0 and self.items[parent] > self.items[index]:
            self.items[parent], self.items[index] = self.items[index], self.items[parent]
            self.sift_up(parent)

    def sift_down(self, index):
        child = (index * 2) + 1
        if child >= len(self.items):
            return
        if child + 1 < len(self.items) and self.items[child] > self.items[child + 1]:
            child += 1
        if self.items[index] > self.items[child]:
            self.items[child], self.items[index] = self.items[index], self.items[child]
            self.sit_down(child)

    def add(self, item):
        self.items.append(item)
        self.sift_up(len(self.items) - 1)

    def remove(self):
        if self.is_empty():
            raise RuntimeError("Empty queue")
        if len(self.items) == 1:
            self.items = []
        else:
            self.items[0] = self.items.pop()
            self.sift_down(0)
        

