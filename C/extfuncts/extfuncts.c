#include <stdio.h>
#include "helpers.h"

int main(void){

    printf("Hello\n");
    
    int my_var = 0;

    printf("%d\n", my_var);

    printf("my_var at beginning: %d\n", my_var);
    counter(&my_var);
    printf("my_var at end: %d\n", my_var);
    return 0;
}
