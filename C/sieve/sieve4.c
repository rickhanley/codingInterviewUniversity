#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>

void sieve_of_eratosthenes(int limit) {
    int sqrt_limit = (int)sqrt(limit);
    int array_size = (limit / 2) + 1; // Only track odd numbers
    bool *is_prime = calloc(array_size, sizeof(bool));

    // Initialize the array
    for (int i = 1; i < array_size; i++) {
        is_prime[i] = true; // Assume all odds are prime
    }

    // Sieve process (start from 3, only check odd indices)
    for (int i = 1; i <= sqrt_limit / 2; i++) {
        if (is_prime[i]) {
            int p = 2 * i + 1; // Map back to the actual prime (2n + 1)
            for (int j = (p * p) / 2; j < array_size; j += p) {
                is_prime[j] = false;
            }
        }
    }

    // Print primes (handle 2 separately, then all odd primes)
    printf("2\n"); // 2 is the only even prime
    for (int i = 1; i < array_size; i++) {
        if (is_prime[i]) {
            printf("%d\n", 2 * i + 1);
        }
    }

    free(is_prime);
}

int main(void) {
    int limit = 1000000; // Change this for larger ranges
    sieve_of_eratosthenes(limit);
    return 0;
}