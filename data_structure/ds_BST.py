class Node:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)


class BST:
    def __init__(self):
        self.root = None
        self.size = 0
        # self.height = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()  # self.root를 iterable한 객체로 만들어서 return 하는 건가 ?

    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None
        v = self.root
        while v:
            p = v
            if v.key < key:
                v = v.right
            else:
                v = v.left
        return p

    def insert(self, key):
        p = self.find_loc(key)
        if p == None or p.key != key:
            v = Node(key)
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        else:
            print("key is already in the tree")
            return p

    def deleteByMerging(self, x):
        a, b, pt = x.left, x.right, x.parent
        if a != None:
            c = a  # c는 x의 위치에 오게 될 Node
            m = a  # Left sub tree 에서 가장 큰 Node
            while m.right:
                m = m.right
            if b != None:
                b.parent = m
                m.right = b
        else:
            c = b

        if pt == None:
            self.root = c
            if c:
                c.parent = None
        else:
            if c:
                c.parent = pt
                if pt.key < c.key:
                    pt.right = c
                else:
                    pt.left = c
        self.size -= 1
