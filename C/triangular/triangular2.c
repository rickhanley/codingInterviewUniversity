#include <stdio.h>

int triangular(int a){
    if(a == 1) {
        return 1;
    }
    else {
        return a + (triangular(a - 1));
    }
}

int main (void){

    printf("%d\n", triangular(3));
}