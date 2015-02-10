from priorityqueue import PriorityQueue

pq = PriorityQueue()

pq.add(5.3)
pq.add(5)
print str(pq)
pq.remove()
print str(pq)
pq.remove()
print len(pq)
print pq.is_empty()
pq.remove()