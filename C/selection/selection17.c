#include <stdio.h>

int main(void){
    int arr[]={4,2,8,3,6};
    int length = sizeof(arr) / sizeof(int);

    // start looping from 0 
    for(int i = 0; i < length; i++){
        int min = i;
        // inner loop j is always one ahead i.e. i + 1
        // arr[i] and arr[i + i] 
        // Also, inner loop check ALL numbers from i + 1 index
        // and may overwrite min numerous times as each time
        // arr[j] is lower, the if condition is true and the assignment
        // is made
        for(int j = i + 1; j < length; j++){
            // if arr[j] is less than the number at min (min == i - 
            // confusing!) then min needs to be j - Out of the
            // 2 numbers copmpared j is lower!
            if(arr[j] < arr[min]){
                min = j;
            }
        }

        // Now use a temp variable to facilitiate the swapping of
        // the values in the array - whatever the lowest index was
        // gets swapped out with whateevr is at arr[i]. The lowest
        // number is now in the correct place, the swapped highers 
        // number may get moved again later in the algo 
        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;

    }
    // loop over and print
    for(int i = 0; i < length; i++){
        printf("%d\n", arr[i]);
    }
}