#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *higher;
    struct node *lower;
} node;


int main(void){

    int list_length = 10;
    node *head = NULL;

    for(int i = list_length; i >=1; i--){
        node *n = malloc(sizeof(node));
        n-> data = i;
        n-> higher = head;
        n-> lower = NULL;
        // Key thing to remember with this if:
        // on entry to each loop it is pointing to the last node
        // so when we check the condition and update the 
        // head -> lower, we're saying "go where heas is pointing,
        // (the last node) and update it's lower value with the address
        // of n."
        if(head != NULL) {
            head-> lower = n;
        }
        head = n;
        printf("head address @ i: %d    address: %p\n", i, head);
    }

    node *temp = head;
    printf("head address: %p\n", head);
    printf("should match.....\n");
    printf("temp address: %p\n", temp);

    while(temp != NULL){
        printf("Data: %d\n",temp->data);
        temp = temp->higher;
    }

    temp = head;
    node *delete_node;
    while(temp != NULL) {
        // printf("1. temp: %p    head: %p\n", temp, head);
        temp = head->higher;
        // printf("2. temp: %p    head: %p\n", temp, head);
        free(head);
        head = temp;
        // printf("3. temp: %p    head: %p\n", temp, head);
    }

    printf("temp: %p, head %p\n", temp, head);

    return 0;
}