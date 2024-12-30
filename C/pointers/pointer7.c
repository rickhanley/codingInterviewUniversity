#include <stdio.h>

int main(void){

    int *int_ptr;

    int number;

    int_ptr = &number;

    printf("pointer address: %p "    
            "address ptr is pointing to (number var):  %p," 
            "number : %p\n", &int_ptr, int_ptr, &number);

    return 0;
}