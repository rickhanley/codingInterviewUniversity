#include <stdio.h>

int countdown(int x){
    if(x == 1){
        return printf("%d\n", x);
    } else {
        printf("%d\n", x);
        return countdown(x - 1);
    }
}

int main(void){

    countdown(20);

    return 0;
}