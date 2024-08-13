#include<stdio.h>

int main(void) {

    int my_int = 8;
    int *my_pointer = &my_int;

    printf("my_int address: %p, my_pointer address: %p\n", &my_int, my_pointer);
    printf("my_int value: %d, my_pointer value: %d\n", my_int, *my_pointer);

    int new_var = 100; // declare a variable
    int *new_var_ptr = &new_var; // new_var_ptr gets THE ADDRESS of the new_var
    printf("new_var_ptr stores address: %p\nnew_var_ptr address pointed to holds this value: %d\naddress of the original var: %p", new_var_ptr, *new_var_ptr, &new_var);
    
    return 0;
};