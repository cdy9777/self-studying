class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, var):
        self.items.append(var)

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty!")
            return None
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x


# Josephus game
def Josephus(n, k):
    Q = Queue()
    for i in range(n):
        Q.enqueue(i+1)
    j = 0
    while Q.front_index != len(Q.items)-1:
        if j < k-1:
            p = Q.dequeue()
            Q.enqueue(p)
            j += 1
        else:
            Q.dequeue()
            j = 0
    return Q.items[-1]


print(Josephus(9, 3))
