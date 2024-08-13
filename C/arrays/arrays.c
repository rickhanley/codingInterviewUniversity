#include<stdio.h>

int main(void) {
    printf("Arrays\n");

    int my_array[] = {1, 2, 3, 4, 5};
    int new_array[5];

    printf("sizeof new_array: %d\n ", (sizeof(new_array) / sizeof(new_array[0])));

    printf("%d\n", my_array[0]);
    printf("%p\n", &my_array[0]);

    printf("%p\n", &my_array[0] + 1);

    printf("%d\n",sizeof(my_array[0]));
    printf("%d\n", sizeof(int));

    // store the address of my_array in an int pointer
    int *my_array_2_ptr = &my_array[0];

    // address of my_array_2_ptr
    printf("address of my_array_2_ptr: %p\n", my_array_2_ptr);

    // my_array_2_ptr functions as my_array with elements accessible with[]
    printf("element [1] of my_array_2_ptr: %d",my_array_2_ptr[1]);

    int *copied_array;
        

    return 0;
}