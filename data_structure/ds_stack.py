class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is Empty")

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")

    def __len__(self):
        return len(self.items)

    def is_empty(self):
        return len(self) == 0


parentheses = "(){}}{}{}[][][][])()))))"
s = Stack()
m = Stack()
l = Stack()

for par in parentheses:
    if par == "(":
        s.push(par)
    elif par == ")" and s.is_empty():
        print(False)
        exit()
    elif par == ")":
        s.pop()
    elif par == "[":
        m.push(par)
    elif par == "]" and m.is_empty():
        print(False)
        exit()
    elif par == "]":
        m.pop()
    elif par == "{":
        l.push(par)
    elif par == "}" and l.is_empty():
        print(False)
        exit()
    elif par == "}":
        l.pop()
    else:
        print("It's not parentheses!")

if s.is_empty() and m.is_empty() and l.is_empty():
    print(True)
else:
    print(False)
