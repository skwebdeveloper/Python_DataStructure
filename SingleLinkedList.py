print("================================================")


class Node:
    def __init__(self, value):
        self.info = value
        self.link = None


class SingleLinkedList:
    def __init__(self):
        self.start = None
#   DISPLAYING

    def display_list(self):
        if self.start is None:
            print("List is Empty")
            return
        else:
            print("List is: ")
            p = self.start
            while p is not None:
                print(p.info, " ", end='')
                p = p.link
            print()
#  COUNTING

    def Count_list(self):
        if self.start is None:
            print("Count is Zero")
            return
        else:
            p = self.start
            count = 0
            while p is not None:
                
                 
                p = p.link
                count += 1
            print(count)
#  SEARCHING

    def Searching_list(self, x):
        position = 1
        p = self.start
        while p is not None:
            if p.info == x:
                print(position)
                return True
            position += 1
            p = p.link
        else:
            print("Not found")
            return False

# INSERTION
# ===============================================
# INSERT AT BEGINNING 
# ===============================================

    def insert_beginning(self, data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp

# ===============================================
# INSERT AT END
# ===============================================
    def insert_end(self, data):
        temp = Node(data)
        if self.start is None:
             self.start = temp
             return 
        p = self.start
        while p.link is not None:
                 p = p.link
        p.link = temp


    def create_list(self):
            n = int(input("Enter number of Nodes : "))
            if n == 0:
                return
            for i in range(n):
                data = int(input("Enter element : "))
                self.insert_end(data)
# ===============================================
# INSERT IN BETWEEN THE NODES
# ===============================================
    
    def insertion_after(self,data,x):
        p = self.start
        while p is not None:
            if p.info == x:
                break
            p = p.link
        if x is None:
            print("X is not in list") 
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
                   
            
    def insertion_before(self,data,x):
        if self.start is None:
            print("Empty")
            return
        
        if self.start.info == x:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
        p = self.start
        while p.link is not None:
            if p.link.info == x:
                break
            p = p.link    
        if p.link is None:
            print("Not present")
        else:
            temp = Node(data)
            temp.link = p.link
            p.link = temp
 
 
 
    def insertion_at_position(self,data,k):
        if k == 1:
            temp = Node(data)
            temp.link = self.start
            self.start = temp
            return
        i = 1
        p = self.start
        while i<k-1 and p is not None:
            p = p.link
            i += 1
        if p is None:
            print("Not Found") 
        else:
            temp = Node(data)
            temp.link = p.link 
            p.link = temp
                  
            
                           






# ===============================================
# MAIN DECLARATION
# ===============================================

list = SingleLinkedList()
list.create_list()

while True:
    print("1. Display List")
    print("2. Count List")
    print("3. Search List")
    print("4. Insert Beginning")
    print("5. Insert End")
    print("6. Insertion After")
    print("7. Insertion Before")
    print("19. Quit")
    option = int(input("Enter your choice : "))
    if option == 1:
        list.display_list()
    elif option == 2:
        list.Count_list()
    elif option == 3:
        data = int(input('Enter your searching data : '))
        list.Searching_list(data)
    elif option == 4:
        data = int(input('Insert Beginning data : '))
        list.insert_beginning(data)
    elif option == 5:
        data = int(input('Insert Lastdata : '))
        list.insert_end(data)
    elif option == 6:
        data = int(input("Enter number to be added ")
        x = int(input("Enter number after which you want to add "))
        list.insertion_after(data,x)  
    elif option == 7:    
        data = int(input('Enter number to be added : '))
        x = int(input('Enter number before which you want to add : '))
        list.insertion_after(data,x)               
        
    elif option  == 19:
        break
    else:
        print("Wrong choice")
    print()


print("================================================")
