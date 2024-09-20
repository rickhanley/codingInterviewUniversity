#include <stdio.h>

// factorial()
// recursive factorial definition
// INPUT: int
// OUTPUT: int

int factorial(int x){
    // base case
    if(x == 1){
        return 1;
    }
    // recursive case
    // since this is returning an expression with a fucntion call
    // it goes on the STACK.
    else {
        return x * factorial(x - 1);
    };
};

int main(void){

    int x = 8;

    printf("%d\n", factorial(x));

    return 0;
}