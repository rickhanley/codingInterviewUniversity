#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<stdbool.h>

int main(void) {

    srand(time(0)); // seed srand with call to time. rand() now willbe differenr each run
    bool swaps = false;
    int counter = 0;

    int unsorted[1000]; // declare 10 element arrya
    for(int i = 0; i < 1000; i ++){ // fill array with 10 randome numbers
        unsorted[i] = rand() % 900;
    } 
    int array_length = sizeof(unsorted) / sizeof(unsorted[0]); // get array_length for loops
    int temp = 0; // variable to enable swapping

    for(int i = 0; i < array_length; i++) { // outer loop runs array_length times
    swaps = false; // reset the swaps to false. If we do a full run of the inner loop
                   // and this variable remains false it means no swaps have been made
                   // and therefore the array is already sorted so we can quit now.

        // inner loop REMEMBER any Moodifications to the index need to be reflected in 
        // how many times the loop runs. So j+1 index lookups in the body of the function
        // means the loop runs array_length - 1 times to avoid seg fault.
        // In this bubble sort the J loop starts at 0 and compares the next element, 1.
        // Then 1 vs 2, 2 vs 3 etc until array_length -1 = index 8 vs J + 1 = index 9
        // ALSO REMEMBER because Bubble sort moves the largest element to the right end of 
        // the array on each pass we don't need to check those numbers again. If the largest
        // number was in index 0, after just one pass the largest number WILL be in the 
        // far right position.
        // so for each iteration of the J loop we can decremement its iterations by i
        // meaning each time it runs it will run from 0 through to 8, then 7, 6 etc. 
        // The statements in the loop look at j + 1 meaning all elementa will be looked at
        // and will decrement properley to prevent seg faults.

        for(int j = 0; j < array_length - 1 - i; j++) { // inner loop runs 
            if(unsorted[j] > unsorted[j + 1]) {
                temp = unsorted[j + 1];
                unsorted[j + 1] = unsorted[j];
                unsorted[j] = temp;
                swaps = true;
                counter++;
            };
        };
        // break out of the loop here if no swaps made
        // i.e. after a completed run through of the 
        // inner "j" loop
        if (swaps == false) { 
            break;
            };
    };
    for(int i = 0; i < array_length; i++){
        printf("%d\n", unsorted[i]);
    };
    printf("Number of comparisons: %d\n", counter);
return 0;
};