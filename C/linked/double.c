#include <stdio.h>
#include <stdlib.h>

typedef struct node {
    int data;
    struct node *next;
    struct node *prev;
} node;

int print_list(node *ptr);

int node_insertion(int find_this, node *temp);

int main (void){

    node *head = NULL;
    int list_length = 11;

    for(int i = 0; i < list_length; i++){

        node *n = malloc(sizeof(node));
        if(n == NULL){
            printf("malloc failed\n");
            return 1; 
        }

        // we have created a node n
        // n-> data gets i
        n->data = i + 1;
        // n-> next gets the head value (NULL on first)
        n->next = head;
        // n->prev gets NULL each iteration
        n->prev = NULL;
        // if the head is not NULL i.e. must be on iteration > 0
        // head-> AND THIS IS THE KEY PART --
        // head-> is pointing to last n, so head->prev = n
        // means: 1. go where head is pointing i.e. last n
        //        2. update the property prev in n with n
        //           which is now not NULL
        // 
        if (head != NULL) {
            head->prev = n;  // Update the previous head's `prev` to point to the new node
            // printf("%p\n", head->prev);
        }
        // NOW we update head with new n address.
        head = n;
    }
    
    node *temp = head;

    
    print_list(temp);
    
    temp = head; // reset temp back to head address
// specify node to find
// new node will be added numerically above this
    int find_this = 7;

    for(int i = 0; i < 10; i++){
        node_insertion(i + 1, temp);
    };
    // for(int i = 0; i < 10; i++){
    //     node_insertion(i + 1, temp);
    // };
// find node of a certain data value
    

    temp = head;

    print_list(temp);

    while(temp != NULL){
        temp = head->next;
        free(head);
        head = temp;
    };

    if(head == NULL) {
        printf("Head is NULL. All is right with the world!\n");
    };
   
}

int print_list(node *ptr) {

    while(ptr != NULL){
    printf("node data: %d  next: %p prev: %p\n", ptr->data, ptr->next, ptr->prev);
    ptr = ptr->next;
    }
    return 0;
    
};

int node_insertion(int find_this,node * temp){
    while(temp->data != find_this){
        temp = temp->next;
        if(temp->data == find_this){
            printf("Found! @ %p\n", temp);
        };
    };
// create new node
     node *n = malloc(sizeof(node));
        if(n == NULL){
            printf("Error with malloc");
            return 1;
        }

        printf("temp data = %d\n", temp->data);
        printf("temp next->data: %p\n", temp->prev->data);
        printf("n addres: %p\n", n);
// insert node between the fund node and it's previous
// previous in this context means it's higher number.
        n->prev = temp->prev;
        n->next = temp;
        n->data = 1000;
        printf("n prev: %p\n", n-> prev);
        printf("n next: %p\n", n-> next);
        temp->prev->next = n;
        temp->prev = n;
        printf("temp next: %p\n", temp-> next); // pointd to 8
        // printf("temp next->data: %d\n", temp-> next->data); // pointd to 8
        // printf("temp prev: %p\n", temp-> prev->next); // pointd to 6

};