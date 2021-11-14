class Heap:
    def __init__(self, L=[]):
        self.A = L
        self.make_heap()

    def __str__(self):
        return str(self.A)

    def heapify_down(self, k, n):  # n은 리스트 전체 노드 개수
        while 2*k + 1 < n:
            L, R = 2*k+1, 2*k+2
            if self.A[L] > self.A[k]:
                m = L
            else:
                m = k

            # R <= n일 것 같은 느낌.? > R은 리스트내 index니까 n보단 작아야함.
            if R < n and self.A[R] > self.A[m]:
                m = R

            if m != k:
                self.A[k], self.A[m] = self.A[m], self.A[k]
                k = m
            else:
                break

    def heapify_up(self, k):
        while k > 0 and self.A[(k-1)//2] < self.A[k]:
            self.A[k], self.A[(k-1)//2] = self.A[k], self.A[(k-1)//2]
            k = (k-1)//2

    def make_heap(self):
        n = len(self.A)
        for k in range(n-1, -1, -1):
            self.heapify_down(k, n)

    def heap_sort(self):
        n = len(self.A)
        for k in range(len(self.A)-1, -1, -1):
            self.A[0], self.A[k] = self.A[k], self.A[0]
            n = n-1
            self.heapify_down(0, n)

    def heap_insert(self, key):
        self.A.append(key)
        self.heapify_up(len(self.A)-1)

    def delete_max(self):
        if len(self.A) == 0:
            return 0
        key = self.A[0]
        self.A[0], self.A[len(self.A)-1] = self.A[(len(self.A)-1)], self.A[0]
        self.A.pop()
        self.heapify_down(0, len(self.A))
        return key


heap = Heap([2, 8, 6, 1, 10, 15, 3, 12, 11])

heap.heap_insert(7)
print(heap)
heap.delete_max()
print(heap)
heap.heap_sort()
print(heap)
