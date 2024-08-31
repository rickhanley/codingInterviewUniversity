#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}
node;

int main (int argc, char *argv[])
{

    if (argc !=2)
    {
        printf("Usage: ./linked number\n");
        return 1;
    }

   node *list = NULL; // implement a linked list of size 0

   printf("You entered: %d so I've created the nodes below at the addresses given:\n\n",argc);

   int i = 0;

   for (i = atoi(argv[1]); i >= 1; i--)
   {
        node *n = malloc(sizeof(node));
        if (n == NULL)
        {
            return 1;
        }
        else
        {
        printf("new pointer %d: %p\n", i, n);

        n->number = i;
        n->next = NULL;

        n->next = list;
        list = n;
        }
   }

    node *ptr = list;
    while (ptr != NULL)
    {
    ptr = ptr->next;
    }

    ptr = list;

    while (ptr != NULL)
    {
        node *next = ptr->next;
        free(ptr);
        ptr = next;
    }

    printf("\nlist: %ld\n", sizeof(list));
}