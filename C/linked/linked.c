// ****************************************************************************
// Singly Linked list implementation in C -
//
// This implementation adds items to the beginning of the list.
// As we add nodes, the new node becomew the first node in the list.
// Therefore if were adding sequential numbers, the last node in the
// list contains the LOWEST i.e. first number number added.
// 
// 
//
// Things to remember:
// 1. Use malloc and check it has assigned memory properley
// 2. Be aware a pointer's contents is an adress. So head in this context
//    will only point to nodes. THose nodes properties can be accessed with ->
// 3. -> means go to the address pointed at and acces the property
// 4. Be aware that this method is setting pointers to be NULL in some
//    instances and also checking if the pointed to node's next value is
//    NULL - it's easy to mix these concepts up 
// 5. if you use and change a pointer to the head you'll lose the head's
//    address. Store the head address and make copies as needed in temp
//    pointer vars
// 6. You MUST free memory when done with it
// 7. A head pointer == NULL means an empty list. We dont' delete the head
//    variable, but it being set to NULL means the list has length 0.
// 8. This implementation is adding nodes where the next pointer is really 
//     pointing "backwards" to the previously added node.
// ****************************************************************************

#include <stdio.h>
#include <stdlib.h>

// create a struct called node with typedef. Will hold only an int variable and
// a pointer remember - just declare the items but don't initialise them

typedef struct node {
    int number;
    struct node *next;
} node;

// *head is a ptr to my node. It is set to NULL initially
// so the list is techincally of zero lenght

node *head = NULL;
node *head_f = NULL;


int main(void){

    printf("sizeof(node)%d\n", sizeof(node));

    int list_length = 5;
    // for loop to create to some nodes, 5 in this case

    for(int i = 0; i < list_length; i++){
        // malloc the required number *n's using sizeof
        node *n = malloc(sizeof(node));
        // always check malloc hapened corrected
        if(n == NULL)
        {
            printf("Memory allocation error\n");
            return 1;
        }

        else
        {
            // for the instance of n set it's number var to get i
            n -> number = i + 1;
            // set it's next pointer to be NULL to initialise 
            // before immediately going on to do...
            n -> next = NULL;
            // n -> next now gets the pointer address at head
            // In the first loop this is NULL again. 
            n-> next = head;
            // now head get's the address of the node.
            // on the first pass it's now pointing to the first
            // node.
            head = n;
        }
        // list traversal
        printf("i: %d\n", i);
        printf("next: %p\n", n->next);
        printf("head: %p\n", head);
    }
    // loop to print the enirety of the list
    node *head_f = head;
    // while (head_f != NULL){
        // printf("contents of node: %d\n", head_f->number);
    //     head_f = head_f->next; 
    // }

    printf("head->number: %d\n", head->number);

    // loop to free memory

    // declare a temp pointer to hold addresses of our nodes
    node *temp = head;

    // whilst our temp pointer is NOT NULL i.e. not reached the last node
    while(temp != NULL){
        // copy the address of the next node into temp (copy pointer into 
        // pointer var)
        temp = head->next;
        // now free the memory address pointed to by the head node
        free(head);
        // now assign head the memory from temp which is the address of the
        // next node
        head = temp;
        // back to the top of the loop. temp may still not be NULL
        // so assigns temp the address from head-> next and loop again.
        // Let's say this IS the last loop iteration. So temp = head-> next 
        // assigns NULL
        // We free head and head now gets NULL meaning it DOESN'T point anywhere
        // So the memory is freed up. Head variable remains pointint to NULL
    }  

    if(head == NULL) {
        printf("Head is NULL. All is right with the world!\n");
    }
}

