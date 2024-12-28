#include <stdio.h>
#define RANGE 6

int main (void){

    // test array
    int test_arr[] = {6,2,5,3,4,1,2,1,2,1,2,4,3,5,6,5,4,3,4,5,
    6,7,6,5,4,5,6,7,8,7,6,5,6,7,8,7,6,7,8,9,8,7,8,8,7,5,4,3,4,
    5,6,7,5,4,3,3,54,5,4,4,4,4,4,4,5,5,5,5,6,7,6,5,4,3,2,1,2,3,
    4,4,3,1,2,3,4};
    // work out length of array
    int arr_length = sizeof(test_arr) / sizeof(int);

    // int lowest = test_arr[0];

    // outer loop - loops length of input array - 1 times
    // use the i to define the minIndex 
    // Outer loop really provides a seed value for the inner loop
    for (int i = 0; i < arr_length - 1; i++){
        // printf("i: %d\n", i);
        int minIndex = i; // minIndex is now 6
        // inner loop
        // inner loop always runs from i + 1 to the end
        // on each loop through it effectivley finds the lowest
        // value from the unsorted part of the array and moves it
        // fully to the left

        // j is set to one ahead of i, 2 in this case
        for (int j = i + 1; j < arr_length; j++){
            // loops over the remaining part of the array
            // finding the lowest of the remaining values
            if (test_arr[j] < test_arr[minIndex]){
                minIndex = j;
            }
        }
        // temp gets value from array at minIndex
        // test_arr[minIndex] now gets value at test_arr[i] (minIndex = j remember)
        // test_arr[i] now gest temp
        printf("swap happening\n");
        int temp = test_arr[minIndex];
        test_arr[minIndex] = test_arr[i];
        test_arr[i] = temp;
        // printf("comparing i + 1: %d and i: %d\n", test_arr[i + 1], test_arr[i]);
        // for(int j = 0; j < RANGE - 1; j++){
        //     if(test_arr[i + 1] < lowest){
        //     lowest = test_arr[i + 1];
        };  
        // print out the list
        for (int i = 0; i < arr_length; i++) {
            printf("%d ", test_arr[i]);
        }
        printf("\n");
    
        

    // printf("lowest: %d", lowest);
    return 0;
}