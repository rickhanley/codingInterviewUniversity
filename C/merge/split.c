#include <stdio.h>


// take an array and recursive split it in half until
// we have length 1 
void splitter(int my_array[], int start, int end){

    if (end - start <= 0){
        return;
    };

    int mid = (start + end) / 2;

    int leftLength = mid - start + 1;
    int rightLength = end - mid;

    printf("Left half length: %d, Right half length: %d\n", leftLength, rightLength);

    splitter(my_array, start, mid);
    splitter(my_array, mid + 1, end);
}

int main(void){

    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15};
    int length = sizeof(arr) / sizeof(arr[0]);

    // Start splitting the array from index 0 to length-1
    splitter(arr, 0, length - 1);

    return 0;
}