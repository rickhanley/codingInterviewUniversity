#include <stdio.h>

int main(void){

    int *ptr;

    int x = 0;

    ptr = &x;

    printf("%d\n", *ptr);
    printf("%p\n", ptr);
    printf("%d\n", x);
    printf("%p\n", &x);
}