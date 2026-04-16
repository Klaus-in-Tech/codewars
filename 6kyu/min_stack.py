"""
Stack Min: How would you design a stack which, in addition to p u s h and pop, has a function m i n
which returns the minimum eiement? Push, p o p and m i n should ail operate in 0 ( 1 ) time.
"""

class min_stack():
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self,x):
        self.stack.append(x)
        if not self.minStack or x <= self.minStack[-1]:
            self.minStack.append(x)
        else:
            self.minStack.append(self.minStack[-1])
    
    def pop(self):
        if not self.stack:
            return
        self.stack.pop()
        self.minStack.pop()
        
    def peek(self):
        if not self.stack:
            return -1
        return self.stack[-1]
    def get_min(self):
        if not self.minStack:
            return -1
        return self.minStack[-1]
        

if __name__ == "__main__":
    st = min_stack()
    st.push(18)
    st.push(19)
    st.push(29)
    st.push(15)
    st.push(16)
 
    print(st.get_min())
   
    st.pop()
    print(st.get_min())
    st.pop()
    print(st.get_min())
    st.pop()
    print(st.get_min())
    st.pop()
    print(st.get_min())
    st.pop()
    print(st.get_min())