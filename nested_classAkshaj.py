class Data:
      def __init__(self, data):
        self.usn=data[0]
        self.name=data[1]
        self.bday=data[2]
        self.pno=data[3]

class Node:
    def __init__(self,data):
        self.data=Data(data)
        self.next=None
    
        
class LinkedList:
    def __init__(self):
        self.head=None   #set head value for a linked list
    
    def __repr__(self):
        curr=self.head   #pointer to head, use to traverse ll
        print("USN\t\tName\t\tBirthday\t\tPhone Number")
        while curr is not None:
            print(curr.data.usn + "\t"+ curr.data.name + "\t\t"+ curr.data.bday + "\t\t" + curr.data.pno)
            curr=curr.next
        return ""
    
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

l1.head=Node(['1RF21CS009','Riddhi','11 June 2004','8080808080'])
e2=Node(['1RF21CS009','Akshaj','12 June 2003','9090909090'])
e3=Node(['1RF21CS010','Mithali','14 June 2005','7070707070'])
l1.head.next=e2
e2.next=e3

while(True):
    ch=int(input("Enter choice= "))
    if ch not in range(1,5):
        print("Unacceptable input")
    else:
        if ch==1:
            print(l1)
        elif ch==2:
            break