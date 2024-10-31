#include <stdio.h>

int receiver(int *a, int *array, char *string){

    int length = sizeof(array);

    printf("%d\n",a);
    for (int i = 0; i < length; i++){
        printf("Array[%d] = %d\n", i, array[i]);
    };
    printf("String: %s\n", string);

    printf("a before: %d\n", *a);

    *a = 10;

    printf("a after: %d\n", *a);

    return 0;
}

int main(void){

    int my_num = 0;
    int my_array[]={1,2,3,4,5};
    char *my_string = "Rick";

    receiver(&my_num, my_array, my_string);
    // printf("my_num: %d\n", *my_num);
}