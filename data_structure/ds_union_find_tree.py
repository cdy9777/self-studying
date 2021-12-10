class Node:
    def __init__(self, key):
        self.key = key
        self.parent = self
        self.rank = 0  # height


def make_set(x):
    return Node(x)


def find(x):
    while x.parent != x:
        x = x.parent

    return x


def union(x, y):
    v, w = find(x), find(y)
    if v.rank > w.rank:
        v, w = w, v
    v.parent = w

    if v.rank == w.rank:
        w.rank += 1
