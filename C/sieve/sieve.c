// Sieve of Eratosthenes
// Start with all number except 0 and 1 labelled as prime
// with the aim of changing their flags to false by 
// elimination. Eliminate numbers by changing multiples 
// to false, i.e. look for all multiples of 2, mark false
// then muliples of 3 etc. If the number you are looking
// for is already marked false (e.g. 4, as this will be marked
// false as the second itartion when looking through multiples of
// 2 then don't look through the rest of the array.
// Also you only every need to look up to the SQUARE ROOT of the max
// value of the primes you are looking for, as the mutiples will
// have been removed for higher numbers


#include <stdio.h>
#include <stdbool.h>
#include <math.h>

int main(void){

    // set up an array to check through

    bool sieve_input[] = {false, false, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true, true};

    int sieve_size = sizeof(sieve_input) / sizeof(bool);
    int max = sqrt(sieve_size - 1);
    printf("max: %d\n", max);

    // int divisor = 2;

    printf("sieve size:%d\n", sieve_size);
    bool factor = false;

    // Outer loop gets a number to use as a factor
    // if this number is already marked false, continue
    for(int i = 2; i <= max; i ++){
        printf("top of loop i: %d\n", i);
        if(sieve_input[i] == false){
            continue;
        }
        if (factor == true){
            for(int j = i * 2; j < sieve_size; j += i){
                printf("%d\n", j);
                sieve_input[j] = false;
                printf("sieve_input[%d] marked as false\n", j);
            }
        }
        else{
            for(int j = i; j < sieve_size; j += i){
                printf("%d\n", j);
                sieve_input[j] = false;
                printf("sieve_input[%d] marked as false\n", j);
            }
        }
    }

    for (int i = 0; i < sieve_size; i++){
        if (sieve_input[i] == true){
            printf("i: %d is prime\n", i);
        }
        else{
            printf("i: %d is NOT prime\n", i);
        }
    };
return 0;
}