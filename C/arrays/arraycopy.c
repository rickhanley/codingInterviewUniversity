#include<stdio.h>
#
int main(void) {

    int initial_array[] = {1,2,3};

    int *copied_array = initial_array;

    printf("initial_array address: %p\n",&initial_array);
    printf("copied_array address: %p\n",&copied_array);
    printf("copied_array[0]: %d\n",copied_array[0]);

}