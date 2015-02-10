from queue import Queue

q = Queue()

q.add(5)
q.add(True)
q.add('dog')
q.add([1,2,3])
q.add({'x':1, 'y':2})
q.add(5.3)
q.remove()
q.remove()
print q.size()
print q.is_empty()