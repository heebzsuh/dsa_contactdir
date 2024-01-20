class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None   #set head value for a linked list
    def listprint(self):
        printval=self.head   
        while printval is not None:
            print(printval.data)
            printval=printval.next

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

while(True):
    ch=int(input("Enter choice= "))
    if ch not in range(1,5):
        print("Unacceptable input")
    else:
        if ch==1:
            l1.listprint()
        elif ch==2:
            








'''list1=LinkedList()
list1.head=Node('monday')
e2=Node('tue')
e3=Node('wed')

list1.head.next=e2
e2.next=e3

list1.listprint()'''




