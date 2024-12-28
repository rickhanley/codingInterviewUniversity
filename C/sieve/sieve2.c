#include <stdio.h>
#include <stdbool.h>
#include <math.h>

#define SIZE 1000000

int main(void){

    bool sieve_input[SIZE];
    for (int i = 0; i < SIZE; i++) {
        if (i == 0 || i == 1){
            sieve_input[i] = false;
        } 
        else {
        sieve_input[i] = true;
        }
    }

    // set up an array to check through

   

    int sieve_size = sizeof(sieve_input) / sizeof(bool);
    int max = sqrt(sieve_size);
    printf("max: %d\n", max);

    printf("sieve size: %d\n", sieve_size);

    for(int i = 2; i <= max; i+=1){
        // printf("Outer: %d\n", i);
        for(int j = i * i; j <= sieve_size; j+=i){
            // printf("    inner: %d\n", j);
                sieve_input[j] = false;
        };
    };

    for (int i = 0; i < sieve_size; i++){
        if(sieve_input[i] == true){
            printf("prime: %d\n", i);
        }
    }

    return 0;
}
