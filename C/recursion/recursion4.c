#include <stdio.h>

int fact(int x){

    if(x == 1){
        printf("Base case reached x == %d\nStack now begine to unwind\n", x);
        return 1;
    }
    else{
        printf("stack frame added for x = %d. This function is paused awaiting a return from fact(x - 1) of the previous call\n", x);
        return x * fact(x - 1);
    }
}

int main(void){

    printf("%d\n", fact(5));

    return 0;
}