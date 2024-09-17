// ************************* FACTORIAL - RECURSION ****************************
// 
//  Factorial solution using recursion
//
// ****************************************************************************


#include <stdio.h>

// ***********************Recursive function "fact"****************************
// INPUT: integer
// output: integer
//
// When called the function takes the integer x. If the intger is not 1, i.e.
// NOT the base case it returns X + the result of fact(x-1)
//
// let's say x is 3:
// fact(3) checks for base case: false, therefore return x(3) + result of
// fact(x-1) = fact(2). Check for base case: false, therefore return result
// of fact(x-1) = fact(1). Check for base case: true therefore return 1. 
// Now the program works through the function calls on the stack.
//
// Last call is 1
// previous to that the call was 2
// previous to that the call was 3 
// x = 1 * 2 * 3 == 6
// ****************************************************************************

int fact(int x){
    if(x == 1){
        return 1;
    }
    else {
        return x * fact(x - 1);
    }
}

int main(void){

    int x = 11;

    printf("Factorial of %d is: %d\n", x, fact(x));

    return 0;

};

