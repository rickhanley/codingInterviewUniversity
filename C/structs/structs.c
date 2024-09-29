#include <stdio.h>


int main(void){
    typedef struct {
        int a;
        int b;
    } MyStruct;
;
    MyStruct my_struct;

    my_struct.a = 1;
    my_struct.b = 2;

    printf("Initial value: %d\n", my_struct.a);

    my_struct.a = 10;
    my_struct.b = 20;

    printf("Updated value: %d\n", my_struct.a);
    printf("Updated value: %d\n", my_struct.b);
  
};