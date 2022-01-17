import os
from time import time
from random import randint

os.system("cls")



class Node:
   
    # Function to initialize the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.nextnode = None  # Initialize next as null
        self.backnode = None  # Initialize next as null


    def push(self, data):
        while self.nextnode != None:
            self = self.nextnode
        self.nextnode = Node(data)
        self.nextnode.nextnode = None
        self.nextnode.backnode = self

    def delete(self):
        if self.backnode == None:
            self = self.nextnode
            self.backnode = None
            return self
        
        if self.nextnode == None:
            self.backnode.nextnode = None
            self = None
            return
            
        self.backnode.nextnode = self.nextnode
        self.nextnode.backnode = self.backnode

    def print_nodes(self):
        while self.nextnode != None:
            self = self.nextnode
            print(self.data,end = " ")

    def print_rev_nodes(self):
        global begin
        global end
        while self.backnode != None:
            self = self.backnode
            print(self.data)
    


def list_del_neg(a):
    begin = a

    while a.nextnode != None:
        a = a.nextnode
        
        if (a.data<0):
            new_a = a.delete()
            if new_a != None:
                a = new_a

    if begin.data <0:
        begin = begin.nextnode
    
    return begin

def massive_del_neg(b):
    a = b.copy()
    it = len(a)-1
    while it>=0:
        if a[it]<0:
            del a[it]
        it -= 1
        
    
    return a
        
    
count = 10
print("count - > {}\n".format(count))


massive = [] #объявлем list
for i in range(count):
    massive.append(randint(-90,-9)) # добавляем в list

a = Node(massive[0]) # Объявляем список
for i in range(1,len(massive)):
    a.push(massive[i])



print(massive)
start_time = time()
massive = massive_del_neg(massive)
end_time = time()
print("massive delete for {} sec".format(end_time - start_time))
print(massive)
print("\n")


a.print_nodes() #выводим список
start_time = time()
a = list_del_neg(a)
end_time = time()
print("\nlist delete for {} sec".format(end_time - start_time))
if a:
    a.print_nodes() #выводим список


################





