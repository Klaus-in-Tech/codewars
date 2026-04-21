class ThreeStacks:
    def __init__(self, cap=2):
        # cap = size per stack (default 2)
        self.cap = cap
        # total array size = cap * 3
        self.items = [None] * (cap * 3)

        # start indices for stack 0, 1, 2
        self.start = [0, cap, 2 * cap]

        # end indices (exclusive) for each stack
        self.end = [cap, 2 * cap, 3 * cap]

    def push(self, stack, val):
        # stack is 0, 1, or 2
        if self.start[stack] >= self.end[stack]:
            raise IndexError(f"Stack {stack} is full")
        self.items[self.start[stack]] = val
        self.start[stack] += 1

    def pop(self, stack):
        if self.start[stack] == self.end[stack] - self.cap:  # start at original position?
            # Actually better: check if stack is empty
            if self.start[stack] == self.end[stack] - self.cap:
                raise IndexError(f"Stack {stack} is empty")
        # move top index back by 1
        top = self.start[stack] - 1
        item = self.items[top]
        self.items[top] = None
        self.start[stack] = top
        return item

    def peek(self, stack):
        if self.start[stack] == self.end[stack] - self.cap:
            raise IndexError(f"Stack {stack} is empty")
        return self.items[self.start[stack] - 1]

    def is_empty(self, stack):
        return self.start[stack] == self.end[stack] - self.cap
        

if __name__ =="__main__":
    three_stack = ThreeStacks()
    three_stack.push(0,2)
    three_stack.push(0,5)
    print(three_stack.peek(0))
    three_stack.push(1,2)
    three_stack.push(1,5)
    three_stack.push(2,"A")
    three_stack.push(2,"B")
    print(three_stack.pop(2))