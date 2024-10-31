#include <stdio.h>

// halfs
// pass in an int and return the sizes of 2 arrays
// for mergesort algo. If 3 return 1 and 2, if 2


int main(void){

    int myarray[7] = {4,2,7,6,1,3,5};
    int array_size = sizeof(myarray) / sizeof(int);

    int left_half = array_size / 2;
    int right_half = array_size - left_half;

    
    printf("left half: %d\n", left_half);
    printf("right half: %d\n", right_half);

    return 0;
}