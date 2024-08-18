#include <stdio.h>
#include <math.h>

int main(void) {

    long max = 100000000; // check up to
    int divisor_count = 2; // every number after 1 must inherently be divisible by itself and 1
    long numbers_found = 0; // counter for number of primes found
    long upper_bound = 0;

    // Outer for loop. 
    // Provides the number i to check for primality
    // Since 1 is not included we start at 2
    for (int i = 2; i <= max; i ++){
        divisor_count = 2; // reset divisor count
        // printf("%d\n", i);
        // Inner for loop
        // Every number is divisible by 1 so start at 2
        // run whilst j is <= i / 2
        upper_bound = sqrt(i);
        for (int j = 2; j <= upper_bound; j++){
            // if modulo operation returns 0 increment divisor_count
            if(i % j == 0){
                divisor_count++;
                // as soon as we go over 2 break out to save 
                // useless comparisons
                if(divisor_count > 2){
                    break;
                } 
            }
        }
        // here we either have have checked every number up to the value
        // of i and divisor_remains at 2 OR we have broken out because 
        // divisor count was > 2
        // The if statement below captures the primes
        // and counts to toal primes found 
        if(divisor_count == 2) {
        // printf("%d is prime\n" , i);
        numbers_found++;
        }

    };
    printf("numbers found: %d", numbers_found);
};