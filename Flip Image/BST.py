import time
import random

class Node : 
    def __init__(self): #constructor
        self.Nodedata = None
        self.Left = None
        self.Right = None

head = None

def sorted_list(): 
    global head 
    n = NodeCount(head) 
    return recurrence(n) 

def recurrence(n): 
    global head 
    
    if (n <= 0) : 
        return None

    Left = recurrence( int (n / 2)) 

    root = new_node((head).Nodedata) 
    root.Left = Left 
    head = (head).next
    root.Right = recurrence( n - int (n / 2) - 1) 

    return root 

def NodeCount(head) : 

    count = 0
    temp = head 
    while(temp != None): 
        temp = temp.next
        count = count + 1
    
    return count 

def push(head, new_Nodedata) : 

    new_node = Node() 

    new_node.Nodedata = new_Nodedata 
    new_node.next = (head) 
    (head) = new_node 

    return head 
    
def new_node(Nodedata) : 

    node = Node() 

    node.Nodedata = Nodedata 
    node.Left = None
    node.Right = None

    return node 

def preOrd( node) : 

    if (node == None) : 
        return
    print(node.Nodedata, end = " " ) 
    preOrd(node.Left) 
    preOrd(node.Right) 

def leaf_node( node): 
    current = node 
  
    while(current.Left is not None): 
        current = current.Left  
  
    return current 

def deleteFunc(root, Nodedata): 
  
    if root is None: 
        return root  
   
    if Nodedata < root.Nodedata: 
        root.Left = deleteFunc(root.Left, Nodedata) 
 
    elif(Nodedata > root.Nodedata): 
        root.Right = deleteFunc(root.Right, Nodedata) 

    else: 
        if root.Left is None : 
            temp = root.Right  
            root = None 
            return temp  
              
        elif root.Right is None : 
            temp = root.Left  
            root = None
            return temp 
   
        temp = leaf_node(root.Right) 

        root.Nodedata = temp.Nodedata 
        root.Right = deleteFunc(root.Right , temp.Nodedata) 
  
  
    return root

# Driver code 
head = None

t1 = time.time()
for i in range(0 , 10):
    head = push(head, i)

root = sorted_list() 
t2 = time.time()

print("OUTPUT :")
print("\nTime taken for 2000 elements in array A[] (ascending order)")
print(f"  {t2 - t1} seconds")
print(f"  {(t2 - t1)*1000000} microseconds")

t1 = time.time()
for i in range(0 , 4000):
    head = push(head, i)

root = sorted_list() 
t2 = time.time()
print("\nTime taken for 4000 elements in array A[] (ascending order)")
print(f"  {t2 - t1} seconds")
print(f"  {(t2 - t1)*1000000} microseconds")

t1 = time.time()
for i in range(0 , 6000):
    head = push(head, i)

root = sorted_list() 
t2 = time.time()
print("\nTime taken for 6000 elements in array A[] (ascending order)")
print(f"  {t2 - t1} seconds")
print(f"  {(t2 - t1)*1000000} microseconds")

t1 = time.time()
for i in range(0 , 8000):
    head = push(head, i)

root = sorted_list() 
t2 = time.time()
print("\nTime taken for 8000 elements in array A[] (ascending order)")
print(f"  {t2 - t1} seconds")
print(f"  {(t2 - t1)*1000000} microseconds")

t1 = time.time()
for i in range(0 , 10000):
    head = push(head, i)

root = sorted_list() 
t2 = time.time()
print("\nTime taken for 10000 elements in array A[] (ascending order)")
print(f"  {t2 - t1} seconds")
print(f"  {(t2 - t1)*1000000} microseconds")
