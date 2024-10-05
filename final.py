from tkinter import *
import tkinter as tk
from tkinter import ttk


class Node:
    class Data:   #nested class
        def __init__(self, name, pno, city, email, bday):   #member initialization
            self.name = name
            self.pno = pno
            self.city = city
            self.email = email
            self.bday = bday 
            self.next = None   
        
        def __str__(self):   #predefined print fn, self=Node.Data
            return f"Name: {self.name}\n, Phone Number: {self.pno}\n, City: {self.city}\n, Email: {self.email}\n, Birthday: {self.bday}\n"

    def __init__(self, data):
        self.data = self.Data(data.name, data.pno, data.city, data.email, data.bday)
        self.next = None   #pointer init to None

class LinkedList:
    def __init__(self):   #only prop of ll is HEAD
        self.head = None

    def insertEnd(self, data):   
        new_node = Node(data)   
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:   #while curr node is True
                current_node = current_node.next
            current_node.next = new_node

    def delete_contact(self, name):    #deletion from front end, curr sstars from head
        if self.head is None:
            print("Contact list is empty.")
            return   

        if self.head.data.name == name:   
            self.head = self.head.next
            print("Contact", name, "deleted successfully.")
            return

        prev = None    
        current_node = self.head  
        while current_node and current_node.data.name != name:
            prev = current_node
            current_node = current_node.next

        if current_node is None:
            print("Contact", name, "not found.")
            return

        prev.next = current_node.next    #assign prev to the next of deleted node, cuz curr_node gets deleted
        print("Contact", name, "deleted successfully.")

    def searchcont(self, nm):
        if self.head is None:
            print("Contact directory is empty.")
            return

        current_node = self.head
        while current_node:
            if current_node.data.name == nm:
                print("Contact found:")
                return f"Name: {current_node.data.name}\n, Phone Number: {current_node.data.pno}\n, City: {current_node.data.city}\n, Email: {current_node.data.email}\n, Birthday: {current_node.data.bday}\n"
                
            current_node = current_node.next

        print("Contact not found.")

    def display_contacts(self):
        current_contact = self.head
        while current_contact:
            print(current_contact.data)
            print("--------------------")
            current_contact = current_contact.next

class ContactDirectoryApp(tk.Tk):   #tk.Tk is root window
    def __init__(self):
        super().__init__()   #no need of self when using super
        self.title('Contact Directory')
        self.geometry('600x700')  
        self.configure(bg="cyan3")

        self.entry = ttk.Entry(self, font=('Courier'), width=40)  

        title = Label(self, text='CONTACTS DIRECTORY', anchor=CENTER, font=("Century Schoolbook", 15),bg="cyan3")
        title.pack(pady=45) 

        self.tb_name = tk.Entry(self, width=50,bg="pink")
        self.tb_pno = tk.Entry(self, width=50,bg="pink")
        self.tb_city = tk.Entry(self, width=50,bg="pink")
        self.tb_email = tk.Entry(self, width=50,bg="pink")
        self.tb_bday = tk.Entry(self, width=50,bg="pink")

        Label(self, text="Name",bg="cyan3").place(x=70, y=120)
        self.tb_name.pack(padx=1, pady=2)
        Label(self, text="Phone no.",bg="cyan3").place(x=70, y=140)
        self.tb_pno.pack(padx=1, pady=2)
        Label(self, text="City",bg="cyan3").place(x=70, y=160)
        self.tb_city.pack(padx=1, pady=2)
        Label(self, text="Email",bg="cyan3").place(x=70, y=180)
        self.tb_email.pack(padx=1, pady=2)
        Label(self, text="Birthday",bg="cyan3").place(x=70, y=200)
        self.tb_bday.pack(padx=1, pady=2)

        self.l1 = LinkedList()    #init linkedlist inside app class so all memebers are native to class itself

        #BUTTONS
        btn_insert = Button(self, text='INSERT', bd='10', command=self.insert_button)
        btn_insert.pack(side=TOP, pady=5,fill=BOTH)

        btn_delete = Button(self, text='DELETE', bd='10', command=self.delete_button)
        btn_delete.pack(side=TOP, pady=5,fill=BOTH)

        btn_search = Button(self, text='SEARCH', bd='10', command=self.search_button)
        btn_search.pack(side=TOP, pady=5,fill=BOTH)

        btn_display = Button(self, text='DISPLAY ALL', bd='10', command=self.display_button)
        btn_display.pack(side=TOP, pady=5,fill=BOTH)

        btn_reset = Button(self, text='RESET', bd='10', command=self.reset_button)
        btn_reset.pack(side=TOP, pady=5,fill=BOTH)

        self.listbox = Listbox(self, width=90, height=20,bg="#BDFCC9")
        self.listbox.pack(pady=10)

    #functions of buttons call functions of linked list operations
    def insert_button(self):
        name = self.tb_name.get()   #get fetches single line string
        pno = self.tb_pno.get()
        city = self.tb_city.get()
        email = self.tb_email.get()
        bday = self.tb_bday.get()

        self.l1.insertEnd(Node.Data(name, pno, city, email, bday))
        self.reset_button()

    def delete_button(self):
        name = self.tb_name.get()
        self.l1.delete_contact(name)
        self.reset_button()      #calls another button function, reset


    def display_button(self):
        self.l1.display_contacts()

    def reset_button(self):
        self.tb_name.delete(0, 'end')   
        self.tb_pno.delete(0, 'end')
        self.tb_city.delete(0, 'end')
        self.tb_email.delete(0, 'end')
        self.tb_bday.delete(0, 'end')

    def display_button(self):
     self.listbox.delete(0, 'end')
     current_contact = self.l1.head
     while current_contact:
        contact_info = (
            f"Name: {current_contact.data.name}",
            f"Phone Number: {current_contact.data.pno}",
            f"City: {current_contact.data.city}",
            f"Email: {current_contact.data.email}",
            f"Birthday: {current_contact.data.bday}",
            "--------------------"
        )
        self.listbox.insert('end', *contact_info)
        current_contact = current_contact.next

    def search_button(self):
     name = self.tb_name.get()
     result = self.l1.searchcont(name)
     if result:
        self.listbox.delete(0, END)  # Clear the listbox
        contact_info = self.l1.searchcont(name)
        self.listbox.insert(END, contact_info)
     else:
        self.listbox.delete(0, END)
        self.listbox.insert(END, "Contact not found.")


if __name__ == "__main__":
    app = ContactDirectoryApp()
    app.mainloop()