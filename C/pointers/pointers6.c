#include <stdio.h>

int adder (int *array){

    int length = sizeof(array);
    printf("length: %d\n", length);
    int running_total = 0;

    for (int i = 0; i < length + 1; i++){
        running_total += array[i];
    }

    return running_total;

}

int main(void){

    int my_array[] = {1,2,3,4,5};

    printf("%d\n", adder(my_array));

    return 0;
}