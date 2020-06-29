class EmptyError(Exception):
    pass

class Node:
        def __init__(self,value):
              self.info = value
              self.link = None

class Stack:

# ============================================================
# THIS IS VIA LIST 
# ============================================================
    
    def __init__(self):
        self.items = []
        
    def empty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)
    
    def push(self,item):
        self.items.append(item)
            
    def pop(self):
        if self.empty():
            raise EmptyError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def display(self):
        print(self.items)    

# ============================================================
# THIS IS VIA LINKED LIST
# ===========================================================

    def __init__ (self):
        self.top = None
          
    def is_empty(self):
        return self.top == None
    
    def size(self):
        if self.is_empty():
            return
        count = 0
        p = self.top
        while p is not None:
            p = p.link
            count += 1
        return count
    
    def push(self, data):
        temp = Node(data)
        temp.link = self.top
        self.top = temp
        
    def pop(self):
        if self.is_empty():
            return
        popped = self.top.info()
        self.top = self.top.link    
        return popped
    
    def peek(self):
        return self.top.info
    
    def display(self):
        if self.is_empty():
            print("List is Empty")
        
        p = self.top
        while p is not None:
            print(p.info, ' ', end=" ")
            p = p.link
                             
                          

if __name__ == "__main__":
    st = Stack()
    
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Size")
        print("5. Display")
        print("0. EXit")
        
        option = int(input("Enter your choice : "))
        
        if option == 1:
            x = int(input("Push your item : "))
            st.push(x)
        elif option == 2:
            st.pop()
        elif option == 3:
            print(st.peek()) 
        elif option == 4:
            print(st.size())
        elif option == 5:
            st.display()
        elif option == 0:
            break
        else:
            print("Wrong Choice")
        print()        
                
                       
        
        
        