#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>
#include<math.h>


int main(void){

long next_j(long array_size, long start, bool *primes);
long last = 0;

long array_size = 100000000; // find primes up to this number
long upper_bound = 0; // variable to control loop iterations
long total_primes = 0; // count of total primes found
long result = 0;

bool *primes = malloc(sizeof(bool) * array_size); // allocate memory bools

// check 
if(primes == NULL) {
    printf("malloc didn't happen\n");
}
else 
{
    printf("malloc ok\n");
};

for(long i = 0; i < array_size; i++) {
        primes[i] = i < 2 ? false : true;
};

// 

// upper_bound ****************************************************
// run the outer loop this many times.


upper_bound = sqrt(array_size);
printf("upper_bound: %d\n", upper_bound);

// Remember the outer loop seeds the inner loop with an appropriate
// number. We run to sqrt(array_size) because as the loops run we
// are knocking out non primes from our array. For each number
// seeded into the inner loop, we  square it (j = i * i)  to begine with
// This is because all smaller prime factors have already been knocked out
// by previous numbers. I.e. 2 has already dealt with 2,4,6,8,10,12,14,16 etc etc
// So when we get to 4 it's fine to start at 4 * 4 = 16  2 gives 4,6,8,10 etc. 3 gives 9,12,
// Consider an array 1 to 10 to check for primalirty.
// Our array setup sets
// 1 and 2 as prime (technically 1 isn't prime).
// and then our inner loop picks up with j = i * i = 4 in this case.
// So 4, then 6, then 8 get made false. 


for(long i = 2; i <= upper_bound; i++){
    last = next_j(array_size, i, primes);
    i = last;
    // printf("i: %d\n", i);
    for(long j = i * i; j < array_size; j += i){
        // printf("j: %d\n", j);
        if(primes[j] != false) {
            (primes[j] = false);
        };
        
    };
    // for(int i = 0; i < array_size; i++){
    //         printf("prime listing: %d position: %d\n", primes[i], i);
    //     };
};

for(int i = 0; i < array_size; i++) {
    if(primes[i] == true){
        total_primes++;                
    }
    // printf("number: %d  T/F:  %d\n",i, primes[i]);
};
// printf("Total primes: %d\n", total_primes);
// primes[99] = false;

printf("total primes: %ld\n", total_primes);

free(primes); 
return 0;
}

long next_j(long array_size, long start, bool *primes){
    // printf("Array size: %d\n", array_size);
    // printf("Primes: %p\n", primes);
    for(long i = start; i < array_size; i++ ){
        if(primes[i] == true){
            // printf("next prime: %d", i);
           return i;
        };
    };
};