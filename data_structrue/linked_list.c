//Demonstrate a program in C that will create and display Singly Linked List

#include<stdio.h>
#include<stdlib.h>

struct node
{ 
    int num;
    struct node *nextptr;
}*stnode;

void createNodelist(int n);
void displaylist();

int main(){
    int n;
    printf("Enter the number of node \n");
    scanf("%d",&n);
    createNodelist(n);
    printf("Data entered in the list \n");
    displaylist();
    return 0;
}

void createNodelist(int n){
    struct node *fnNode, *tmp;
    int num, i;
    stnode = (struct node *)malloc(sizeof(struct node));
    if(stnode == NULL){
        printf("Memory can not be allocated");
    }else{
        printf("Enter the data for node 1: ");
        scanf("%d",&num);
        stnode->num = num;
        stnode->nextptr = NULL;
        tmp = stnode;
        for(i=2;i<=n;i++){
            fnNode = (struct node *)malloc(sizeof(struct node));
            if(fnNode == NULL){
                printf("Memory can not be allocated");
                break;
            }else{
                printf("Enter the data for node %d: ",i);
                scanf("%d",&num);
                fnNode->num = num;
                fnNode->nextptr = NULL;
                tmp->nextptr = fnNode;
                tmp = tmp->nextptr;
            }
        }
    }

}
void displaylist(){
    struct node *tmp;
    if(stnode == NULL){
        printf("List is empty");
    }else{
        tmp = stnode;
        while(tmp != NULL){
            printf("Data = %d\n",tmp->num);
            tmp = tmp->nextptr;
        }
    }
}
