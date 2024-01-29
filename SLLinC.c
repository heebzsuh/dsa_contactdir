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

cont start = NULL;
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
    scanf("%s", &newcont->name);
    printf("Enter Phone Number:\n");
    scanf("%ld", &newcont->phone);
    printf("Enter city:\n");
    scanf("%s", &newcont->city);
    printf("Enter email:\n");
    scanf("%s", &newcont->email);
    printf("Enter birthday(DD/MM/YYYY):\n");
    scanf("%s", &newcont->birthday);

    newcont->next = NULL;
    elts++;
    return newcont;
}

cont insert_back(){
    cont temp;
    temp=new();
    if(start==NULL)
    {return temp;}
     temp->next=start;
    return temp;
}




void fulldisplay()
{
    // user input ofname required
    cont cur = start;
    int num = 1;
    if (start == NULL)
    {
        printf("No contacts saved.");
        exit(0);
    }
    while (cur->next != NULL)
    {
        printf("|%d|Name: %s\nPhone: %s\nCity: %ld\nEmail: %s\nBirthday: %s\n", num, *cur->name, cur->phone, *cur->city, *cur->email, *cur->birthday);
        cur = cur->next;
        num++;
    }
    printf("Total number of contacts saved=%d\n", (num - 1));
}

void display(char nm)
{

    cont cur = start;
    int num = 1;
    printf("Enter name of required contact= "); // user input of name required
    scanf("%s", &nm);
    while (cur->name != nm)
    {
        cur = cur->next;
        num++;
    }
    printf("Name: %s\nPhone: %s\nCity: %ld\nEmail: %s\nBirthday: %s\n", *cur->name, cur->phone, *cur->city, *cur->email, *cur->birthday);
}

int main()
{

    int i, n, ch;
    char nm;
    while (1)
    {
        printf("-----MENU-----");

        printf("\n1. Create contact");
        printf("\n2. Display all contacts");
        printf("\n3. Display entered name's contact");

        printf("\nEnter choice= ");
        scanf("%d", &ch);

        switch (ch)
        {
        case 1:
            printf("enter no of contacts= ");
            scanf("%d", &n);
            for (i = 0; i < n; i++)
            {
                start = new ();
                insert_back(start);
            }
            break;
        case 2:
            fulldisplay();
            break;
        case 3:

            display(nm);
        default:
            return 1;
        }
    }
}
