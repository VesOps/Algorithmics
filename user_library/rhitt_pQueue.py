class pQueue:
    # pQueue constructor (operation)
    def __init__(self, min_heap=True):
        self.heap = []      # python lists [] are dynamic arrays of pointers to data
        self.min_heap = min_heap
        self.size = 0

    # helper functions
    def parent(self, i):
        return (i - 1) // 2
    
    def children(self, i):
        return (2*i + 1, 2*i + 2)

    def swap(self, i, j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp

    def compare(self, i, j):
        # out of bounds check
        if i < self.size:
            a = self.heap[i][0]
        else:
            return False
        if j < self.size:
            b = self.heap[j][0]
        else:
            return True

        return a <= b if self.min_heap else a >= b
    

    # standard operations
    def enqueue(self, priority, data):
        # store them together
        node = (priority, data)
        self.heap.append(node)
        self.size += 1

        # restore the heap property
        i = self.size - 1      # index of current node - start at end
        while i > 0:
            parent = self.parent(i)
            if self.compare(parent, i):
                break   # heap property is satisfied
            else:
                self.swap(i, parent)
            i = parent
        
        return self
        
    def dequeue(self):
        if self.isEmpty():
            return None     # nothing to dequeue
        
        # replace root with last dangling leaf node (no strings attached)
        self.heap[0] = self.heap[self.size-1]
        self.heap[self.size-1] = None
        self.size -= 1

        # restore heap property by iteratively swapping out violations
        i = 0   # index of current node - start at root
        while True:
            left, right = self.children(i)
            if left >= self.size:   # reached end, so finished
                break

            violation = i   # value of i is sentinel indicating NO violation
            if self.compare(left, i):
                violation = left
            if right < self.size and self.compare(right, violation):
                violation = right

            if violation == i:      # no violation
                break
            else:                   # resolve violation
                self.swap(i, violation)
                i = violation

        return self
    
    def front(self):
        if self.isEmpty():
            return None
        return self.heap[0]
    
    def isEmpty(self):
        return self.size == 0