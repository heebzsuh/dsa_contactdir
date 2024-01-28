#include <stdio.h>
#include <stdlib.h>

struct contact
{
    char name[50];
    long int phone;
    char city[20]; // name, city, email, phone, birthday
    char email[50];
    char birthday[10];
    struct contact *next; //
};

typedef struct contact *cont;

cont head = NULL;
int elts = 0;

cont new()
{
    cont newcont;
    newcont = (cont)malloc(sizeof(struct contact));
    if (newcont == NULL)
    {
        printf("Memory is not available.");
        exit(1);
    }
    printf("Enter Name:\n");
    scanf("%s", newcont->name);
    printf("Enter Phone Number:\n");
    scanf("%ld", newcont->phone);
    printf("Enter city:\n");
    scanf("%s", newcont->city);
    printf("Enter email:\n");
    scanf("%s", newcont->email);
    printf("Enter birthday(DD/MM/YYYY):\n");
    scanf("%s", newcont->birthday);

    newcont->next = NULL;
    elts++;
    return newcont;
}

void fulldisplay()
{
    char req; // user input ofname required
    cont cur = head;
    int num = 1;
    if (head == NULL)
    {
        printf("No contacts saved.");
        exit(0);
    }
    while (cur->next != NULL)
    {
        printf("|%d|Name: %s\nPhone: %s\nCity: %ld\nEmail: %s\nBirthday: %s\n", num, cur->name, cur->phone, cur->city, cur->email, cur->birthday);
        cur = cur->next;
        num++;
    }
    printf("Total number of contacts saved=%d", (num - 1));
}

void display(int elt)
{
    char req; // user input of name required
    cont cur = head;
    int num = 1;
    printf("Enter Name of person=/n");
    scanf("%s", req);
    while (cur->name != req)
    {
        cur = cur->next;
        num++;
    }
    printf("Name: %s\nPhone: %s\nCity: %ld\nEmail: %s\nBirthday: %s\n", cur->name, cur->phone, cur->city, cur->email, cur->birthday);
}

// cont new()