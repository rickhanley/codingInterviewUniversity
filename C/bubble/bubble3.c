#include<stdio.h>
#include<stdlib.h>
#include<time.h>

int main(void) {

    srand(time(0));

    int unsorted[5000];
    for(int i = 0; i < 5000; i ++){
        unsorted[i] = rand() % 500;
    }
    int array_length = sizeof(unsorted) / sizeof(unsorted[0]);
    int temp = 0;

    for(int i = 0; i < array_length; i++) { // outer loop
        for(int j = 0; j < array_length - 1 - i; j++) { // inner loop
            if(unsorted[j] > unsorted[j + 1]) {
                temp = unsorted[j + 1];
		unsorted[j + 1] = unsorted[j];
		unsorted[j] = temp;
            }
        }
    }
    for(int i = 0; i < array_length; i++){
        printf("%d\n", unsorted[i]);
    };
return 0;
}