#include <stdio.h>
#include <stdlib.h>

int main(void) {

    typedef struct node {
        int data;
        struct node *next;
    } node;

    node *head = NULL;
    node *temp;

    for (int i = 0; i < 10; i++){
        node *n = malloc(sizeof(node));
        if (n == NULL){
            printf("Memory allocation error\n");
        }

        n->data = i;
        n->next = head;
        head = n;
    }

    // temp = head;
    // while (temp != NULL){
    //     printf("%d\n", temp->data);
    //     temp = temp->next;
    // }

    temp = head;

    while(temp->data != 5){
        printf("%d\n", temp->data);
        temp = temp->next;
        printf("%d\n", temp->next->data);
    }

    while (head != NULL){
        printf("Freeing\n");
        temp = head->next;
        free(head);
        head = temp;
    };
    free(head);
}