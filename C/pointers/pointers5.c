#include <stdio.h>

int main() {

    int *my_ptr;
    int my_num = 9;
    my_ptr = &my_num;

    printf("my_ptr address: %p\n", (void*)&my_ptr); 
    printf("address inside my_ptr %p\n", my_ptr);
    printf("value pointed to %d", *my_ptr);

    return 0;
}
