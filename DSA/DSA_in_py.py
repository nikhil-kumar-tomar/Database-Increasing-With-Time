# def bubbsort(low,high,array):
#     l=0
#     while True:
#         for x in range(0,len(array)-1):
#             if array[x]>array[x+1]:
#                 array[x],array[x+1]=array[x+1],array[x]
#                 l+=1
#         if l==0:
#             break
#         l=0
#     return array
# lis=bubbsort(0,2,[10,5,23])
# print(lis)

# def sortt(array,l):
#     if l==len(array)-1:
#         return array
#     else: 
#         for x in range(len(array)-1):
#             if array[x]>array[x+1]:
#                 array[x],array[x+1]=array[x+1],array[x]
#         sortt(array,l+1)
#     return array


# Quicksort First element as pivot

# def piv_index(low,high,lis):
#     pivot=lis[low]
#     i=low+1
#     for j in range(low+1,high+1):
#         if lis[j]<pivot:
#             lis[i],lis[j]=lis[j],lis[i]
#             i+=1
#     lis[low],lis[i-1]=lis[i-1],lis[low]
#     print(lis,lis[low:high],i-1)
#     return i-1
               
# def quicksort(low,high,lis):
#     if low<high:
#         los=piv_index(low,high,lis)
#         quicksort(low,los,lis)
#         quicksort(los+1,high,lis)    
#         return lis
# lis=[35,50,15,25,80,23,52]
# print(quicksort(0,6,lis))


# Quicksort First element as pivot

# def piv_index(low,high,lis):
#     pivot=lis[low]
#     i=low+1
#     for j in range(low+1,high+1):
#         if lis[j]<pivot:
#             lis[i],lis[j]=lis[j],lis[i]
#             i+=1
#     lis[low],lis[i-1]=lis[i-1],lis[low]
#     return i-1
               
# def quicksort(low,high,lis):
#     if low<high:
#         los=piv_index(low,high,lis)
#         quicksort(low,los-1,lis)
#         quicksort(los+1,high,lis)    
#         return lis
# lis=[35,50,15,25,80,23,52]
# print(quicksort(0,6,lis))



# Quicksort last element as pivot

# def piv_index(low,high,lis):
#     pivot=lis[high]
#     i=high-1
#     for j in range(high-1,low-1,-1):
#         if lis[j]>pivot:
#             lis[i],lis[j]=lis[j],lis[i]
#             i-=1
#     lis[high],lis[i+1]=lis[i+1],lis[high]
#     return i+1
               
# def quicksort(low,high,lis):
#     if low<high:
#         los=piv_index(low,high,lis)
#         quicksort(low,los-1,lis)
#         quicksort(los+1,high,lis)    
#         return lis
# lis=[35,50,15,25,80,23,52]
# print(quicksort(0,6,lis))


# # Quicksort median element as pivot

# def bubbsort(low,high,array):
#     l=0
#     while True:
#         for x in range(0,len(array)-1):
#             if array[x]>array[x+1]:
#                 array[x],array[x+1]=array[x+1],array[x]
#                 l+=1
#         if l==0:
#             break
#         l=0
#     return array

# def median(low,high,lis):
#     mid=(low+high)//2
#     lim=[lis[low],lis[mid],lis[high]]
#     lim=bubbsort(0,2,lim)
#     for x in [low,high,mid]:
#         if lis[x]==lim[1]:
#             return x

# def piv_index(low,high,lis):
#     #Taking the median 
#     mid=median(low,high,lis)
#     lis[mid],lis[0]=lis[0],lis[mid]
#     pivot=lis[low]
#     i=low+1
#     for j in range(low+1,high+1):
#         if lis[j]<pivot:
#             lis[i],lis[j]=lis[j],lis[i]
#             i+=1
#     lis[low],lis[i-1]=lis[i-1],lis[low]
#     return i-1
               
# def quicksort(low,high,lis):
#     if low<high:
#         los=piv_index(low,high,lis)
#         quicksort(low,los-1,lis)
#         quicksort(los+1,high,lis)    
#         return lis
# lis=[35,50,15,25,80,23,52]
# print(quicksort(0,6,lis))


# Merge Sort

# def mergesort(array):
#     if len(array)<=1:
#         return array
#     mid=len(array)//2
#     left=mergesort(array[:mid])
#     right=mergesort(array[mid:])

#     return merge(left,right)

# def merge(left, right):
#     output=[]
#     i=j=0

#     while (i<len(left) and j<len(right)):
#         if left[i] < right[j]:
#             output.append(left[i])
#             i+=1
#         else:
#             output.append(right[j])
#             j+=1

#     output.extend(left[i:])
#     output.extend(right[j:])

#     return output

# print(mergesort([5,3,2,1,6]))
# from sklearn.ensemble import IsolationForest 


# Tower of hanoi
# 3 pegs and 3 discs

# lis=[[3,2,1],[],[]]

#  Tower of hanoi
# def hanoi(discs,start,aux,end):
#     if discs==1:
#         print(f"{start}->{end}")
#     else:
#         hanoi(discs-1,start,end,aux)
#         print(f"{start}->{end}")
#         hanoi(discs-1,aux,start,end)

# hanoi(2,0,1,2)

# Linked list
# class Node():
#     def __init__(self,data):
#         self.data=data
#         self.next=None
# class linked_list():
#     def __init__(self):
#         self.head=None
    
#     def add_node(self,data):
#         new_node=Node(data)
#         if self.head is None:
#             self.head=new_node
#         else:
#             current=self.head
#             while current.next:
#                 current=current.next
#             current.next=new_node
#     def display(self):
#         current=self.head
#         while current:
#             print(current.data)
#             current=current.next

# my_lis=linked_list()
# my_lis.add_node(5)
# my_lis.add_node(10)
# my_lis.add_node(15)
# my_lis.display()


# Nice LInked LIst for automatic making

# class Node:
#     def __init__(self) -> None:
#         self.data = None
#         self.ptr = None

#     def __str__(self):
#         return f"{self.data} -> {self.ptr}"

# def make_node(head: object, number_of_items: int):
#     for iterator in range(number_of_items+1):
#         newnode = Node()
#         newnode.data = iterator

#         if head == None:
#             head = newnode
#         else:
#             current = head
#             while current.ptr != None:
#                 current = current.ptr
#             current.ptr = newnode
#     return head

# head = None
# head = make_node(head,331)
# print(head)

# def fibonacci(n):
#     if n==0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n-1) + fibonacci(n-2)
# print(fibonacci(20))

# BST Below:
# class Node:
#     def __init__(self) -> None:
#         self.data = None
#         self.right = None
#         self.left = None

#     def __str__(self):
#         return f"{self.data}->{self.left.data}\n{self.data}->{self.right.data}"

# def inorder_traverse(root):
#     result = []
#     if not root:
#         return result
#     else:
#         result += inorder_traverse(root.left)
#         result.append(root.data)
#         result += inorder_traverse(root.right)
#         return result

# def preorder_traverse(root):
#     result = []
#     if not root:
#         return result
#     else:
#         result.append(root.data)
#         result += preorder_traverse(root.left)
#         result += preorder_traverse(root.right)
#         return result

# def postorder_traverse(root):
#     result = []
#     if not root:
#         return result
#     else:
#         result += postorder_traverse(root.left)
#         result += postorder_traverse(root.right)
#         result.append(root.data)
#         return result


# def append_node(head, value):
#     newnode = Node()
#     newnode.data = value

#     prev_node = None
#     current = head
#     while(current != None):
#         if (newnode.data < current.data):
#             prev_node = current
#             current = current.left
#         elif (newnode.data > current.data):
#             prev_node = current
#             current = current.right
#         else:
#             print("Don't Test me MR.TOMAR")
#             return
    
#     if newnode.data > prev_node.data:
#         prev_node.right = newnode
#     elif newnode.data < prev_node.data:
#         prev_node.left = newnode
#     else:
#         head = newnode


# ob1 = Node()

# ob1.data = 2

# while True:
#     choice = int(input("Enter your choice: "))
#     if choice == 1:
#         break
#     elif choice == 2:
#         num = int(input("Enter your number: "))
#         append_node(ob1, num)
#     elif choice == 3:
#         traverse_choice = int(input("Enter your traverse choice: "))
#         if traverse_choice == 1:
#             print(preorder_traverse(ob1))
#         elif traverse_choice == 2:
#             print(inorder_traverse(ob1))
#         elif traverse_choice == 3:
#             print(postorder_traverse(ob1))

# --------------------------------------------------------------    

# TREE with many children Below
# class Node:
#     def __init__(self) -> None:
#         self.data = None
#         self.child = []

#     def __str__(self, level = 0):
#         ret = "\t" * level + f"{self.data}" + "\n"
        
#         for child in self.child:
#             ret += child.__str__(level + 1)
#         return ret
    
# def get_node(node, node_data):
#     num = None
#     if node.data == node_data:
#         num = node
    
#     for child in node.child:
#         if not num:
#             num = get_node(child, node_data)
#     return num

# def traverse(node):
#     array=[]
#     array += [node.data]
#     if node.child:
#         for childs in node.child:
#             array += traverse(childs)
#     return array

# def add_child(node, node_data, value):
#     newnode = Node()
#     newnode.data = value

#     current = get_node(node, node_data)
#     if current:
#         current.child.append(newnode)
#     return current

# ob1 = Node()
# ob2 = Node()
# ob3 = Node()
# ob4 = Node()
# ob1.data = 1
# ob2.data = 2
# ob3.data = 3
# ob4.data = 4
# ob1.child.append(ob2)
# ob2.child.append(ob4)
# ob1.child.append(ob3)


# print(add_child(ob1, 3, 9))
# print(ob1)
# traverse(ob1)

# Circular queue

# class Node:
#     def __init__(self) -> None:
#         self.data = None
#         self.next = None
#     def __str__(self) -> str:
#         return f"{self.data} -> {self.next.data}"

# class CircularQueue:
#     def init_queue(self):
#         self.head = Node()
#         new_head = self.head
#         for iter in range(self.size-1):
#             newnode = Node()
#             new_head.next = newnode
#             new_head = new_head.next
#             if iter == self.size - 2:
#                 new_head.next = self.head

#     def __init__(self,size):
#         self.tail_index = self.head_index = -1
#         self.size = size
#         self.init_queue()
        
#     def enqueue(self, element):
#         if self.head_index == -1:
#             self.head_index += 1
#             self.tail_index += 2
#             self.head.data = element
#         else:
#             newhead = self.head
#             for iter in range(self.head_index, self.tail_index):
#                 newhead = newhead.next
#             newhead.data = element
#             self.tail_index += 1
#     def dequeue(self):
#         self.head_index += 1
#         self.head = self.head.next

#     def print_queue(self):
#         newhead = self.head
#         for iter in range(self.head_index, self.tail_index):
#             print(newhead.data)
#             newhead = newhead.next 

# queue = CircularQueue(5)
# newhead = queue.head
# queue.print_queue()


# Stack using Linked List

# class Node:
#     def __init__(self) -> None:
#         self.data = None
#         self.next = None
#     def __str__(self) -> str:
#         return f"{self.data} -> {self.next}"


# class Stack:
#     def __init__(self, size) -> None:
#         self.size = size
#         self.head_index = -1
#         self.head = None
    
#     def is_full(self):
#         if self.head_index == self.size -1:
#             return True
#         return False
    
#     def is_empty(self):
#         if self.head_index == -1:
#             return True
#         return False
    
#     def push(self, element):
#         if self.head_index == -1:
#             self.head = Node()
#             self.head.data = element
#             self.head_index += 1
#         elif not self.is_full():
#             newnode = Node()
#             newnode.data = element
#             newnode.next = self.head
#             self.head = newnode
#             self.head_index += 1
#         else: 
#             print("Stack is Full")

#     def pop(self):
#         if not self.is_empty():
#             temp = self.head
#             self.head = self.head.next
#             del temp  
#             self.head_index -= 1
#         else:
#             print("Stack Is empty")

#     def print_stack(self):
#         current = self.head
#         while current is not None:
#             print(current.data)
#             current = current.next

# stack = Stack(5)
# stack.push(1)
# stack.push(2)
# stack.push(3)
# stack.push(4)
# stack.push(5)
# stack.pop()
# stack.print_stack()


# Heapsort Max Heap

def max_heapify(arr, N, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < N and arr[left] > arr[largest]:
        largest = left
    if right < N and arr[right] > arr[largest]:
        largest = right
    
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, N, largest)

def min_heapify(arr, N, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < N and arr[left] < arr[largest]:
        largest = left
    if right < N and arr[right] < arr[largest]:
        largest = right
    
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]
        min_heapify(arr, N, largest)


def heap_sort(arr:list, size:int, type_of_heapsort:str):

    if type_of_heapsort.lower() == "max":
        heap_function = max_heapify
    elif type_of_heapsort.lower() == "min":
        heap_function = min_heapify
    else:
         return f"{type_of_heapsort} is not applicable, choose between \"min\" and \"max\""

    for largest in range(size//2 - 1, -1, -1):
        heap_function(arr, size, largest)

    array = []
    for element in range(size-1, -1, -1):
        arr[element], arr[0] = arr[0], arr[element]
        array.append(arr.pop())

        heap_function(arr, len(arr), 0)

    return array

arr = [4, 5, 3, 10, 1, 6, 9]
size = len(arr)

print(heap_sort(arr=arr, size=len(arr), type_of_heapsort="max"))
