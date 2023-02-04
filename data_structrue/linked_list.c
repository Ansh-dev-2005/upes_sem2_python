//Demonstrate a program in C that will create and display Singly Linked List

#include <stdio.h>
#include <stdlib.h>

struct node
{
    int data;
    struct node *next;
};

struct node *head = NULL;
struct node *current = NULL;

//display the list
void printList()
{
    struct node *ptr = head;
    printf(" [head] =>");
    //start from the beginning
    while (ptr != NULL)
    {
        printf(" %d =>", ptr->data);
        ptr = ptr->next;
    }

    printf(" [null] n");
}

//insert link at the first location
void insertFirst(int data)
{
    //create a link
    struct node *link = (struct node*) malloc(sizeof(struct node));

    link->data = data;
    link->next = head;

    head = link;
}

//delete first item
struct node* deleteFirst()
{

    //save reference to first link
    struct node *tempLink = head;

    //mark next to first link as first
    head = head->next;

    //return the deleted link
    return tempLink;
}

//is list empty

int isEmpty()
{
    return head == NULL;
}

int length()
{
    int length = 0;
    struct node *current;

    for(current = head; current != NULL; current = current->next)
    {
        length++;
    }

    return length;
}

//find a link with given key
struct node* find(int data)
{

    //start from the first link
    struct node* current = head;

    //if list is empty
    if(head == NULL)
    {
        return NULL;
    }

    //navigate through list
    while(current->data != data)
    {

        //if it is last node
        if(current->next == NULL)
        {
            return NULL;
        }
        else
        {
            //go to next link
            current = current->next;
        }
    }

    //if data found, return the current Link
    return current;
}

//delete a link with given key
