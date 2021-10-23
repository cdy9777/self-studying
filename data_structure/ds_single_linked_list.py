# 한방향 linked_list
# push_front, pop_front는 시간복잡도 O(1), push_back, pop_back의 시간복잡도는 O(n)
class Node:
    def __init__(self, key=None):
        self.key = None
        self.next = None

    def __str__(self):
        return str(self.key)


class Singly_linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def push_front(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = key
        self.size += 1

    def push_back(self, key):
        new_node = Node(key)
        if len(self) == 0:
            self.head = new_node
        else:
            tale = self.head
            while tale.next != None:
                tale = tale.next
            tale.next = new_node

        self.size += 1

    def pop_front(self):
        if len(self) == 0:
            return None
        else:
            x = self.head
            key = x.key
            self.head = key.next
            self.size -= 1
            del x
            return key

    def pop_back(self):
        prev, tale = None, self.head
        while tale.next != None:
            prev = tale
            tale = tale.next

        if len(self) == 1:
            key = self.head.key
            self.head = None
            self.size = 0
            return key
        else:
            prev.next = None
            key = tale.key
            del key
            self.size -= 1
            return key

    def search(self, key):
        v = self.head
        while v != None:
            if v.key == key:
                return v
            v = v.next
        return None

    # Generator (__iterator__라는 special method를 가진 객체는 for loof 구문에서 사용 가능하다.)
    def __iterator__(self):
        v = self.head
        while v != None:
            yield v
            v = v.next
