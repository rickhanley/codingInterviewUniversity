// Prime factors
// Needs a loop to pre-pop say the first thousand primes.
// Given a number, divide it starting from the smallest prime(2)
// and look for 0 remainder. If 2 divides in with no remainder, 2
// is a prime factor. Now the given number is the number of times
// 2 divided into the original number. Keep going until the number
// 

#include <stdio.h>
#include <math.h>



int primes[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109,
113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173,179, 181, 191,
193,197,199,211,223,227,229,233,239,241,251,257,263,269,271,277,281,
283,293};
int prime_list_length = sizeof(primes) / sizeof(primes[0]);

int main(void){
    
    int given_n = 891;
    int calc_n = given_n;
    int factors[100] = {0};
    int fact_size = sizeof(factors) / sizeof(int);
    int counter = 0;
    int max = sqrt(given_n);
    int fact_index = 0;
    int total = 0;

    int result = 0;

    // printf("PLL: %d\n", prime_list_length);

    while (result != 1){
        for(int i = 0; i < prime_list_length; i++){
            // printf("i: %d\n", i);
            if (calc_n % primes[i] == 0){
                // printf("will look for: %d divided by %d\n", calc_n, primes[i]);
                // printf("Factor found position %d\n", i);
                factors[fact_index] = primes[i];
                fact_index ++;
                result = calc_n / primes[i];
                calc_n = result;
                break;
            }
        }
    }

    int start = factors[0];
    printf("prime factors of %d are:\n", given_n);
    for (int i = 1; i < fact_size; i++){
        if(factors[i - 1] != 0){
        printf("Prime factor %d: %d\n", i, factors[i-1]);
        }
       
        // printf("total: %d\n", start);
    }

    // printf("total: %d\n", start);

    return 0;
}