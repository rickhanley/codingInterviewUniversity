// Selection sort
// Outer loop really just provides a seed to the inner loop
// Out loop runs the size of the input array -1 times
// inner loop loops over all unsorted elements size of array -1 times
// when the inner loop runs each time, all it does is find the lowest number in the
// unosrted part of the array.  


#include <stdio.h>

int main(void){

    int my_arr[] = {2,4,1,3};

    int arr_length = sizeof(my_arr) / sizeof(my_arr[0]);
    printf("arr_length: %d\n", arr_length);

    for (int i = 0; i < arr_length - 1; i++){
        int min = i;
        printf("top of loop i: %d\n");
        for (int j = i + 1; j < arr_length; j++){
            printf("%d vs %d\n", my_arr[j] , my_arr[i]);
            if(my_arr[j] < my_arr[min]){
                min = j;
                printf("min: %d\n", min);
            } 
        }
        int temp = my_arr[min];
        printf("temp: %d\n", temp);
        my_arr[min] = my_arr[i];
        my_arr[i] = temp;
        // printf("i %d\n:", i);
    }

    for(int i = 0; i < arr_length; i++){
        printf("%d", my_arr[i]);
    }
    // printf("%n");

    return 0;
}
