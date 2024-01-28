
class Node:
    class Data:
       def __init__(self,usn,name,bday,pno):
        self.usn=usn
        self.name=name
        self.bday=bday
        self.pno=pno
    
       def __str__(self):
          dt=""
          while self.usn is not None:
            dt+=str(self.usn)+" "+str(self.name)+" "+str(self.bday)+" "+str(self.pno)
            return dt
          
    def __init__(self,data):
        self.data=self.Data(data.usn,data.name,data.bday,data.pno)
        self.next=None
       
       
class LinkedList:
    def __init__(self):
        self.head=None   #set head value for a linked list
    
    def __str__(self):
        LL=""
        curr=self.head   #pointer to head, use to traverse ll
        while curr is not None:
            print(curr.data)
            curr=curr.next
        #LL+=str(curr.data)
        return LL
    
    ''' def listprint(self):
        printval=self.head   #head is of data type node
        while printval is not None:
            print(printval.data)
            printval=printval.next'''

    def insertEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next
        current_node=current_node.next

print("================================================\n")
print("                 CONTACT DIRECTORY               \n")
print("================================================\n")
print("CHOICES:")
print('''
      1. Display directory
      2. Enter new contact and details
      3. Delete existing contact
      4. Display chosen contact
      5. Exit''')
print("================================================\n")

l1=LinkedList()

l1.head=Node(Node.Data('084','monday','4505853','sfivhj'))
e2=Node(Node.Data('098','rid','25102004','mushroom'))
e3=Node(Node.Data('43','gsfuissv','srg','w68394'))

#l1.head.next=e2
#e2.next=e3

while True:
    ch=int(input("Enter choice= "))
    if ch not in range(1,5):
        print("Unacceptable input")
    else:
        if ch==1:
            print(l1)
        elif ch==2:
            break














