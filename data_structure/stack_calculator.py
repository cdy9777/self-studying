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

# 스택 계산기


# 1. infix > postfix
cal = "7+6+4+2*3/2/5"
operator = "+-*/()"
s = Stack()
outstack = []
for c in cal:
    if c in operator and len(s.items) == 0:
        s.push(c)
    elif c == ")":
        while s.top() != "(":
            outstack.append(s.pop())
        s.pop()
    elif (c == "+" or c == "-"):
        while s.top() == "*" or s.top() == "/":
            outstack.append(s.pop())
        s.push(c)
    elif c == "/" and (s.top() == "*" or s.top() == "/"):
        outstack.append(s.pop())
        s.push(c)
    elif c == "*" and s.top() == "/":
        outstack.append(s.pop())
        s.push(c)
    elif not c in operator:
        outstack.append(c)
    else:
        s.push(c)
while len(s.items) != 0:
    outstack.append(s.pop())

# 2. postfix > calculate
num = []
for out in outstack:
    if not out in operator:
        num.append(int(out))
    else:
        if out == "+":
            mid_num = num[-1] + num[-2]
        elif out == "-":
            mid_num = num[-1] - num[-2]
        elif out == "*":
            mid_num = num[-1] * num[-2]
        elif out == "/":
            mid_num = num[-2] / num[-1]
        for i in range(2):
            del num[-1]

        num.append(mid_num)

print(num[0])
