class Queue:

    def __init__(self):
    	self.items = []

	def peek(self):
		return self.items[0]

	def add(self, item):
		self.items.append(item)

	def remove(self):
		self.items.pop(0)

	def size(self):
		return len(self.items)

	def is_empty(self):
		return len(self.items) == 0

	def __str__(self):
		return str(self.items)
