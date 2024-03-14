
class Node:
    class Data:
       def __init__(self,name,pno,city,email,bday):
        
        self.name=name
        self.pno=pno
        self.city=city
        self.email=email
        self.bday=bday
        self.next=None
        
    
       def __str__(self):
          dt=""
          while self.name is not None:
            dt+=str(self.name)+" "+str(self.pno)+" "+str(self.city)+" "+str(self.email)+" "+str(self.bday) #format with 3 tabspaces
            return dt
          
    def __init__(self,data):
        self.data=self.Data(data.name,data.pno,data.city,data.email,data.bday)
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

    def insertEnd(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        current_node=self.head
        while(current_node.next):
            current_node=current_node.next
        current_node.next=new_node
        new_node.next=None

    def searchcont(self,nm):   #traverse from front end
        if self.head is None:
            print("Contact directory is empty.")
            
        current_node=self.head
        if self.head==None:
            print("Directory empty")
        else:
            if current_node.data.name==nm:
                print("Contact found:")
                print("Name:", current_node.data.name)
                print("Phone Number:", current_node.data.pno)
                print("City:", current_node.data.city)
                print("Email:", current_node.data.email)
                print("Bday:", current_node.data.bday)
                return "" 
            else:
                print("Contact not found.")
                return ""
        

    def delete_contact(self, name):
        if self.head is None:
            print("Contact list is empty.")
            return

        if self.head.data.name == name:
            self.head = self.head.next
            print("Contact", name, "deleted successfully.")
            return

        prev = None
        current_node = self.head
        while (current_node and current_node.data.name)!=name: #basically loses the contact

            prev = current_node       #prev becomes current
            current_node = current_node.next   #current becomes next
        if current_node is None:
            print("Contact", name, "not found.")
            return

        prev.next = current_node.next
        print("Contact", name, "deleted successfully.")

    def display_contacts(self):
        current_contact = self.head
        while current_contact is not None:
            print("Name:", current_contact.data.name)
            print("Phone Number:", current_contact.data.pno)
            print("City:", current_contact.data.city)
            print("Email:", current_contact.data.email)
            print("Bday:", current_contact.data.bday)
            print("--------------------")
            current_contact = current_contact.next

#list1=[]
l1=LinkedList()       

while True:

    print("================================================\n")
    print("                 CONTACT DIRECTORY               \n")
    print("================================================\n")
    print("CHOICES:")
    print('''
        1. Enter new contact and details
        2. Delete existing contact
        3. Search for contact
        4. Display directory
        5. Exit''')
    print("================================================\n")  #3 tabspaces btwn each data field

    
    '''
    l1.head=Node(Node.Data('084','monday','4505853','sfivhj'))
    e2=Node(Node.Data('098','rid','25102004','mushroom'))
    e3=Node(Node.Data('43','gsfuissv','srg','w68394'))'''

    ch=int(input("Enter choice="))
    if ch not in range(1,6):
        print("Invalid choice, enter again")
        continue
     #returns to next execn of while loop
    if ch==1:    #name,pno,city,email,bday
        dn=str(input("Enter name= "))
        dpno=int(input("enter phoneno="))
        dcity=str(input("enter city="))
        dmail=str(input("enter email="))
        dbday=str(input("enter birthday="))
        l1.insertEnd(Node.Data(dn,dpno,dcity,dmail,dbday))
        #list1.append(Node.Data(dn,dpno,dcity,dmail,dbday))
        continue
    elif ch==2:
        nm=str(input("enter name of contact to delete="))
        l1.delete_contact(nm)
    elif ch==3:
        nm1=str(input("Enter contact to find="))
        l1.searchcont(nm1)
        continue
    elif ch==4:
        l1.display_contacts()
    elif ch==5:
        print("BAI")
        break





